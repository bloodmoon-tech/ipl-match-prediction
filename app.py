import streamlit as st
import pandas as pd

from backend.model import load_dataset, predict_match, prepare_dataset

st.set_page_config(page_title="IPL Match Predictor", page_icon="🏏", layout="wide")

st.markdown(
    """
    <style>
    :root { --ink: #17212b; --muted: #65727e; --paper: #f4f1ea; --accent: #e85d3f; --accent-dark: #b43d2b; --line: #dedbd3; --mint: #dce9df; }
    .stApp { background: radial-gradient(circle at 90% 0%, #f8d7b5 0, transparent 25%), linear-gradient(135deg, #f4f1ea 0%, #f8f6f1 55%, #e9efe9 100%); color: var(--ink); }
    .block-container { max-width: 1180px; padding-top: 2.5rem; padding-bottom: 3rem; }
    .hero { border-bottom: 1px solid rgba(23, 33, 43, 0.14); padding-bottom: 1.8rem; margin-bottom: 1.8rem; }
    .eyebrow { color: var(--accent-dark); font-size: 0.72rem; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 0.65rem; }
    .hero-title { color: var(--ink); font-size: clamp(2.5rem, 5vw, 4.5rem); letter-spacing: -0.03em; line-height: 0.98; font-weight: 850; margin: 0; max-width: 760px; }
    .hero-copy { color: var(--muted); font-size: 1rem; line-height: 1.6; max-width: 620px; margin: 1rem 0 0; }
    .section-kicker { color: var(--muted); font-size: 0.72rem; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; margin: 0 0 0.7rem; }
    .panel { background: rgba(255, 255, 255, 0.72); border: 1px solid rgba(222, 219, 211, 0.95); border-radius: 10px; padding: 1.35rem 1.5rem; box-shadow: 0 14px 34px rgba(37, 40, 42, 0.07); height: 100%; box-sizing: border-box; }
    .panel-title { color: var(--ink); font-weight: 850; font-size: 1.16rem; margin-bottom: 0.25rem; }
    .panel-note { color: var(--muted); font-size: 0.86rem; line-height: 1.45; margin-bottom: 1.1rem; }
    .stats-strip { background: var(--ink); border-radius: 10px; padding: 0.9rem 1.25rem; margin-bottom: 2rem; }
    .stats-strip [data-testid="stMetricLabel"] { color: #aebbc1; }
    .stats-strip [data-testid="stMetricValue"] { color: #ffffff; font-size: 1.55rem; }
    .result-card { background: var(--ink); border-radius: 10px; padding: 1.7rem; color: white; min-height: 300px; display: flex; flex-direction: column; justify-content: center; box-sizing: border-box; box-shadow: 0 16px 36px rgba(23, 33, 43, 0.18); }
    .result-card.ready { background: linear-gradient(145deg, #233847, #17212b); }
    .result-label { color: #f4b29f; font-size: 0.72rem; letter-spacing: 0.13em; text-transform: uppercase; font-weight: 800; }
    .result-winner { font-size: clamp(1.75rem, 3vw, 2.35rem); line-height: 1.05; font-weight: 850; margin: 0.6rem 0; }
    .result-status { color: #cbd2d7; margin-bottom: 1.35rem; }
    .result-detail { color: #dfe5e8; font-size: 0.9rem; margin: 0.25rem 0; }
    .confidence { border-top: 1px solid rgba(255,255,255,0.18); margin-top: 1.25rem; padding-top: 1rem; color: #ffffff; font-size: 1.3rem; font-weight: 800; }
    .confidence span { color: #aebbc1; display: block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.11em; text-transform: uppercase; }
    .chart-title { color: var(--ink); font-weight: 850; margin: 0 0 0.25rem; }
    .chart-note { color: var(--muted); font-size: 0.84rem; margin-bottom: 1rem; }
    .bar-label { display: flex; justify-content: space-between; color: var(--ink); font-size: 0.84rem; margin: 0.55rem 0 0.25rem; }
    .bar-track { height: 9px; background: #e9e6df; border-radius: 3px; overflow: hidden; }
    .bar-fill { height: 100%; background: var(--accent); border-radius: 3px; }
    .bar-fill-dark { height: 100%; background: var(--ink); border-radius: 3px; }
    [data-testid="stMetricValue"] { color: var(--accent); font-weight: 850; }
    [data-testid="stSelectbox"] label, [data-testid="stNumberInput"] label { color: var(--ink); font-weight: 700; font-size: 0.82rem; }
    [data-baseweb="select"] > div, [data-testid="stNumberInput"] input { background: rgba(255,255,255,0.82); border-color: var(--line); border-radius: 6px; }
    div.stButton > button { background: var(--accent); color: white; border: 0; border-radius: 6px; font-weight: 850; padding: 0.72rem 1.4rem; margin-top: 0.55rem; }
    div.stButton > button:hover { background: var(--accent-dark); color: white; }
    @media (max-width: 700px) { .block-container { padding-top: 1.5rem; } .hero { padding-bottom: 1.3rem; } .panel { padding: 1.1rem; } }
    </style>
    """,
    unsafe_allow_html=True,
)

