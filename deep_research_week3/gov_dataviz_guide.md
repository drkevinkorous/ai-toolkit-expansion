# Evidence-Informed Data Visualization for Government Decision-Making

## Purpose and Scope

This synthesis integrates all evidence reviewed to date, including foundational perceptual science, replication and refinement studies, debates over chart types and embellishment, government accessibility and equity standards, and practitioner consensus on executive communication. It draws on the original deep research, subsequent validation, and four structured research queries addressing core science, government standards and accessibility, chart-specific debates, and executive communication.

The goal is not to prescribe a single "correct" visualization style, but to articulate **evidence-informed principles** that improve decision quality, reduce interpretive risk, and uphold legal and ethical responsibilities in U.S. government contexts. Where the literature shows variability, findings are framed as **heuristics conditioned on task, audience, and context**, rather than universal rules.

---

## Quick Reference: Strength of Recommendations

Recommendations in this guide are classified by evidence strength:

**Level 1 (Strong):** Multiple high-quality studies, consistent findings, or legal requirements
- Use position on common scale for critical comparisons
- Meet WCAG 2.1 AA contrast requirements (legal obligation)
- Avoid dual-axis charts for executive communication
- Apply accessibility standards (Section 508/WCAG)

**Level 2 (Moderate):** Limited direct evidence but strong logical basis
- Use active titles to state conclusions
- Apply "Big Idea" framing for executive briefings
- Prefer tile grid maps over choropleths for state comparisons
- Use bullet graphs instead of gauges for KPI displays

**Level 3 (Weak):** Professional consensus, context-dependent
- Dashboard should fit on single screen (may not apply to mobile)
- Embellishment can improve memorability (depends on audience/purpose)
- Executives prefer brief summaries (observed but not rigorously measured)

**Level 4 (Conditional):** Use only in specific circumstances
- Pie charts: acceptable for simple part-to-whole with ≤5 categories
- Stacked bars: acceptable for showing total composition, not segment comparison
- 3D charts: avoid except for specific spatial data representation

---

## I. Foundations: How People Perceive Visual Information

### 1. Perceptual Accuracy Is Probabilistic, Not Absolute

**Evidence Level: Strong (Level 1)**

Research in graphical perception demonstrates that people do not interpret all visual encodings equally well. Classic work by Cleveland and McGill (1984, 1987) established a hierarchy of perceptual tasks, showing that quantitative judgments based on **position along a common scale** are, on average, more accurate than judgments based on length, angle, area, or color intensity.

**The Cleveland & McGill Hierarchy (Verified)**

The original experiments tested 10 elementary perceptual tasks across multiple studies. Modern synthesis groups these into 5 major levels:

1. **Position along a common scale** (highest accuracy) - comparing points on scatter plot or bar chart tops with shared baseline
2. **Position on identical nonaligned scales** - comparing elements in small multiples with identical but separate scales
3. **Length, angle, direction** - judging bar length, line slope, or pie slice angle
4. **Area** - judging relative size of areas (bubble charts, treemaps)
5. **Volume, curvature, color saturation** (lowest accuracy) - 3D volumes, curved lines, color intensity

**Important Nuances from Replication Studies:**

Heer and Bostock (2010) and subsequent large-sample studies confirm the overall ordering while adding important qualifications:
- Effect-size differences between encodings are smaller than originally reported
- Performance varies by task and data complexity
- Individual differences are substantial (Davis et al. 2022)
- For some tasks, angle judgments can be slightly more accurate than length judgments

These findings indicate that perceptual rankings describe **aggregate tendencies**, not deterministic outcomes. While bar charts perform best on average, 20-25% of individuals may consistently perform better with other chart types.

**Implication for government use:** When accuracy and defensibility matter—as in oversight, budgeting, or policy evaluation—designs should default to encodings with the strongest average performance while reinforcing interpretation through labeling and contextual explanation.

**Confidence Level: Very High** - Replicated across multiple studies with consistent findings

---

### 2. Visual Variables and Their Modern Interpretation

