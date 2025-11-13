import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("ipl_score_predictor1.joblib")

st.set_page_config(page_title="IPL Final Score Predictor", page_icon="🏏")

st.title("🏏 IPL Final Score Predictor")
st.markdown("### Predict the final score of an IPL innings using XGBoost Model")

# Input fields
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting Team", [
        "Chennai Super Kings", "Delhi Capitals", "Kolkata Knight Riders",
        "Mumbai Indians", "Punjab Kings", "Rajasthan Royals",
        "Royal Challengers Bangalore", "Sunrisers Hyderabad", "Lucknow Super Giants",
        "Gujarat Titans"
    ])
    bowling_team = st.selectbox("Select Bowling Team", [
        "Chennai Super Kings", "Delhi Capitals", "Kolkata Knight Riders",
        "Mumbai Indians", "Punjab Kings", "Rajasthan Royals",
        "Royal Challengers Bangalore", "Sunrisers Hyderabad", "Lucknow Super Giants",
        "Gujarat Titans"
    ])
    city = st.selectbox("Match City", [
        "Mumbai", "Delhi", "Chennai", "Kolkata", "Bangalore", "Hyderabad",
        "Jaipur", "Ahmedabad", "Pune", "Unknown"
    ])

with col2:
    current_score = st.number_input("Current Score", min_value=0, max_value=300, value=75)
    wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, value=3)
    current_over = st.number_input("Current Over", min_value=0.0, max_value=20.0, value=10.0, step=0.1)
    last_5_runs = st.number_input("Runs Scored in Last 5 Overs", min_value=0, max_value=100, value=40)

if st.button("Predict Final Score"):
    # Encode categorical variables (simple manual encoding)
    team_dict = {
        "Chennai Super Kings": 0, "Delhi Capitals": 1, "Kolkata Knight Riders": 2,
        "Mumbai Indians": 3, "Punjab Kings": 4, "Rajasthan Royals": 5,
        "Royal Challengers Bangalore": 6, "Sunrisers Hyderabad": 7,
        "Lucknow Super Giants": 8, "Gujarat Titans": 9
    }
    city_dict = {
        "Mumbai": 0, "Delhi": 1, "Chennai": 2, "Kolkata": 3, "Bangalore": 4,
        "Hyderabad": 5, "Jaipur": 6, "Ahmedabad": 7, "Pune": 8, "Unknown": 9
    }

    input_data = pd.DataFrame([{
        "current_over": current_over,
        "current_score": current_score,
        "wickets": wickets,
        "city": city_dict[city],
        "last_5_runs": last_5_runs,
        "bowling_team": team_dict[bowling_team],
        "batting_team": team_dict[batting_team]
    }])

    predicted_score = model.predict(input_data)[0]
    st.success(f"🏆 **Predicted Final Score:** {round(predicted_score)} runs")