teams = [
    "Mumbai Indians",
    "Chennai Super Kings",
    "Royal Challengers Bengaluru",
    "Kolkata Knight Riders",
    "Sunrisers Hyderabad",
    "Punjab Kings",
    "Rajasthan Royals",
    "Delhi Capitals",
]

cities = [
    "Mumbai",
    "Chennai",
    "Bangalore",
    "Kolkata",
    "Hyderabad",
    "Jaipur",
    "Delhi",
    "Ahmedabad",
    "Lucknow",
]

st.markdown('<div class="hero"><div class="eyebrow">IPL 2008-2026 | Match intelligence</div><h1 class="hero-title">Read the match before the first ball.</h1><p class="hero-copy">Build a match scenario and see which side the historical patterns favour. Toss choice, venue and target pressure all matter.</p></div>', unsafe_allow_html=True)


@st.cache_data
def get_dashboard_stats():
    raw_df = load_dataset()
    prepared_df = prepare_dataset(raw_df)
    completed_matches = len(prepared_df)
    chase_win_rate = prepared_df["chase_won"].mean() * 100
    average_target = prepared_df["target"].mean()
    outcome_chart = pd.DataFrame(
        {
            "Outcome": ["Chasing team", "Batting first team"],
            "Matches": [
                int(prepared_df["chase_won"].sum()),
                int((prepared_df["chase_won"] == 0).sum()),
            ],
        }
    ).set_index("Outcome")
    venue_chart = (
        raw_df["city"].dropna().value_counts().head(6).sort_values()
        if "city" in raw_df.columns
        else pd.Series(dtype="int64")
    )
    return completed_matches, chase_win_rate, average_target, outcome_chart, venue_chart


completed_matches, chase_win_rate, average_target, outcome_chart, venue_chart = get_dashboard_stats()
st.markdown('<div class="stats-strip">', unsafe_allow_html=True)
metric_one, metric_two, metric_three = st.columns(3)
metric_one.metric("Completed matches", f"{completed_matches:,}")
metric_two.metric("Chases won", f"{chase_win_rate:.1f}%")
metric_three.metric("Average target", f"{average_target:.0f}")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-kicker">The data behind the forecast</div>', unsafe_allow_html=True)
chart_left, chart_right = st.columns(2, gap="large")
with chart_left:
    st.markdown('<div class="panel"><div class="chart-title">Match outcomes</div><div class="chart-note">Prepared training data</div>', unsafe_allow_html=True)
    outcome_max = max(int(outcome_chart["Matches"].max()), 1)
    outcome_rows = []
    for outcome, row in outcome_chart.iterrows():
        width = int(row["Matches"] / outcome_max * 100)
        outcome_rows.append(
            f'<div class="bar-label"><span>{outcome}</span><strong>{int(row["Matches"]):,}</strong></div>'
            f'<div class="bar-track"><div class="bar-fill" style="width:{width}%"></div></div>'
        )
    st.markdown("".join(outcome_rows) + "</div>", unsafe_allow_html=True)
with chart_right:
    st.markdown('<div class="panel"><div class="chart-title">Top match cities</div><div class="chart-note">Most represented locations in the source dataset</div>', unsafe_allow_html=True)
    venue_max = max(int(venue_chart.max()), 1) if not venue_chart.empty else 1
    venue_rows = []
    for city_name, match_count in venue_chart.items():
        width = int(match_count / venue_max * 100)
        venue_rows.append(
            f'<div class="bar-label"><span>{city_name}</span><strong>{int(match_count):,}</strong></div>'
            f'<div class="bar-track"><div class="bar-fill-dark" style="width:{width}%"></div></div>'
        )
    st.markdown("".join(venue_rows) + "</div>", unsafe_allow_html=True)

left, right = st.columns([1.15, 0.85], gap="large")

with left:
    st.markdown('<div class="panel"><div class="panel-title">Set the match conditions</div><div class="panel-note">Choose the teams, venue and toss outcome to create a scenario.</div>', unsafe_allow_html=True)
    team1 = st.selectbox("Team 1", teams)
    team2 = st.selectbox("Team 2", [t for t in teams if t != team1])
    city = st.selectbox("City", cities)
    toss_winner = st.selectbox("Toss winner", [team1, team2])
    toss_decision = st.selectbox("Toss decision", ["bat", "field"])
    target = st.number_input("Target score", min_value=100, max_value=260, value=170, step=1)
    predict_clicked = st.button("Predict match", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if predict_clicked:
        result = predict_match(team1, team2, city, toss_winner, toss_decision, int(target))
        st.markdown(
            f'''<div class="result-card">
                <div class="result-label">Model forecast</div>
                <div class="result-winner">{result['winner']}</div>
                <div class="result-status">{result['status']}</div>
                <div class="result-detail">Batting first: {result['bat_first']}</div>
                <div class="result-detail">Chasing: {result['bat_second']}</div>
                <div class="confidence"><span>Model confidence</span>{result['confidence']}%</div>
            </div>''',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '''<div class="result-card ready">
                <div class="result-label">Ready for a forecast</div>
                <div class="result-winner">Set the match conditions.</div>
                <div class="result-status">Your prediction will appear here after you submit the form.</div>
                <div class="confidence"><span>What you will get</span>Winner, batting order and confidence</div>
            </div>''',
            unsafe_allow_html=True,
        )