**Evidence Level: Strong (Level 1)**

Jacques Bertin's theory of visual variables remains foundational. His distinction between **ordered variables** (position, size, lightness) and **associative variables** (hue, shape) continues to guide effective design choices (Bertin, 1967).

Bertin identified seven core visual variables:
- Position
- Size (length, area)
- Shape
- Color Hue (e.g., red, green, blue)
- Color Value (lightness/darkness)
- Orientation
- Texture

Later work by Mackinlay (1986) operationalized Bertin's framework for applied and automated design. Key refinements include evidence that lightness/value within a single hue can function as an ordinal encoding in constrained contexts, while color hue and shape remain unsuitable for precise magnitude comparison.

**Implication:** Visual variables must be matched to data type and task; misuse—such as hue gradients for exact values—degrades interpretability.

**Confidence Level: Very High** - Foundational theoretical work validated by decades of practice

---

## II. From Analysis to Communication: Narrative Matters

**Evidence Level: Moderate (Level 2)**

A critical distinction in visualization practice is between **exploratory** analysis and **explanatory** communication. Executive and leadership audiences primarily require explanatory visuals that answer a specific question and support a decision.

### The Knaflic Methodology

Narrative-based methods, particularly those articulated by Knaflic (2015), emphasize defining a clear context, articulating a single "Big Idea," reducing clutter, and using titles and annotations to state conclusions directly. 

**Core Steps:**
1. **Understand the context** - Who is your audience? What do they need to know or do?
2. **Define the "Big Idea"** - Distill your message into one memorable sentence
3. **Choose simple visuals** - Bar, line, dot charts that are easy to interpret
4. **Eliminate clutter** - Maximize signal-to-noise ratio
5. **Focus attention** - Use color and annotation strategically
6. **Tell a story** - Clear beginning, middle, and end
7. **Use active titles** - State conclusions, not just topics

**Evidence Base:**

While Knaflic's "Big Idea" concept is based on communication theory and rhetoric rather than a specific empirical study, experimental research supports related practices:

- **Active titles:** Kong et al. (2019) found that charts with "message-bearing" titles led to faster and more accurate interpretation compared to descriptive titles
- **Storytelling effectiveness:** Kosara & Mackinlay (2013) demonstrated that narrative structure makes visualizations more engaging and memorable
- **Persuasion:** Zubeida et al. (2021) found data stories combining charts with narrative were more persuasive than charts alone

**Implication:** In government briefings, visuals should communicate conclusions explicitly rather than relying on viewers to infer meaning.

**Confidence Level: High** - Strong supporting evidence for individual components, though full methodology not experimentally validated as a package

---

## III. Accessibility and Equity as Core Design Requirements

### 1. Accessibility Standards

**Evidence Level: Strong (Level 1) - Legal Requirement**

U.S. government visualizations are subject to Section 508 and the Web Content Accessibility Guidelines (WCAG 2.1 and 2.2), operationalized through systems such as the U.S. Web Design System (USWDS). 

**Core Requirements:**

**Color and Contrast:**
- **WCAG SC 1.4.1:** Do not rely on color alone to convey information
- **WCAG SC 1.4.3 (Level AA):** Minimum contrast ratio of 4.5:1 for normal text, 3:1 for large text (18pt/24px or 14pt/18.66px bold)
- **WCAG SC 1.4.11 (Level AA):** Minimum contrast ratio of 3:1 for graphical objects and UI components
- **WCAG SC 1.4.6 (Level AAA):** Enhanced contrast of 7:1 for normal text, 4.5:1 for large text

**USWDS "Magic Number":** A difference of 50+ between color grades ensures WCAG AA ratio of at least 4.5:1

**Text Alternatives:**
- Provide clear, concise summary of chart's main message
- Include accessible data table with underlying data (can be visually hidden but available to screen readers)
- Use descriptive alt text for chart images
- Ensure proper HTML structure with `<th>` tags for headers

