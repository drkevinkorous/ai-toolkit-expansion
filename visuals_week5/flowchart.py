import graphviz
import textwrap
from pathlib import Path

# Colorblind-friendly palette from ColorBrewer (Set2, adapted)
colors = {
    'background': '#FFFFFF',
    'start_node': '#8da0cb',  # Blue-grey for start/end
    'goal_node': '#fc8d62',   # Orange for main goals
    'question_node': '#ffd92f', # Yellow for decisions
    'chart_node': '#66c2a4',  # Green for chart recommendations
    'edge_color': '#333333',
    'font_color': '#333333'
}

dot = graphviz.Digraph(
    'ChartSelectionFlowchart',
    comment='Decision Tree 1: Chart Selection',
    graph_attr={
        'rankdir': 'LR',      # Left to Right flow
        'splines': 'spline',  # Use curved splines for edges
        'dpi': '300',         # High DPI for clear presentation export
        'compound': 'true',   # Allow edges to connect to clusters
        'overlap': 'false',   # Prevent node overlap
        'fontsize': '10',
        'fontname': 'Helvetica',
        'bgcolor': colors['background']
    },
    node_attr={
        'fontname': 'Helvetica',
        'fontsize': '9',
        'shape': 'box',
        'style': 'filled,rounded',
        'fillcolor': colors['goal_node'],
        'color': colors['edge_color'],
        'fontcolor': colors['font_color']
    },
    edge_attr={
        'fontname': 'Helvetica',
        'fontsize': '8',
        'color': colors['edge_color'],
        'fontcolor': colors['edge_color']
    }
)

# Start Node
dot.node('start', 'START:\nWhat is your primary goal?', shape='Mdiamond', fillcolor=colors['start_node'], fontcolor='#FFFFFF')


# --- Goal 1: Compare values across categories ---
dot.node('goal_compare', 'Compare values across categories', shape='box', fillcolor=colors['goal_node'])
dot.edge('start', 'goal_compare')

