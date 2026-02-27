from pathlib import Path
import numpy as np
import pandas as pd


def load_dataset(base_dir: Path) -> tuple[pd.DataFrame, Path]:
    """Load the first supported dataset file in the target directory."""
    csv_files = sorted(base_dir.glob("*.csv"))
    xlsx_files = sorted(base_dir.glob("*.xlsx"))
    generated_outputs = {
        "cleaned_data.csv",
        "summary_table.csv",
        "proposed_metrics.csv",
        "hypotheses_results.csv",
    }

    preferred_csv = [p for p in csv_files if p.name.lower().startswith("state_data")]
    fallback_csv = [p for p in csv_files if p.name not in generated_outputs]

    if xlsx_files:
        file_path = xlsx_files[0]
        df = pd.read_excel(file_path)
        return df, file_path

    if preferred_csv:
        file_path = preferred_csv[0]
        df = pd.read_csv(file_path)
        return df, file_path

    if fallback_csv:
        file_path = fallback_csv[0]
        df = pd.read_csv(file_path)
        return df, file_path

    raise FileNotFoundError("No .csv or .xlsx file found in analysis_week4 directory.")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning and type standardization."""
    cleaned = df.copy()

    cleaned.columns = [c.strip() for c in cleaned.columns]
    if "State" in cleaned.columns:
        cleaned["State"] = cleaned["State"].astype(str).str.strip()

    numeric_cols = [c for c in cleaned.columns if c not in ["State"]]
    for col in numeric_cols:
        cleaned[col] = pd.to_numeric(cleaned[col], errors="coerce")

    # Keep rows with core identifiers and remove obvious duplicates.
    required_cols = [c for c in ["State", "Year", "Population"] if c in cleaned.columns]
    cleaned = cleaned.dropna(subset=required_cols)
    cleaned = cleaned.drop_duplicates()

    # Restrict to expected analysis window when available.
    if "Year" in cleaned.columns:
        cleaned = cleaned[(cleaned["Year"] >= 2013) & (cleaned["Year"] <= 2023)]

    return cleaned


def build_summary_table(df: pd.DataFrame) -> pd.DataFrame:
    """Year-level summary table with core totals and rates."""
    totals = {
        "Population": "sum",
        "Lawful Permanent Residents Total": "sum",
        "New Arrivals Total": "sum",
        "Nonimmigrants Total": "sum",
        "Naturalizations Total": "sum",
        "Refugees Total": "sum",
        "Asylees Total": "sum",
    }
    available_totals = {k: v for k, v in totals.items() if k in df.columns}

    summary = (
        df.groupby("Year", as_index=False)
        .agg(available_totals)
        .sort_values("Year")
    )

    if {"Lawful Permanent Residents Total", "Naturalizations Total"}.issubset(summary.columns):
        summary["Naturalizations-to-LPR Inflow Ratio"] = np.where(
            summary["Lawful Permanent Residents Total"] > 0,
            summary["Naturalizations Total"] / summary["Lawful Permanent Residents Total"],
            np.nan,
        )
        summary["LPR Total (Trailing 5yr Avg)"] = summary["Lawful Permanent Residents Total"].rolling(
            window=5, min_periods=3
        ).mean()
        summary["Naturalizations-to-Trailing-5yr-LPR Ratio"] = np.where(
            summary["LPR Total (Trailing 5yr Avg)"] > 0,
            summary["Naturalizations Total"] / summary["LPR Total (Trailing 5yr Avg)"],
            np.nan,
        )

    if {"Refugees Total", "Asylees Total", "Lawful Permanent Residents Total", "Nonimmigrants Total"}.issubset(summary.columns):
        volume = (
            summary["Lawful Permanent Residents Total"]
            + summary["Nonimmigrants Total"]
            + summary["Refugees Total"]
            + summary["Asylees Total"]
        )
        summary["Humanitarian Share"] = np.where(
            volume > 0,
            (summary["Refugees Total"] + summary["Asylees Total"]) / volume,
            np.nan,
        )

    return summary


def propose_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Create and summarize five actionable metrics."""
    work = df.copy()

    total_volume_cols = [
        c for c in [
            "Lawful Permanent Residents Total",
            "Nonimmigrants Total",
            "Naturalizations Total",
            "Refugees Total",
            "Asylees Total",
        ]
        if c in work.columns
    ]

    work["Total Immigration Volume"] = work[total_volume_cols].sum(axis=1)

    work["Immigration Intensity (per 100k)"] = np.where(
        work["Population"] > 0,
        work["Total Immigration Volume"] / work["Population"] * 100000,
        np.nan,
    )

    work["Naturalizations-to-LPR Inflow Ratio"] = np.where(
        work["Lawful Permanent Residents Total"] > 0,
        work["Naturalizations Total"] / work["Lawful Permanent Residents Total"],
        np.nan,
    )

    work["Humanitarian Share"] = np.where(
        work["Total Immigration Volume"] > 0,
        (work["Refugees Total"] + work["Asylees Total"]) / work["Total Immigration Volume"],
        np.nan,
    )

    state_year = work.sort_values(["State", "Year"]).copy()
    state_year["LPR Total (Trailing 5yr Avg)"] = (
        state_year.groupby("State")["Lawful Permanent Residents Total"]
        .rolling(window=5, min_periods=3)
        .mean()
        .reset_index(level=0, drop=True)
    )
    state_year["Naturalizations-to-Trailing-5yr-LPR Ratio"] = np.where(
        state_year["LPR Total (Trailing 5yr Avg)"] > 0,
        state_year["Naturalizations Total"] / state_year["LPR Total (Trailing 5yr Avg)"],
        np.nan,
    )
    state_year["Volume Growth YoY"] = state_year.groupby("State")["Total Immigration Volume"].pct_change()

    metrics = pd.DataFrame(
        {
            "Metric": [
                "Total Immigration Volume",
                "Immigration Intensity (per 100k)",
                "Naturalizations-to-LPR Inflow Ratio",
                "Naturalizations-to-Trailing-5yr-LPR Ratio",
                "Humanitarian Share",
            ],
            "Definition": [
                "LPR + Nonimmigrants + Naturalizations + Refugees + Asylees",
                "Total Immigration Volume divided by Population, scaled by 100k",
                "Naturalizations Total divided by same-year LPR admissions",
                "Naturalizations Total divided by trailing 5-year average LPR admissions",
                "(Refugees + Asylees) divided by Total Immigration Volume",
            ],
            "Dataset Mean": [
                work["Total Immigration Volume"].mean(),
                work["Immigration Intensity (per 100k)"].mean(),
                work["Naturalizations-to-LPR Inflow Ratio"].mean(),
                state_year["Naturalizations-to-Trailing-5yr-LPR Ratio"].mean(),
                work["Humanitarian Share"].mean(),
            ],
        }
    )

    return metrics, work, state_year