**Keyboard Operability:**
- All interactive elements (filters, tooltips, zoom) must be fully operable using keyboard only
- Ensure logical tab order and visible focus indicators

**Research Evidence:** Usability research indicates that accessibility-compliant designs improve clarity and usability for all users, not only those with disabilities.

**Confidence Level: Very High** - Legal requirement with clear technical specifications

**Official Documentation:**
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- USWDS Data Visualizations: https://designsystem.digital.gov/components/data-visualizations/
- Section 508: https://www.section508.gov/
- UK GDS Accessibility: https://analysisfunction.civilservice.gov.uk/guidance-and-research/accessibility/

---

### 2. Equity and the "Do No Harm" Framework

**Evidence Level: Moderate (Level 2)**

Visualization choices influence interpretation of data about people. Equity-centered guidance from the Urban Institute (published June 9, 2021) emphasizes people-first language, neutral ordering of demographic groups, avoidance of stereotypical color use, contextualization of disparities with structural explanations, and transparent treatment of missing or excluded populations.

**Core Practices:**

**People-First Language:**
- Use "people experiencing homelessness" not "the homeless"
- Use "Black people" not "Blacks"
- Center the humanity of individuals

**Thoughtful Ordering:**
- Avoid default orderings that place "White" or "Male" first, reinforcing them as the norm
- Consider ordering alphabetically, by sample size, or by magnitude of results

**Purposeful Color Selection:**
- Avoid colors that reinforce gender or racial stereotypes (pink for women, blue for men)
- Do not use sequential color palettes (light to dark) for distinct demographic groups
- Avoid suggesting hierarchical relationships through color

**Frame Disparities with Context:**
- Provide context about systemic forces (e.g., structural racism) that drive disparities
- Avoid "deficit framing" that can lead to blaming communities
- Acknowledge historical and structural explanations

**Handle Missing Data Thoughtfully:**
- Acknowledge which groups are missing and why
- Avoid generic "Other" category
- Use descriptive labels like "Identity not listed" or "Additional groups"

**Evidence Base:**

The Urban Institute guide is based on qualitative methodology (interviews with nearly 20 data practitioners) and represents expert recommendations. Supporting empirical evidence includes:

- **Xiong et al. (2023, 2024):** Demonstrated that visualization design choices significantly influence interpretation and can increase political polarization; highlighting partisan gaps can induce social conformity
- **Framing effects:** Pre-existing beliefs bias interpretation of data; effect can be mitigated or exacerbated by textual annotations

**Implication:** Equity considerations are integral to credibility, ethical responsibility, and public trust in government communication.

**Confidence Level: High** - Strong ethical foundation with growing empirical support for framing effects

---

## IV. Chart Types: What the Evidence Supports

### Evidence-Based Chart Selection

The research literature supports relative preferences rather than absolute prohibitions:

**Bar Charts and Dot Plots** *(Level 1 - Strong)*
- Most reliable for comparisons due to aligned baselines (Cleveland & McGill, 1984)
- Use horizontal bars for long category labels
- Use diverging bars for positive/negative values
- **Confidence: Very High**

**Line Charts** *(Level 1 - Strong)*
- Effective for trends over time when scales are consistent and annotated
- Superior to stacked areas for comparing multiple series
- **Confidence: Very High**

**Pie Charts** *(Level 4 - Conditional)*
- Acceptable for simple part-to-whole tasks with ≤5 categories
- Weaker for precise comparison (Simkin & Hastie, 1987)
- Historical research shows mixed results depending on task
- **Use only when:** showing rough proportions, few slices, part-to-whole focus
- **Confidence: Medium** - Context-dependent effectiveness

**Stacked Bar Charts** *(Level 4 - Conditional)*
- Difficult for comparing non-baseline segments (Cleveland & McGill, 1984; Talbot et al., 2014)
- Suitable primarily for showing composition of totals
- **Use only when:** focus is on total values and overall composition, not segment comparison
- **Better alternatives:** Grouped bar charts for component comparison, line charts for trends
- **Confidence: High** - Clear evidence of perceptual difficulty

