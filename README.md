## ⚽ EPL 2025/26 Tactical Performance Analysis Dashboard
## Objective

The objective of this project is to analyze the tactical and statistical performance of Premier League teams during the 2025/26 season using advanced football analytics metrics such as:

Expected Goals (xG)
Expected Goals Against (xGA)
Expected Points (xPTS)
Finishing Efficiency
Defensive Efficiency

This dashboard aims to move beyond traditional league tables by identifying:

Overperforming and underperforming teams
Tactical team identities
Attacking and defensive efficiency patterns
Structural strengths and weaknesses across the league

The project simulates a modern football analytics/scouting environment similar to workflows used by professional clubs, analysts, and recruitment departments.

## Data Used

The dataset contains team-level EPL performance metrics for the 2025/26 season.

Core Variables
Variable	Description
Position	League standing
Team	Club name
Matches Played	Total games played
Wins / Draws / Losses	Match outcomes
Goals Scored	Total goals scored
Goals Conceded	Total goals allowed
Points	Actual league points
Expected Goals (xG)	Quality of chances created
Expected Goals Against (xGA)	Quality of chances conceded
Expected Points (xPTS)	Points expected from underlying performance
## Key Findings
1. xG strongly correlates with league success

A strong positive correlation (r ≈ 0.82) was found between xG and league points.

Insight

Teams that consistently create higher-quality chances tend to perform better over the season.

2. Arsenal and Manchester City are the most balanced elite teams

Both teams combine:

High attacking output (high xG)
Strong defensive control (low xGA)
Stable performance metrics
Insight

Their success is driven by sustainable tactical structure rather than short-term variance.

3. Chelsea significantly underperformed offensively

Chelsea generated one of the highest xG totals in the league but failed to convert chances efficiently.

Insight

This suggests:

Poor finishing efficiency
Potential striker inefficiency
Final-third decision-making issues
4. Sunderland and Aston Villa overperformed relative to xPTS

Both clubs earned significantly more points than expected.

Insight

Results may have been influenced by:

High conversion efficiency
Goalkeeping performance
Success in low-margin matches
5. Wolves and Leeds showed structural weakness

These teams combined:

Low attacking production
Weak defensive metrics
Negative performance gaps
Insight

Underlying metrics suggest relegation-risk profiles.

## Visuals Included
live demo: https://epl-2025-26-tactical-performance-analysis-dashboard-hhrddhu5sp.streamlit.app/

The dashboard contains several interactive Plotly visualizations:

⚽ Tactical Identity Map
xG vs xGA scatter plot
Identifies:
Elite teams
Defensive teams
Attack-heavy teams
Structurally weak teams
🔥 Finishing Efficiency Ranking

Measures:

Goals scored relative to xG

Used to identify:

Clinical attacking teams
Wasteful attacking teams
🧱 Defensive Efficiency Ranking

Measures:

Goals conceded relative to xGA

Used to identify:

Elite defensive structures
Defensively unstable teams
📊 xG vs Points Scatter Plot

Analyzes the relationship between:

Chance creation
League success
📈 Performance Gap Analysis

Compares:

Actual Points
Expected Points (xPTS)

Used to detect:

Overperformers
Underperformers
Regression-risk teams
## Tactical Implications
Elite Teams

Arsenal and Manchester City demonstrate that sustainable league success is driven by:

High chance creation
Strong defensive suppression
Tactical balance
Overperforming Teams

Teams such as Aston Villa and Sunderland may face future regression if underlying metrics do not improve.

Underperforming Teams

Chelsea’s data suggests tactical attacking inefficiency rather than defensive weakness.

This indicates:

Finishing problems
Potential recruitment gaps in attacking roles
Relegation-Risk Profiles

Wolves and Leeds exhibit structural issues on both sides of the ball:

Low xG production
High xGA exposure
## Actionable Recommendations
For Elite Clubs

Maintain tactical stability and squad depth to preserve balanced xG/xGA profiles.

For Chelsea-Type Teams

Focus on:

Finishing quality
Striker recruitment
Shot selection optimization
For Overperforming Clubs

Improve underlying metrics rather than relying on:

Variance
Finishing streaks
Narrow victories
For Structurally Weak Teams

Priority should be:

Defensive organization
Chance suppression
Transition control
Improved attacking chance creation
## Tools & Technologies
Python
Pandas
Streamlit
Plotly
Football Analytics Metrics (xG, xGA, xPTS)
## Project Type

Football Analytics | Performance Analysis | Tactical Scouting | Sports Data Science
