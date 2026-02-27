import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import textwrap
from pathlib import Path

# Data for the matrix - first column key is now 'Goal'
data = {
    'Goal': [
        'Compare: All Positive Values',
        'Compare: Mix of Pos/Neg',
        'Compare: Many Categories',
        'Time: Single Series',
        'Time: Multiple Series (≤5)',
        'Time: Multiple Series (>5)',
        'Geographic: Accurate Geography',
        'Geographic: Equal Comparison',
        'Part-to-Whole: ≤5 Categories',
        'Part-to-Whole: >5 or Precision',
        'Relationship: Correlation',
        'Relationship: Change Over Time',
        'Performance: Single Metric',
        'Performance: Multiple Metrics'
    ],
    'Data/Technical Team': [
        '**Chart:** Horizontal Bar\n\nInteractive filtering for deep dives.',
        '**Chart:** Diverging Bar\n\nEnable brushing to link data points.',
        '**Chart:** Dot Plot\n\nHigh information density is acceptable.',
        '**Chart:** Line Chart\n\nProvide full data download options.',
        '**Chart:** Multiple Lines\n\nAllow users to toggle series on/off.',
        '**Chart:** Small Multiples\n\nComplex but powerful; well-suited for this audience.',
        '**Chart:** Choropleth\n\nOverlay with filterable data layers.',
        '**Chart:** Tile Grid Map\n\nLink tiles to detailed data views.',
        '**Chart:** Pie Chart\n\nAcceptable, but include precise labels.',
        '**Chart:** Horizontal Bar\n\nSortable and filterable for exploration.',
        '**Chart:** Scatterplot\n\nAdd tooltips for details-on-demand.',
        '**Chart:** Connected Scatterplot\n\nGood for path analysis; allow animation or filtering.',
        '**Chart:** Bullet Graph\n\nShow detailed metrics on hover.',
        '**Chart:** Table with Bullets\n\nDashboard can be dense with drill-down capability.'
    ],
    'Program Managers': [
        '**Chart:** Horizontal Bar\n\nFocus on actual vs. target variance.',
        '**Chart:** Diverging Bar\n\nClearly show variance from goal.',
        '**Chart:** Dot Plot\n\nUse if it clearly shows performance against KPIs.',
        '**Chart:** Line Chart\n\nInclude sparklines to show trend context.',
        '**Chart:** Multiple Lines\n\nKeep to critical metrics; avoid clutter.',
        '**Chart:** Small Multiples\n\nGroup by team or region to compare performance.',
        '**Chart:** Choropleth\n\nUse for regional KPI monitoring.',
        '**Chart:** Tile Grid Map\n\nGood for at-a-glance state/region comparisons.',
        '**Chart:** Pie Chart\n\nUse sparingly, only for clear KPI composition.',
        '**Chart:** Horizontal Bar\n\nShow progress towards a total goal.',
        '**Chart:** Scatterplot\n\nUse to identify operational outliers.',
        '**Chart:** Connected Scatterplot\n\nTrack two related KPIs over time.',
        '**Chart:** Bullet Graph\n\nIdeal for single KPI tracking.',
        '**Chart:** Table with Bullets\n\nExcellent for a single-screen KPI dashboard.'
    ],
    'Executive Leadership': [
        '**Chart:** Horizontal Bar\n\nSimple, familiar, and clear.',
        '**Chart:** Diverging Bar\n\nUse an active title to state the "Big Idea".',
        '**Chart:** Dot Plot\n\nAVOID. Potentially too complex/unfamiliar.',
        '**Chart:** Line Chart\n\nFocus on the high-level trend. No more than 3-5 series.',
        '**Chart:** Multiple Lines\n\nKeep to 3-5 critical lines. Label directly.',
        '**Chart:** Small Multiples\n\nUse only if it simplifies the story.',
        '**Chart:** Choropleth\n\nAVOID. Too much detail, risk of misinterpretation.',
        '**Chart:** Tile Grid Map\n\nUse for simple, high-level regional summary.',
        '**Chart:** Pie Chart\n\nAcceptable for simple composition. Label clearly.',
        '**Chart:** Horizontal Bar\n\nSimple and effective. State conclusion in title.',
        '**Chart:** Scatterplot\n\nAVOID. Generally too complex for high-level summary.',
        '**Chart:** Connected Scatterplot\n\nAVOID. Too complex.',
        '**Chart:** Bullet Graph\n\nGood for summarizing a key metric vs. goal.',
        '**Chart:** Table with Bullets\n\nKeep table to 3-5 key metrics maximum.'
    ],
    'Public/Legislative Audience': [
        '**Chart:** Horizontal Bar\n\nAdd annotations to explain key points. Use people-first language.',
        '**Chart:** Diverging Bar\n\nUse plain language. Ensure high color contrast.',
        '**Chart:** Dot Plot\n\nUse simple bars instead for clarity.',
        '**Chart:** Line Chart\n\nClearly label axes and source. Provide text alternative.',
        '**Chart:** Multiple Lines\n\nEnsure colors are WCAG compliant. Add patterns/shapes.',
        '**Chart:** Small Multiples\n\nEnsure each chart is clearly titled and accessible.',
        '**Chart:** Choropleth\n\nExplain what the colors mean. Provide data table.',
        '**Chart:** Tile Grid Map\n\nMore accessible than a choropleth for comparison.',
        '**Chart:** Pie Chart\n\nDon\'t rely on color alone to distinguish slices.',
        '**Chart:** Horizontal Bar\n\nEnsure high contrast and provide a data table.',
        '**Chart:** Scatterplot\n\nInclude a clear explanation of what the chart shows.',
        '**Chart:** Connected Scatterplot\n\nLikely too complex. Use simpler trend charts.',
        '**Chart:** Bullet Graph\n\nExplain the components (target, actual).',
        '**Chart:** Table with Bullets\n\nEnsure table is 508 compliant (has proper headers).'
    ]
}
df = pd.DataFrame(data)

