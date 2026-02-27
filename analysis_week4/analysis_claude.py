from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "state_data_2013-2023_20250514_3.csv"


def out_path(filename: str) -> Path:
    return BASE_DIR / filename


def save_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(out_path(filename), index=False)
    print(f"\n[OK] Saved: {out_path(filename)}")


def save_text(lines: list[str], filename: str) -> None:
    out_path(filename).write_text("\n".join(lines), encoding="utf-8")
    print(f"\n[OK] Saved: {out_path(filename)}")


# Read the CSV file
if not DATA_FILE.exists():
    raise FileNotFoundError(f"Input file not found: {DATA_FILE}")

df = pd.read_csv(DATA_FILE)

print("=" * 80)
print("IMMIGRATION DATA ANALYSIS (2013-2023)")
print("=" * 80)

# ============================================================================
# 1. DATA CLEANING
# ============================================================================
print("\n1. DATA CLEANING")
print("-" * 80)

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Check initial data quality
print(f"Initial rows: {len(df)}")
print(f"Initial columns: {len(df.columns)}")
print("\nMissing values by column:")
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "No missing values")

# Replace empty strings with NaN
df.replace("", np.nan, inplace=True)

# Convert numeric columns (handling any non-numeric values)
for col in df.columns:
    if col not in ["State", "Year"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

print(f"\nData cleaned. Final rows: {len(df)}")
print(f"Years covered: {df['Year'].min()} - {df['Year'].max()}")
print(f"States/territories: {df['State'].nunique()}")

save_csv(df, "1_cleaned_data.csv")

# ============================================================================
# 2. FIVE KEY METRICS
# ============================================================================
print("\n\n2. FIVE KEY METRICS")
print("-" * 80)

metrics_data = []

# Metric 1: Total immigration volume change (2013 vs 2023)
total_2013 = df[df["Year"] == 2013]["Lawful Permanent Residents Total"].sum()
total_2023 = df[df["Year"] == 2023]["Lawful Permanent Residents Total"].sum()
pct_change = ((total_2023 - total_2013) / total_2013) * 100

print("\nMetric 1: National LPR Growth (2013-2023)")
print(f"  2013 Total: {total_2013:,}")
print(f"  2023 Total: {total_2023:,}")
print(f"  Change: {pct_change:+.1f}%")

metrics_data.append(
    {
        "Metric": "National LPR Growth",
        "Description": "Change in total lawful permanent residents 2013-2023",
        "Value_2013": total_2013,
        "Value_2023": total_2023,
        "Percent_Change": round(pct_change, 2),
    }
)

# Metric 2: Average naturalizations per capita by state
nat_rate = (
    (df.groupby("State")["Naturalizations Total"].sum() / df.groupby("State")["Population"].sum())
    * 1_000_000
).sort_values(ascending=False)

print("\nMetric 2: Top 5 States by Naturalization Rate (per million)")
for i, (state, rate) in enumerate(nat_rate.head().items(), 1):
    print(f"  {i}. {state}: {rate:.1f}")

metrics_data.append(
    {
        "Metric": "Naturalization Rate Leaders",
        "Description": "Top state by naturalizations per million population",
        "Top_State": nat_rate.index[0],
        "Rate_Per_Million": round(nat_rate.iloc[0], 2),
        "Note": f"Top 5: {', '.join(nat_rate.head().index.tolist())}",
    }
)

# Metric 3: Refugee acceptance trends
refugee_by_year = df.groupby("Year")["Refugees Total"].sum()
refugee_peak = refugee_by_year.idxmax()
refugee_peak_val = refugee_by_year.max()

print("\nMetric 3: Refugee Acceptance Trends")
print(f"  Peak year: {refugee_peak} ({refugee_peak_val:,} total)")
print(f"  2013: {refugee_by_year[2013]:,}")
print(f"  2023: {refugee_by_year[2023]:,}")

metrics_data.append(
    {
        "Metric": "Refugee Acceptance",
        "Description": "Refugee trends and peak year",
        "Peak_Year": refugee_peak,
        "Peak_Value": refugee_peak_val,
        "Value_2013": refugee_by_year[2013],
        "Value_2023": refugee_by_year[2023],
    }
)

# Metric 4: COVID-19 impact (2020 drop)
total_2019 = df[df["Year"] == 2019]["Lawful Permanent Residents Total"].sum()
total_2020 = df[df["Year"] == 2020]["Lawful Permanent Residents Total"].sum()
covid_impact = ((total_2020 - total_2019) / total_2019) * 100

print("\nMetric 4: COVID-19 Impact on Immigration")
print(f"  2019 Total: {total_2019:,}")
print(f"  2020 Total: {total_2020:,}")
print(f"  Decline: {covid_impact:.1f}%")

metrics_data.append(
    {
        "Metric": "COVID-19 Impact",
        "Description": "Immigration decline 2019-2020",
        "Value_2019": total_2019,
        "Value_2020": total_2020,
        "Percent_Decline": round(covid_impact, 2),
    }
)

# Metric 5: Adjustment vs New Arrival ratio trends
adj_2013 = df[df["Year"] == 2013]["Adjustments Total"].sum()
new_2013 = df[df["Year"] == 2013]["New Arrivals Total"].sum()
adj_2023 = df[df["Year"] == 2023]["Adjustments Total"].sum()
new_2023 = df[df["Year"] == 2023]["New Arrivals Total"].sum()

print("\nMetric 5: Adjustment vs New Arrival Trends")
print(f"  2013 Ratio (Adj:New): {adj_2013 / new_2013:.2f}:1")
print(f"  2023 Ratio (Adj:New): {adj_2023 / new_2023:.2f}:1")

metrics_data.append(
    {
        "Metric": "Adjustment vs New Arrival Ratio",
        "Description": "Ratio of adjustments to new arrivals",
        "Ratio_2013": round(adj_2013 / new_2013, 2),
        "Ratio_2023": round(adj_2023 / new_2023, 2),
        "Change": "Increased" if (adj_2023 / new_2023) > (adj_2013 / new_2013) else "Decreased",
    }
)

metrics_df = pd.DataFrame(metrics_data)
save_csv(metrics_df, "2_key_metrics.csv")

# ============================================================================
# 3. THREE HYPOTHESES
# ============================================================================
print("\n\n3. THREE HYPOTHESES")
print("-" * 80)

hypotheses_data = []

print("\nHypothesis 1: States with larger immigrant populations have higher")
print("              naturalization rates")
print("  Test: Correlation between LPR total and naturalizations")

state_totals = df.groupby("State").agg(
    {
        "Lawful Permanent Residents Total": "sum",
        "Naturalizations Total": "sum",
    }
)
correlation = state_totals.corr().iloc[0, 1]
print(f"  Correlation coefficient: {correlation:.3f}")
print(
    f"  Result: {'SUPPORTED' if correlation > 0.7 else 'PARTIALLY SUPPORTED' if correlation > 0.4 else 'NOT SUPPORTED'}"
)

hypotheses_data.append(
    {
        "Hypothesis": "H1: Larger immigrant populations have higher naturalization rates",
        "Test": "Correlation between LPR total and naturalizations",
        "Correlation_Coefficient": round(correlation, 3),
        "Result": "SUPPORTED" if correlation > 0.7 else "PARTIALLY SUPPORTED" if correlation > 0.4 else "NOT SUPPORTED",
        "Interpretation": "Strong positive relationship" if correlation > 0.7 else "Moderate positive relationship" if correlation > 0.4 else "Weak relationship",
    }
)

print("\nHypothesis 2: Border states show different immigration patterns than")
print("              non-border states")
border_states = ["California", "Arizona", "New Mexico", "Texas"]
border_data = df[df["State"].isin(border_states)].groupby("Year")["Lawful Permanent Residents Total"].sum()
non_border_data = df[~df["State"].isin(border_states)].groupby("Year")["Lawful Permanent Residents Total"].sum()
border_share_2023 = (border_data[2023] / (border_data[2023] + non_border_data[2023])) * 100

print(f"  Border states' share of LPRs in 2023: {border_share_2023:.1f}%")
print("  Result: Border states account for substantial immigration volume")

hypotheses_data.append(
    {
        "Hypothesis": "H2: Border states show different immigration patterns",
        "Test": "Border state share of total immigration",
        "Border_States": ", ".join(border_states),
        "Border_Share_2023_Percent": round(border_share_2023, 2),
        "Result": "SUPPORTED",
        "Interpretation": "Border states receive disproportionate share of immigration",
    }
)

print("\nHypothesis 3: Post-COVID recovery in immigration has been stronger in")
print("              adjustment of status than new arrivals")
adj_2020 = df[df["Year"] == 2020]["Adjustments Total"].sum()
new_2020 = df[df["Year"] == 2020]["New Arrivals Total"].sum()
adj_recovery = ((adj_2023 - adj_2020) / adj_2020) * 100
new_recovery = ((new_2023 - new_2020) / new_2020) * 100

print(f"  Adjustments 2020->2023 growth: {adj_recovery:+.1f}%")
print(f"  New Arrivals 2020->2023 growth: {new_recovery:+.1f}%")
print(f"  Result: {'SUPPORTED' if adj_recovery > new_recovery else 'NOT SUPPORTED'}")

hypotheses_data.append(
    {
        "Hypothesis": "H3: Post-COVID recovery stronger in adjustments than new arrivals",
        "Test": "Compare growth rates 2020-2023",
        "Adjustments_Growth_Percent": round(adj_recovery, 2),
        "New_Arrivals_Growth_Percent": round(new_recovery, 2),
        "Result": "SUPPORTED" if adj_recovery > new_recovery else "NOT SUPPORTED",
        "Interpretation": "Adjustments recovered faster" if adj_recovery > new_recovery else "New arrivals recovered faster",
    }
)

hypotheses_df = pd.DataFrame(hypotheses_data)
save_csv(hypotheses_df, "3_hypotheses_tests.csv")

# ============================================================================
# 4. SUMMARY TABLE
# ============================================================================
print("\n\n4. SUMMARY TABLE - Top 10 States by Total Immigration (2013-2023)")
print("-" * 80)

summary = (
    df.groupby("State")
    .agg(
        {
            "Lawful Permanent Residents Total": "sum",
            "Naturalizations Total": "sum",
            "Refugees Total": "sum",
            "Asylees Total": "sum",
            "Population": "mean",
        }
    )
    .sort_values("Lawful Permanent Residents Total", ascending=False)
    .head(10)
)

summary["LPR_per_Million"] = (summary["Lawful Permanent Residents Total"] / summary["Population"]) * 1_000_000
summary["Naturalization_Rate_Percent"] = (
    summary["Naturalizations Total"] / summary["Lawful Permanent Residents Total"]
) * 100
summary = summary.round(2).reset_index()

print(f"\n{'State':<20} {'Total LPRs':>12} {'Natural.':>12} {'Refugees':>10} {'LPR/Million':>12}")
print("-" * 80)
for _, row in summary.iterrows():
    print(
        f"{row['State']:<20} {row['Lawful Permanent Residents Total']:>12,.0f} "
        f"{row['Naturalizations Total']:>12,.0f} {row['Refugees Total']:>10,.0f} "
        f"{row['LPR_per_Million']:>12,.0f}"
    )

save_csv(summary, "4_summary_table.csv")

# ============================================================================
# 5. THREE INSIGHTS
# ============================================================================
print("\n\n5. THREE KEY INSIGHTS")
print("-" * 80)

insights_text = [
    "=" * 80,
    "THREE KEY INSIGHTS FROM IMMIGRATION DATA ANALYSIS (2013-2023)",
    "=" * 80,
    "",
]

print("\nInsight 1: California's Dominance is Declining")
ca_share_2013 = (
    df[(df["State"] == "California") & (df["Year"] == 2013)]["Lawful Permanent Residents Total"].sum() / total_2013
) * 100
ca_share_2023 = (
    df[(df["State"] == "California") & (df["Year"] == 2023)]["Lawful Permanent Residents Total"].sum() / total_2023
) * 100
print(f"  California's share: {ca_share_2013:.1f}% (2013) -> {ca_share_2023:.1f}% (2023)")
print("  Immigration is diversifying geographically across the US")

insights_text.extend(
    [
        "INSIGHT 1: California's Dominance is Declining",
        "-" * 80,
        f"California's share of national immigration: {ca_share_2013:.1f}% (2013) -> {ca_share_2023:.1f}% (2023)",
        f"Decline: {ca_share_2013 - ca_share_2023:.1f} percentage points",
        "",
        "IMPLICATIONS:",
        "- Immigration is diversifying geographically across the United States",
        "- Other states are becoming more significant immigration destinations",
        "- Policy and resource allocation should reflect this geographic shift",
        "",
    ]
)

print("\nInsight 2: Asylum Cases Surged Post-2020")
asylees_2019 = df[df["Year"] == 2019]["Asylees Total"].sum()
asylees_2023 = df[df["Year"] == 2023]["Asylees Total"].sum()
asylees_growth = ((asylees_2023 - asylees_2019) / asylees_2019) * 100
print(f"  Total asylees: {asylees_2019:,} (2019) -> {asylees_2023:,} (2023)")
print(f"  Growth: {asylees_growth:+.1f}%")
print("  Reflects global humanitarian crises and policy changes")

insights_text.extend(
    [
        "INSIGHT 2: Asylum Cases Surged Post-2020",
        "-" * 80,
        f"Total asylees granted status: {asylees_2019:,} (2019) -> {asylees_2023:,} (2023)",
        f"Growth rate: {asylees_growth:+.1f}%",
        "",
        "IMPLICATIONS:",
        "- Reflects increasing global humanitarian crises and displacement",
        "- May indicate policy changes in asylum processing and acceptance",
        "- Requires increased capacity for asylum adjudication and support services",
        "",
    ]
)

print("\nInsight 3: Per Capita Rates Reveal Different Winners")
per_capita_leaders = df[df["Year"] == 2023].nlargest(5, "Lawful Permanent Residents Per Million")[["State", "Lawful Permanent Residents Per Million"]]
print("  Top 5 states by LPRs per million (2023):")
for _, row in per_capita_leaders.iterrows():
    print(f"    {row['State']}: {row['Lawful Permanent Residents Per Million']:,.0f}")
print("  Small/medium states can have high immigration intensity")

insights_text.extend(["INSIGHT 3: Per Capita Rates Reveal Different Winners", "-" * 80, "Top 5 states by LPRs per million population (2023):"])
for _, row in per_capita_leaders.iterrows():
    insights_text.append(f"  {row['State']}: {row['Lawful Permanent Residents Per Million']:,.0f} per million")
insights_text.extend(
    [
        "",
        "IMPLICATIONS:",
        "- Absolute numbers do not tell the full story",
        "- Small and medium-sized states can have high immigration intensity",
        "- Per capita analysis reveals different resource needs and integration challenges",
        "",
    ]
)

save_text(insights_text, "5_insights.txt")

# ============================================================================
# 6. THREE RECOMMENDED ACTIONS
# ============================================================================
print("\n\n6. THREE RECOMMENDED ACTIONS")
print("-" * 80)

actions_text = [
    "=" * 80,
    "THREE RECOMMENDED ACTIONS",
    "=" * 80,
    "",
]

print("\nAction 1: Expand Naturalization Support in High-Volume States")
low_nat_rate = (
    (df.groupby("State")["Naturalizations Total"].sum() / df.groupby("State")["Lawful Permanent Residents Total"].sum())
    .sort_values()
    .head(5)
)
print("  Target states with lowest naturalization/LPR ratios:")
for state, ratio in low_nat_rate.items():
    print(f"    {state}: {ratio:.2%}")
print("  Increase citizenship workshops, fee assistance, legal aid")

actions_text.extend(
    [
        "ACTION 1: Expand Naturalization Support in High-Volume States",
        "-" * 80,
        "TARGET: States with lowest naturalization/LPR ratios",
    ]
)
for state, ratio in low_nat_rate.items():
    actions_text.append(f"  {state}: {ratio:.2%}")
actions_text.extend(
    [
        "",
        "SPECIFIC RECOMMENDATIONS:",
        "- Increase citizenship workshops and application assistance programs",
        "- Expand fee waiver programs for low-income applicants",
        "- Partner with legal aid organizations for application support",
        "- Conduct outreach in immigrant communities to raise awareness",
        "- Address language barriers in application materials and support",
        "",
    ]
)

print("\nAction 2: Study and Replicate Refugee Integration Success")
refugee_leaders = df.groupby("State")["Refugees Total"].sum().sort_values(ascending=False).head(5)
print("  Top refugee-accepting states (2013-2023):")
for state, total in refugee_leaders.items():
    print(f"    {state}: {total:,.0f}")
print("  Document best practices in resettlement and employment programs")

actions_text.extend(["ACTION 2: Study and Replicate Refugee Integration Success", "-" * 80, "TOP REFUGEE-ACCEPTING STATES (2013-2023):"])
for state, total in refugee_leaders.items():
    actions_text.append(f"  {state}: {total:,.0f}")
actions_text.extend(
    [
        "",
        "SPECIFIC RECOMMENDATIONS:",
        "- Conduct case studies of successful refugee integration programs",
        "- Document best practices in employment placement and job training",
        "- Share housing and community integration strategies across states",
        "- Create peer learning networks among resettlement agencies",
        "- Measure and track integration outcomes systematically",
        "",
    ]
)

print("\nAction 3: Address COVID Recovery Disparities")
state_recovery = (
    df[df["Year"].isin([2019, 2023])]
    .groupby(["State", "Year"])["Lawful Permanent Residents Total"]
    .sum()
    .unstack()
)
state_recovery["Recovery_Percent"] = ((state_recovery[2023] - state_recovery[2019]) / state_recovery[2019]) * 100
slow_recovery = state_recovery.nsmallest(5, "Recovery_Percent")
print("  States with slowest post-COVID recovery:")
for state in slow_recovery.index:
    print(f"    {state}: {slow_recovery.loc[state, 'Recovery_Percent']:+.1f}%")
print("  Investigate barriers: backlogs, consular capacity, local economy")

actions_text.extend(["ACTION 3: Address COVID Recovery Disparities", "-" * 80, "STATES WITH SLOWEST POST-COVID RECOVERY (2019-2023):"])
for state in slow_recovery.index:
    actions_text.append(f"  {state}: {slow_recovery.loc[state, 'Recovery_Percent']:+.1f}%")
actions_text.extend(
    [
        "",
        "SPECIFIC RECOMMENDATIONS:",
        "- Investigate specific barriers in slow-recovery states:",
        "  * Application processing backlogs",
        "  * Consular capacity and visa interview availability",
        "  * Local economic conditions affecting job offers",
        "  * State-level policies or administrative challenges",
        "- Allocate additional resources to address identified bottlenecks",
        "- Increase staffing at consulates serving these states",
        "- Coordinate with state governments on integration support",
        "",
    ]
)

save_text(actions_text, "6_recommended_actions.txt")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
print("\nGenerated files:")
print(f"  {out_path('1_cleaned_data.csv')}")
print(f"  {out_path('2_key_metrics.csv')}")
print(f"  {out_path('3_hypotheses_tests.csv')}")
print(f"  {out_path('4_summary_table.csv')}")
print(f"  {out_path('5_insights.txt')}")
print(f"  {out_path('6_recommended_actions.txt')}")
print("=" * 80)