**Dual-Axis Charts** *(Level 1 - Avoid)*
- High risk of misinterpretation and scale manipulation
- Viewers misinterpret where lines cross (mathematically meaningless)
- Isenberg et al. (2011) found them "very confusing" with poor accuracy
- Generally inappropriate for executive communication
- **Better alternatives:** Small multiples, connected scatterplots
- **Confidence: Very High** - Strong evidence against use

**Choropleth Maps** *(Level 4 - Conditional)*
- Useful for rate-based geographic patterns
- Vulnerable to area bias (large areas dominate visually)
- Subject to Modifiable Areal Unit Problem (MAUP) - patterns can be artifacts of boundary choices
- **Use only when:** geographic location matters more than precise comparison
- **Better alternative:** Tile grid maps for state-level comparisons
- **Confidence: High** - Well-documented limitations

**Tile Grid Maps** *(Level 2 - Moderate)*
- Mitigate area bias by giving each region equal visual weight
- Enable clearer at-a-glance comparisons
- Best for familiar geographies (U.S. states)
- **Trade-off:** Sacrifice geographic accuracy
- **Confidence: Medium** - Strong logical basis, limited formal usability testing

**3D Charts** *(Level 1 - Avoid)*
- Lead to less accurate judgments (Zacks et al., 1998)
- Perspective distortion acts as "chartjunk"
- Increases cognitive load without benefit
- **Confidence: Very High** - Clear experimental evidence

---

### Embellishment and Memorability: The Chartjunk Debate

**The Tension:** Minimalist principles vs. memorability research

**Position A: Minimalism (Tufte)**
- Maximize data-ink ratio
- Remove all "chartjunk" that doesn't aid comprehension
- **Evidence Quality:** Medium - Strong design principles and expert opinion, not originally experimentally validated

**Position B: Thoughtful Embellishment**
- Bateman et al. (2010): Embellished charts were significantly more memorable after 2-3 weeks without harming comprehension
- Borkin et al. (2013): Visualizations with human-recognizable objects, more color, and higher visual density were more memorable
- **Evidence Quality:** High - Peer-reviewed experimental studies

**Reconciliation (Level 3 - Context-Dependent):**

Design choices should follow purpose:
- **For analytical clarity** (reports, dashboards, expert analysis): Minimalism excels
- **For engagement and recall** (presentations, public communication, journalism): Thoughtful embellishment can help
- **Key principle:** Embellishments should make the *data* memorable, not just the decoration

**Implication:** Design choices should follow purpose—analysis versus communication—rather than strict stylistic ideology.

**Confidence Level: High** - Clear evidence that both approaches have merit in different contexts

---

## V. Executive Communication in Government

**Evidence Level: Mixed (Levels 2-3)**

Direct experimental research on executive audiences is limited. Nevertheless, converging evidence from cognitive science, usability research, and professional practice supports several consistent heuristics.

### Dashboard Design Principles

**Single-Screen Display** *(Level 3 - Weak)*
- **Rationale:** Stephen Few's recommendation based on cognitive load theory - scrolling fragments attention and burdens working memory
- **Evidence:** Theoretical reasoning, not direct empirical validation
- **Important caveat:** May not apply to mobile devices
- **Confidence: Medium** - Strong logical basis but context-dependent

**Space-Efficient Visuals** *(Level 2 - Moderate)*
- **Bullet graphs** instead of gauges
  - Use length/position (more accurate) instead of angle
  - More information-dense
  - Evidence: Based on Cleveland & McGill hierarchy
  - Confidence: High
  
- **Sparklines** for trend context
  - Provide high-bandwidth trend information compactly
  - Tufte's "data-intense, design-simple" concept
  - Evidence: Design principles, limited direct testing
  - Confidence: Medium