# --- Create the plot ---
fig, ax = plt.subplots(figsize=(20, 16))
ax.axis('off')

# Color palette
header_color = '#4393C3'
row_colors = ['#F0F0F0', '#FFFFFF']
cell_text_color = '#000000'
header_text_color = '#FFFFFF'
avoid_color_hex = '#A10000' # Dark Red

# General audience advice for headers
audience_headers = {
    'Data/Technical Team': 'Interactive, High Density, Drill-Down',
    'Program Managers': 'KPI-Focused, Actual vs. Target, Single Screen',
    'Executive Leadership': '"Big Idea" First, Simple Charts, 3-5 Metrics',
    'Public/Legislative Audience': 'Max Accessibility, Plain Language, Provide Context'
}

# Add table
ncols = len(df.columns)
nrows = len(df)
cell_height = 0.08
table_data = []

# Prepare cell text with wrapping and coloring
for i in range(nrows):
    row_data = []
    for j, col in enumerate(df.columns):
        text = str(df.loc[i, col])
        wrapped_text = ""

        if "**Chart:**" in text:
            # Format chart type in bold
            chart_type, description = text.split('\n\n', 1)
            chart_type_bold = f"$\\bf{{{chart_type.replace('**', '')}}}$"
            wrapped_text = f"{chart_type_bold}\n\n" + '\n'.join(textwrap.wrap(description, width=30))
        else:
            wrapped_text = '\n'.join(textwrap.wrap(text, width=30))
        
        row_data.append(wrapped_text)
    table_data.append(row_data)

# Prepare headers (handling the new 'Goal' column name)
column_headers = []
for col in df.columns:
    if col in audience_headers:
        header_text = f"$\\bf{{{col}}}$\n{audience_headers[col]}"
    else:
        # This will now correctly handle 'Goal'
        header_text = f"$\\bf{{{col}}}$"
    column_headers.append(header_text)

# Create table object
the_table = ax.table(cellText=table_data,
                     colLabels=column_headers,
                     loc='center',
                     cellLoc='left')

# Style the table
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)

for i in range(nrows + 1):
    for j in range(ncols):
        cell = the_table[i, j]
        cell.set_height(cell_height)
        cell.set_edgecolor('grey')
        cell.set_linewidth(0.5)
        cell.set_text_props(ha='left', va='center', wrap=True)
        
        if i == 0:  # Header row
            cell.set_facecolor(header_color)
            cell.set_text_props(color=header_text_color, weight='bold', ha='center')
        else:  # Data rows
            cell.set_facecolor(row_colors[(i - 1) % len(row_colors)])
            cell.set_text_props(color=cell_text_color)
            
            if j == 0:
                 cell.get_text().set_weight('bold')

# Adjust layout for padding
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

# Title is removed as requested

# Save the image next to this script
output_path = Path(__file__).resolve().parent / 'matrix_visualization.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')

print(f"Updated matrix visualization created as '{output_path.name}'")