def evaluate_hypotheses(state_year: pd.DataFrame) -> pd.DataFrame:
    """Generate three hypotheses and evaluate with simple correlations."""
    hypo_rows = []

    # Hypothesis 1: Nonimmigrant intensity is positively associated with naturalization intensity.
    h1 = state_year[["Nonimmigrants Per Million", "Naturalizations Per Million"]].dropna()
    h1_corr = h1["Nonimmigrants Per Million"].corr(h1["Naturalizations Per Million"]) if not h1.empty else np.nan
    hypo_rows.append(
        {
            "Hypothesis": "States with higher nonimmigrant rates have higher naturalization rates.",
            "Test": "Correlation(Nonimmigrants Per Million, Naturalizations Per Million)",
            "Result": h1_corr,
            "Interpretation": "Supported" if pd.notna(h1_corr) and h1_corr > 0.2 else "Weak/Not supported",
        }
    )

    # Hypothesis 2: Larger new-arrival rates are associated with higher LPR rates.
    h2 = state_year[["New Arrivals Per Million", "Lawful Permanent Residents Per Million"]].dropna()
    h2_corr = h2["New Arrivals Per Million"].corr(h2["Lawful Permanent Residents Per Million"]) if not h2.empty else np.nan
    hypo_rows.append(
        {
            "Hypothesis": "States with more new arrivals per capita also show higher LPR rates.",
            "Test": "Correlation(New Arrivals Per Million, LPR Per Million)",
            "Result": h2_corr,
            "Interpretation": "Supported" if pd.notna(h2_corr) and h2_corr > 0.2 else "Weak/Not supported",
        }
    )

    # Hypothesis 3: Higher humanitarian intensity coincides with lower lag-adjusted naturalization ratio.
    h3 = state_year[
        ["Refugees Per Million", "Asylees Per Million", "Naturalizations-to-Trailing-5yr-LPR Ratio"]
    ].dropna()
    if not h3.empty:
        h3["Humanitarian Per Million"] = h3["Refugees Per Million"] + h3["Asylees Per Million"]
        h3_corr = h3["Humanitarian Per Million"].corr(h3["Naturalizations-to-Trailing-5yr-LPR Ratio"])
    else:
        h3_corr = np.nan
    hypo_rows.append(
        {
            "Hypothesis": "Higher humanitarian inflow intensity is associated with lower lag-adjusted naturalization ratio.",
            "Test": "Correlation((Refugees+Asylees) Per Million, Naturalizations-to-Trailing-5yr-LPR Ratio)",
            "Result": h3_corr,
            "Interpretation": "Supported" if pd.notna(h3_corr) and h3_corr < -0.2 else "Weak/Not supported",
        }
    )

    return pd.DataFrame(hypo_rows)