**Executive Preferences** *(Level 3 - Weak)*
- LBI Research Institute (2014): Survey of 250 C-level executives found primary frustration was tools "too complex" and "too slow"
- Yigitbasioglu & Velcu (2012): Literature review found "ease of use" and avoiding "information overload" critical for adoption
- **Confidence: Medium** - Survey data and qualitative research, not controlled experiments

### Narrative Techniques for Executives

**Lead with "Big Idea"** *(Level 2 - Moderate)*
- Based on communication theory and rhetoric
- Analogous to "topic sentence" in writing
- Provides organizing schema that improves comprehension and recall
- **Confidence: High** - Strong theoretical basis with supporting cognitive science research

**Information Hierarchy** *(Level 1 - Strong)*
- **Primacy effect:** Items at beginning are recalled more accurately and perceived as more important
- **Nielsen Norman Group eye-tracking:** Users focus attention "above the fold" and scan in "F-shaped" pattern
- **Inverted pyramid:** Journalistic structure ensuring main point communicated even if reading stops early
- **Confidence: Very High** - Extensive empirical support

**Time Constraints** *(Level 3 - Weak)*
- **Claim:** Executives have very short attention spans
- **Evidence:** Primarily professional consensus and qualitative observations
- **Note:** Direct quantification is scarce - difficult to measure in real-world context
- **Indirect support:** Studies on managerial behavior show high volume of brief, fragmented interactions
- **Confidence: Medium** - Widely observed but not rigorously measured

### Government-Specific Practices

**Congressional Research Service (CRS)**
- **Verified source:** USAFacts testimony to House Subcommittee on Modernization (April 2023), published recommendations (October 2023)
- **Recommendations included:**
  - Modernize reports with shorter summaries emphasizing data visualizations
  - Produce and regularly update interactive dashboards
  - Publish in web-friendly, searchable formats vs. static PDFs
  - Conduct outreach and training on data literacy

**Government Accountability Office (GAO)**
- Principles embedded in "Government Auditing Standards" (Yellow Book)
- Reports must be accurate, objective, complete, convincing, and clear
- Observed practices: Clear, simple charts (bars, lines, pies) with meticulous sourcing

**Centers for Disease Control (CDC)**
- Provides specific guidance through CDC Open-Source Visualization Editor (COVE)
- "Best Practices for Data Visualization" (March 2021)
- Detailed guidance for chart types and accessibility
- Link: https://www.cdc.gov/cove/

**Implication:** Executive visualization guidance should be presented as **evidence-informed best practice**, not experimentally proven law.

---

## VI. Common Mistakes to Avoid

Based on evidence reviewed, these errors frequently occur:

### Mistake 1: Relying on color alone
- **Evidence:** WCAG SC 1.4.1 violation, excludes colorblind users (~8% of men, ~0.5% of women)
- **Fix:** Add patterns, direct labels, or redundant encoding (shape + color)

### Mistake 2: Using dual-axis charts to show correlation
- **Evidence:** Scales can be manipulated; viewers misinterpret crossover points (Isenberg et al., 2011)
- **Fix:** Use small multiples (side-by-side charts) or connected scatterplot

### Mistake 3: Ordering demographic groups to reinforce hierarchy
- **Evidence:** Urban Institute research on implicit framing effects; Xiong et al. on polarization
- **Fix:** Order alphabetically, by sample size, or by magnitude of outcome

### Mistake 4: Insufficient color contrast
- **Evidence:** WCAG SC 1.4.3 and 1.4.11 requirements
- **Fix:** Use USWDS color system (50+ grade difference) or WebAIM contrast checker

### Mistake 5: Omitting data sources and collection dates
- **Evidence:** Reduces credibility and prevents verification
- **Fix:** Always include "Source:" and "Data as of:" in chart footer

### Mistake 6: Using 3D effects for 2D data
- **Evidence:** Zacks et al. (1998) - reduces accuracy without benefit
- **Fix:** Use flat 2D charts with clear visual hierarchy

### Mistake 7: Presenting visualization without text summary
- **Evidence:** Section 508 violation, inaccessible to screen readers
- **Fix:** Provide text equivalent summarizing key findings and accessible data table

