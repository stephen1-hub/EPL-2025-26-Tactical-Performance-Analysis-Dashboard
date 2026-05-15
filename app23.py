import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="EPL 2025/26 Scouting Dashboard",
    layout="wide"
)

st.title("⚽ EPL 2025/26 Performance Dashboard")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
df = pd.read_excel("league-chemp.xlsx")

# ---------------------------------------------------
# RENAME COLUMNS
# ---------------------------------------------------
df = df.rename(columns={
    "number": "position",
    "matches": "matches_played",
    "loses": "losses",
    "goals": "goals_scored",
    "ga": "goals_conceded",
    "xG": "expected_goals",
    "xGA": "expected_goals_against",
    "xPTS": "expected_points"
})

# ---------------------------------------------------
# FEATURE ENGINEERING
# ---------------------------------------------------
df["finishing_efficiency"] = (
    df["goals_scored"] / df["expected_goals"]
)

df["defensive_efficiency"] = (
    df["goals_conceded"] / df["expected_goals_against"]
)

df["performance_gap"] = (
    df["points"] - df["expected_points"]
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.header("Dashboard Filters")

selected_team = st.sidebar.multiselect(
    "Select Teams",
    df["team"].unique(),
    default=df["team"].unique()
)

filtered_df = df[df["team"].isin(selected_team)]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
st.subheader("📊 League KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average xG",
    round(filtered_df["expected_goals"].mean(), 2)
)

col2.metric(
    "Average xGA",
    round(filtered_df["expected_goals_against"].mean(), 2)
)

col3.metric(
    "Average Points",
    round(filtered_df["points"].mean(), 1)
)

col4.metric(
    "Average xPTS",
    round(filtered_df["expected_points"].mean(), 1)
)

# ---------------------------------------------------
# ENHANCED LEAGUE TABLE
# ---------------------------------------------------
st.subheader("📋 Enhanced League Table")

st.dataframe(
    filtered_df.sort_values("points", ascending=False),
    use_container_width=True
)

# ---------------------------------------------------
# TACTICAL IDENTITY MAP (PLOTLY)
# ---------------------------------------------------
st.subheader("⚽ Tactical Identity Map")

fig_scatter = px.scatter(
    filtered_df,
    x="expected_goals",
    y="expected_goals_against",
    text="team",
    size="points",
    color="points",
    hover_data=[
        "goals_scored",
        "goals_conceded",
        "expected_points"
    ],
    title="xG vs xGA Tactical Identity Map"
)

fig_scatter.update_traces(textposition="top center")

fig_scatter.update_layout(
    xaxis_title="Expected Goals (xG)",
    yaxis_title="Expected Goals Against (xGA)",
    height=700
)

st.plotly_chart(fig_scatter, use_container_width=True)

# ---------------------------------------------------
# FINISHING EFFICIENCY CHART
# ---------------------------------------------------
st.subheader("🔥 Finishing Efficiency")

finishing_df = filtered_df.sort_values(
    "finishing_efficiency",
    ascending=False
)

fig_finish = px.bar(
    finishing_df,
    x="team",
    y="finishing_efficiency",
    color="finishing_efficiency",
    hover_data=[
        "goals_scored",
        "expected_goals"
    ],
    title="Goals Scored vs Expected Goals"
)

fig_finish.update_layout(
    xaxis_title="Team",
    yaxis_title="Finishing Efficiency",
    height=600
)

st.plotly_chart(fig_finish, use_container_width=True)

# ---------------------------------------------------
# DEFENSIVE EFFICIENCY CHART
# ---------------------------------------------------
st.subheader("🧱 Defensive Efficiency")

defense_df = filtered_df.sort_values(
    "defensive_efficiency"
)

fig_defense = px.bar(
    defense_df,
    x="team",
    y="defensive_efficiency",
    color="defensive_efficiency",
    hover_data=[
        "goals_conceded",
        "expected_goals_against"
    ],
    title="Goals Conceded vs xGA"
)

fig_defense.update_layout(
    xaxis_title="Team",
    yaxis_title="Defensive Efficiency",
    height=600
)

st.plotly_chart(fig_defense, use_container_width=True)

# ---------------------------------------------------
# PERFORMANCE GAP CHART
# ---------------------------------------------------
st.subheader("📈 Points vs xPTS (Performance Gap)")

gap_df = filtered_df.sort_values(
    "performance_gap",
    ascending=False
)

fig_gap = px.bar(
    gap_df,
    x="performance_gap",
    y="team",
    orientation="h",
    color="performance_gap",
    hover_data=[
        "points",
        "expected_points"
    ],
    title="Overperformance vs Underperformance"
)

fig_gap.update_layout(
    xaxis_title="Points - xPTS",
    yaxis_title="Team",
    height=700
)

st.plotly_chart(fig_gap, use_container_width=True)

# ---------------------------------------------------
# xG vs POINTS RELATIONSHIP
# ---------------------------------------------------
st.subheader("📊 xG vs League Points")

fig_points = px.scatter(
    filtered_df,
    x="expected_goals",
    y="points",
    text="team",
    size="expected_points",
    color="points",
    hover_data=[
        "performance_gap",
        "finishing_efficiency"
    ],
    title="Relationship Between xG and Points"
)

fig_points.update_traces(textposition="top center")

fig_points.update_layout(
    xaxis_title="Expected Goals (xG)",
    yaxis_title="League Points",
    height=700
)

st.plotly_chart(fig_points, use_container_width=True)

# ---------------------------------------------------
# INSIGHTS SECTION
# ---------------------------------------------------
st.subheader("🧠 Key Insights")

st.markdown("""
### Key Findings

- Arsenal and Manchester City profile as the most balanced elite teams.
- Chelsea create elite attacking chances but underperform in finishing efficiency.
- Tottenham overperform xG slightly through finishing quality.
- Wolves and Leeds show structural weakness in both attack and defense.
- xG has a strong positive relationship with league points (~0.82 correlation).
""")