dot.node('q_comp_pos', 'All values positive?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('goal_compare', 'q_comp_pos')
dot.node('chart_hbar', 'Horizontal Bar Chart', fillcolor=colors['chart_node'])
dot.edge('q_comp_pos', 'chart_hbar', label='Yes')

dot.node('q_comp_mix', 'Mix of pos/neg?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_comp_pos', 'q_comp_mix', label='No')
dot.node('chart_dbar', 'Diverging Bar Chart', fillcolor=colors['chart_node'])
dot.edge('q_comp_mix', 'chart_dbar', label='Yes')

dot.node('q_comp_many', 'Many categories?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_comp_mix', 'q_comp_many', label='No')
dot.node('chart_dot', 'Dot Plot', fillcolor=colors['chart_node'])
dot.edge('q_comp_many', 'chart_dot', label='Yes')
dot.node('chart_comp_default', 'Horizontal Bar Chart\n(few categories)', fillcolor=colors['chart_node'])
dot.edge('q_comp_many', 'chart_comp_default', label='No')


# --- Goal 2: Show change over time ---
dot.node('goal_time', 'Show change over time', shape='box', fillcolor=colors['goal_node'])
dot.edge('start', 'goal_time') # Connect from start, allowing parallel paths

dot.node('q_time_single', 'Single series?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('goal_time', 'q_time_single')
dot.node('chart_line', 'Line Chart', fillcolor=colors['chart_node'])
dot.edge('q_time_single', 'chart_line', label='Yes')

dot.node('q_time_multi5', 'Multiple series (≤5)?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_time_single', 'q_time_multi5', label='No')
dot.node('chart_mlines', 'Multiple Lines', fillcolor=colors['chart_node'])
dot.edge('q_time_multi5', 'chart_mlines', label='Yes')

dot.node('q_time_multiN', 'Multiple series (>5)?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_time_multi5', 'q_time_multiN', label='No')
dot.node('chart_smult', 'Small Multiples', fillcolor=colors['chart_node'])
dot.edge('q_time_multiN', 'chart_smult', label='Yes')
dot.node('chart_time_default', 'Consider Separate Charts', fillcolor=colors['chart_node'])
dot.edge('q_time_multiN', 'chart_time_default', label='No')


# --- Goal 3: Show geographic patterns ---
dot.node('goal_geo', 'Show geographic patterns', shape='box', fillcolor=colors['goal_node'])
dot.edge('start', 'goal_geo')

dot.node('q_geo_acc', 'Need accurate geography?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('goal_geo', 'q_geo_acc')
dot.node('chart_choro', 'Choropleth', fillcolor=colors['chart_node'])
dot.edge('q_geo_acc', 'chart_choro', label='Yes')

dot.node('q_geo_equal', 'Need equal comparison?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_geo_acc', 'q_geo_equal', label='No')
dot.node('chart_tile', 'Tile Grid Map', fillcolor=colors['chart_node'])
dot.edge('q_geo_equal', 'chart_tile', label='Yes')

dot.node('q_geo_loc', 'Showing specific locations?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_geo_equal', 'q_geo_loc', label='No')
dot.node('chart_point', 'Point Map', fillcolor=colors['chart_node'])
dot.edge('q_geo_loc', 'chart_point', label='Yes')
dot.node('chart_geo_default', 'Re-evaluate Goal', fillcolor=colors['chart_node'])
dot.edge('q_geo_loc', 'chart_geo_default', label='No')


# --- Goal 4: Show part-to-whole relationship ---
dot.node('goal_part', 'Show part-to-whole relationship', shape='box', fillcolor=colors['goal_node'])
dot.edge('start', 'goal_part')

dot.node('q_part_few', '≤5 categories, rough OK?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('goal_part', 'q_part_few')
dot.node('chart_pie', 'Pie Chart', fillcolor=colors['chart_node'])
dot.edge('q_part_few', 'chart_pie', label='Yes')

dot.node('q_part_prec', 'Need precision or >5 cats?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_part_few', 'q_part_prec', label='No')
dot.node('chart_hbar2', 'Horizontal Bar Chart', fillcolor=colors['chart_node'])
dot.edge('q_part_prec', 'chart_hbar2', label='Yes')

dot.node('q_part_change', 'Show composition change\nover time?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_part_prec', 'q_part_change', label='No')
dot.node('chart_bartime', 'Separate Bar Charts\nor Slope Chart', fillcolor=colors['chart_node'])
dot.edge('q_part_change', 'chart_bartime', label='Yes')
dot.node('chart_part_default', 'Re-evaluate Goal', fillcolor=colors['chart_node'])
dot.edge('q_part_change', 'chart_part_default', label='No')


# --- Goal 5: Show relationship between two variables ---
dot.node('goal_rel', 'Show relationship\nbetween two variables', shape='box', fillcolor=colors['goal_node'])
dot.edge('start', 'goal_rel')

dot.node('q_rel_corr', 'Looking for correlation?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('goal_rel', 'q_rel_corr')
dot.node('chart_scatter', 'Scatterplot', fillcolor=colors['chart_node'])
dot.edge('q_rel_corr', 'chart_scatter', label='Yes')

dot.node('q_rel_time', 'Show change over time?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_rel_corr', 'q_rel_time', label='No')
dot.node('chart_cscatter', 'Connected Scatterplot', fillcolor=colors['chart_node'])
dot.edge('q_rel_time', 'chart_cscatter', label='Yes')

dot.node('q_rel_2series', 'Comparing two series\nover time?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_rel_time', 'q_rel_2series', label='No')
dot.node('chart_smult2', 'Small Multiples', fillcolor=colors['chart_node'])
dot.edge('q_rel_2series', 'chart_smult2', label='Yes')
dot.node('chart_rel_default', 'Re-evaluate Goal', fillcolor=colors['chart_node'])
dot.edge('q_rel_2series', 'chart_rel_default', label='No')


# --- Goal 6: Show performance against target ---
dot.node('goal_perf', 'Show performance\nagainst target', shape='box', fillcolor=colors['goal_node'])
dot.edge('start', 'goal_perf')

dot.node('q_perf_single', 'Single metric?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('goal_perf', 'q_perf_single')
dot.node('chart_bullet', 'Bullet Graph', fillcolor=colors['chart_node'])
dot.edge('q_perf_single', 'chart_bullet', label='Yes')

dot.node('q_perf_multi', 'Multiple metrics?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_perf_single', 'q_perf_multi', label='No')
dot.node('chart_bullet_table', 'Table with Bullet Graphs', fillcolor=colors['chart_node'])
dot.edge('q_perf_multi', 'chart_bullet_table', label='Yes')

dot.node('q_perf_trend', 'Need trend context?', shape='ellipse', fillcolor=colors['question_node'])
dot.edge('q_perf_multi', 'q_perf_trend', label='No')
dot.node('chart_sparklines', 'Sparklines in table', fillcolor=colors['chart_node'])
dot.edge('q_perf_trend', 'chart_sparklines', label='Yes')
dot.node('chart_perf_default', 'Re-evaluate Goal', fillcolor=colors['chart_node'])
dot.edge('q_perf_trend', 'chart_perf_default', label='No')


# Render and save the image
output_stem = Path(__file__).resolve().parent / 'chart_selection_flowchart'
dot.render(str(output_stem), format='png', cleanup=True)
print("Chart Selection Flowchart created as 'chart_selection_flowchart.png'")