### Mistake 8: Stacked bars for comparing segments
- **Evidence:** Cleveland & McGill hierarchy; Talbot et al. (2014) experimental confirmation
- **Fix:** Use grouped bars for component comparison, lines for trends over time

### Mistake 9: Choropleths when comparison is the goal
- **Evidence:** Area bias and MAUP create misleading patterns
- **Fix:** Use tile grid maps for state-level comparisons

### Mistake 10: Generic or missing chart titles
- **Evidence:** Kong et al. (2019) - active titles improve speed and accuracy
- **Fix:** State the conclusion: "Sales Peaked in Q3" not "Sales Over Time"

---

## VII. Decision Trees for Practitioners

### Decision Tree 1: Chart Selection

**START: What is your primary goal?**

**→ Compare values across categories**
- All values positive? → **Horizontal bar chart**
- Mix of positive/negative? → **Diverging bar chart**
- Many categories? → **Dot plot** (more compact)

**→ Show change over time**
- Single series? → **Line chart**
- Multiple series (≤5)? → **Multiple lines with clear labels**
- Multiple series (>5)? → **Small multiples** (separate mini-charts)
- Need to show total and parts? → **Consider separate charts** (not stacked area)

**→ Show geographic patterns**
- Need accurate geography? → **Choropleth** (with cautions about area bias)
- Need equal comparison weight? → **Tile grid map** (for familiar geographies like U.S. states)
- Showing specific locations? → **Point map** with proportional symbols

**→ Show part-to-whole relationship**
- ≤5 categories, rough comparison OK? → **Pie chart** (acceptable)
- Need precision or >5 categories? → **Horizontal bar chart** (sorted by size)
- Show composition change over time? → **Separate bar charts** or **slope chart**

**→ Show relationship between two variables**
- Looking for correlation/patterns? → **Scatterplot**
- Want to show change over time? → **Connected scatterplot**
- Comparing two series over time? → **Small multiples**, NOT dual-axis

**→ Show performance against target**
- Single metric? → **Bullet graph**
- Multiple metrics? → **Table with bullet graphs** or **dashboard with multiple bullets**
- Need trend context? → **Sparklines in table**

---

### Decision Tree 2: Audience Adaptation

**START: Who is your primary audience?**

**→ Data/Technical Team (Analysts, Data Scientists)**
- **Purpose:** Exploration and discovery
- **Format:** Interactive dashboard with drill-down capability
- **Design approach:**
  - All data available, high information density acceptable
  - Enable filtering, brushing, linking between charts
  - Follow Shneiderman's mantra: "Overview first, zoom and filter, then details-on-demand"
  - Provide data download options
- **Chart preferences:** Can use more complex charts if they add analytical value

**→ Program Managers**
- **Purpose:** Performance monitoring and operational decisions
- **Format:** Dashboard focused on KPIs and targets
- **Design approach:**
  - Performance-focused: actual vs. target, variance from goal
  - Single-screen view of critical metrics
  - Use bullet graphs for KPI performance
  - Use sparklines for trend context
  - Traffic-light indicators acceptable if supplemented with actual values
- **Key question:** "Are we on track to meet our goals?"

**→ Executive Leadership**
- **Purpose:** Strategic oversight and high-level decision support
- **Format:** Single-screen summary leading with key takeaway
- **Design approach:**
  - Lead with "Big Idea" - one sentence stating what matters
  - Show only critical metrics (3-5 maximum)
  - Use simple, familiar charts (bar, line)
  - Active titles that state conclusions
  - Provide detailed appendix for staff follow-up
  - Assume 3-5 minutes of attention maximum
- **Key question:** "What decision needs to be made and why?"

**→ Public/Legislative Audience**
- **Purpose:** Transparency, accountability, public communication
- **Format:** Accessible, web-friendly presentation
- **Design approach:**
  - Maximum accessibility compliance (WCAG 2.1 AA minimum)
  - Apply equity lens (Urban Institute Do No Harm framework)
  - Plain language explanations
  - Transparent sourcing and limitations
  - Avoid jargon and technical terms
  - Provide context and definitions