def generate_insights_and_actions(summary: pd.DataFrame, state_year: pd.DataFrame) -> tuple[list[str], list[str]]:
    insights = []
    actions = []

    latest_year = int(summary["Year"].max())
    latest = state_year[state_year["Year"] == latest_year].copy()

    # Insight 1: Highest intensity states in latest year.
    top_intensity = latest.nlargest(3, "Immigration Intensity (per 100k)")["State"].tolist()
    insights.append(f"In {latest_year}, immigration intensity is most concentrated in: {', '.join(top_intensity)}.")
    actions.append("Prioritize outreach capacity and service delivery planning in top-intensity states.")

    # Insight 2: Growth trend from first to last year.
    first_year = int(summary["Year"].min())
    first_vol = state_year[state_year["Year"] == first_year]["Total Immigration Volume"].sum()
    last_vol = state_year[state_year["Year"] == latest_year]["Total Immigration Volume"].sum()
    change_pct = ((last_vol - first_vol) / first_vol * 100) if first_vol > 0 else np.nan
    insights.append(f"Total immigration volume changed by {change_pct:.1f}% from {first_year} to {latest_year}.")
    actions.append("Use year-over-year triggers to scale staffing and budgets before high-growth years.")

    # Insight 3: Humanitarian share level in latest year.
    latest_hum_share = summary.loc[summary["Year"] == latest_year, "Humanitarian Share"].iloc[0]
    insights.append(f"Humanitarian pathways represent {latest_hum_share:.2%} of measured volume in {latest_year}.")
    actions.append("Segment programs by pathway (economic/family/humanitarian) and track outcomes separately.")

    return insights, actions


def write_insights_actions_txt(base_dir: Path, insights: list[str], actions: list[str]) -> None:
    output_path = base_dir / "insights_actions.txt"
    with output_path.open("w", encoding="utf-8") as f:
        f.write("Insights (3)\n")
        for i, insight in enumerate(insights, start=1):
            f.write(f"{i}. {insight}\n")
        f.write("\nActions (3)\n")
        for i, action in enumerate(actions, start=1):
            f.write(f"{i}. {action}\n")


def safe_to_csv(df: pd.DataFrame, path: Path) -> None:
    try:
        df.to_csv(path, index=False)
    except PermissionError:
        print(f"Warning: could not write {path.name} (file is locked).")


def main() -> None:
    base_dir = Path(__file__).resolve().parent

    raw_df, source_file = load_dataset(base_dir)
    cleaned_df = clean_data(raw_df)

    metrics_df, enriched_df, state_year_df = propose_metrics(cleaned_df)
    summary_df = build_summary_table(cleaned_df)
    hypotheses_df = evaluate_hypotheses(state_year_df)
    insights, actions = generate_insights_and_actions(summary_df, state_year_df)

    # Persist outputs for review.
    write_insights_actions_txt(base_dir, insights, actions)
    safe_to_csv(cleaned_df, base_dir / "cleaned_data.csv")
    safe_to_csv(summary_df, base_dir / "summary_table.csv")
    safe_to_csv(metrics_df, base_dir / "proposed_metrics.csv")
    safe_to_csv(hypotheses_df, base_dir / "hypotheses_results.csv")

    print("=== Source File ===")
    print(source_file.name)

    print("\n=== Cleaning Completed ===")
    print(f"Rows after cleaning: {len(cleaned_df):,}")
    print(f"Columns retained: {len(cleaned_df.columns)}")

    print("\n=== Proposed Metrics (5) ===")
    print(metrics_df.to_string(index=False))

    print("\n=== Hypotheses (3) ===")
    print(hypotheses_df.to_string(index=False))

    print("\n=== Summary Table (first 10 rows) ===")
    print(summary_df.head(10).to_string(index=False))

    print("\n=== Insights (3) ===")
    for i, insight in enumerate(insights, start=1):
        print(f"{i}. {insight}")

    print("\n=== Actions (3) ===")
    for i, action in enumerate(actions, start=1):
        print(f"{i}. {action}")

    print("\n=== Note on Additional Data ===")
    print(
        "For stronger causal analysis, add external context such as state labor-market, unemployment, wage, housing, and policy data."
    )


if __name__ == "__main__":
    main()