- **Key requirements:**
  - Text alternatives for all visualizations
  - Sufficient color contrast (4.5:1 text, 3:1 graphics)
  - Do not rely on color alone
  - People-first language
  - Clear data sources and dates

---

## VIII. Practical Synthesis

Across all evidence reviewed, several conclusions are robust:

1. **Visualization design materially affects interpretation and decisions** *(High confidence)*
   - Chart choice, color, framing all influence how audiences understand data
   - Design is not neutral - choices have consequences

2. **Perceptual science provides strong but probabilistic guidance** *(Very high confidence)*
   - Position on common scale is most accurate on average
   - Individual variation exists - no universal "best" for everyone
   - Rankings describe tendencies, not absolute rules

3. **Accessibility and equity are foundational in government work** *(Very high confidence - legal requirement)*
   - Section 508 and WCAG compliance is mandatory
   - Equity considerations build trust and ensure fair communication
   - Benefits all users, not just those with disabilities

4. **Chart guidance is context-dependent; absolutes are rarely justified** *(High confidence)*
   - Purpose (analysis vs. communication) matters
   - Audience (technical vs. executive vs. public) matters
   - Task (comparison vs. trend vs. composition) matters
   - Even "bad" charts have appropriate use cases

5. **Executive communication benefits from clarity, restraint, and explicit framing** *(Medium to high confidence)*
   - Lead with conclusions, not data
   - Minimize cognitive load
   - State limitations explicitly
   - Provide layered detail (summary + appendix)

### The Principle of Evidence-Informed Flexibility

The most defensible approach for government organizations is **principled flexibility**:

- **Default to designs with the strongest evidence** - Position encodings, simple charts, accessible formats
- **Document deviations with rationale** - If using a lower-ranked chart type, explain why it's appropriate for this context
- **Align visualization choices with audience, task, and public responsibility** - One size does not fit all
- **Prioritize legal compliance** - Accessibility is non-negotiable
- **Apply equity lens** - Consider how design choices might reinforce or counter bias
- **Test with actual users** when feasible - User feedback beats assumptions

---

## References

Bateman, S., Mandryk, R. L., Gutwin, C., Genest, A., McDine, D., & Brooks, C. (2010). Useful junk? The effects of visual embellishment on comprehension and memorability of charts. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 2573–2582.

Bertin, J. (1967). *Sémiologie graphique*. Paris: Gauthier-Villars.

Borkin, M. A., Vo, A. A., Bylinskii, Z., Isola, P., Sunkavalli, S., Oliva, A., & Pfister, H. (2013). What makes a visualization memorable? *IEEE Transactions on Visualization and Computer Graphics*, 19(12), 2306–2315.

Cleveland, W. S., & McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. *Journal of the American Statistical Association*, 79(387), 531–554.

Cleveland, W. S., & McGill, R. (1987). Graphical perception: The visual decoding of quantitative information on graphical displays of data. *Journal of the Royal Statistical Society, Series A*, 150(3), 192–229.

Davis, J., Chang, R., & Dunne, C. (2022). Individual differences in graphical perception. *IEEE Transactions on Visualization and Computer Graphics*, 29(1), 1200–1210.

Heer, J., & Bostock, M. (2010). Crowdsourcing graphical perception: Using Mechanical Turk to assess visualization design. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 203–212.

Isenberg, P., Bezerianos, A., Dragicevic, P., & Fekete, J. D. (2011). A study on dual-scale data charts. *IEEE Transactions on Visualization and Computer Graphics*, 17(12), 2469–2478.

Knaflic, C. N. (2015). *Storytelling with data: A data visualization guide for business professionals*. Hoboken, NJ: Wiley.

Kong, X., Liu, Y., Kanitkar, K., & Borkin, M. A. (2019). An empirical investigation of the effects of chart titles with different levels of message. *IEEE VIS 2019 Short Papers*.

Kosara, R., & Mackinlay, J. (2013). Storytelling: The next step for visualization. *Computer*, 46(5), 44–50.

Mackinlay, J. (1986). Automating the design of graphical presentations of relational information. *ACM Transactions on Graphics*, 5(2), 110–141.

Simkin, D., & Hastie, R. (1987). An information-processing analysis of graph perception. *Journal of the American Statistical Association*, 82(398), 454–465.

Talbot, J., Setlur, V., & Anand, A. (2014). Four experiments on the perception of bar charts. *IEEE Transactions on Visualization and Computer Graphics*, 20(12), 2152–2160.

Tufte, E. R. (2001). *The visual display of quantitative information* (2nd ed.). Cheshire, CT: Graphics Press.

Urban Institute. (2021). *Do No Harm Guide: Applying equity awareness in data visualization*. Retrieved from https://www.urban.org/

USAFacts. (2023). *Recommendations for modernizing Congressional Research Service reports*. Testimony to House Subcommittee on Modernization, April 2023; Published October 2023.

Xiong, C., Setlur, V., Bach, B., Koh, E., Lin, K., & Franconeri, S. (2023). Visual arrangements of bar charts influence comparisons in viewer takeaways. *IEEE Transactions on Visualization and Computer Graphics*, 29(1), 1058–1068.

Yigitbasioglu, O. M., & Velcu, O. (2012). A review of dashboards in performance management: Implications for design and research. *International Journal of Accounting Information Systems*, 13(1), 41–59.

Zacks, J., Levy, E., Tversky, B., & Schiano, D. J. (1998). Reading bar graphs: Effects of extraneous depth cues and graphical context. *Journal of Experimental Psychology: Applied*, 4(2), 119–138.

Zubeida, K., Wang, Y., Chen, F., & Yu, B. (2021). Data stories versus data charts: How different types of visual information affect persuasion and empathy. *Frontiers in Psychology*, 12, 616298.

---

## Appendix: Accessibility and Government Standards

### WCAG 2.1/2.2 Success Criteria Relevant to Data Visualization

**SC 1.1.1 Non-text Content (Level A)**
- All non-text content must have a text alternative that serves the equivalent purpose
- For charts: Provide alt text AND accessible data table

**SC 1.4.1 Use of Color (Level A)**
- Color must not be the only visual means of conveying information
- Add patterns, labels, or icons in addition to color

**SC 1.4.3 Contrast (Minimum) (Level AA)**
- Text: 4.5:1 for normal text, 3:1 for large text
- Verify with tools like WebAIM Contrast Checker

**SC 1.4.11 Non-text Contrast (Level AA)**
- Graphical objects: 3:1 minimum
- Includes chart bars, lines, data point markers

**SC 2.1.1 Keyboard (Level A)**
- All functionality must be operable through keyboard interface
- Critical for interactive dashboards and filters

**SC 4.1.2 Name, Role, Value (Level A)**
- User interface components must have programmatically determinable names and roles
- Use semantic HTML and ARIA labels appropriately

### USWDS Color Accessibility Resources

- Color tokens use numeric grades (0-100)
- Difference of 50+ ensures WCAG AA compliance (4.5:1)
- Color contrast tool: https://designsystem.digital.gov/utilities/color/

### Section 508 Refresh (2017)

Incorporated WCAG 2.0 Level AA by reference. Key implications:
- Federal agencies must comply with all WCAG 2.0 AA success criteria
- Applies to all electronic and information technology
- Visualizations in reports, dashboards, and presentations included

### Testing Tools

**Automated:**
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- WAVE Browser Extension: https://wave.webaim.org/
- axe DevTools: https://www.deque.com/axe/

**Manual:**
- Screen reader testing (JAWS, NVDA, VoiceOver)
- Keyboard-only navigation testing
- Color blindness simulation (Color Oracle, Coblis)

---

*Document Version: 1.0*  
*Last Updated: February 2026*  
*For Internal Reference and Training*