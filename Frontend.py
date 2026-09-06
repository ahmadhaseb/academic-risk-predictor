import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

#page setup for wide dashboard
st.set_page_config(page_title="Student Academic Risk Predictor",layout="wide")

#Custom CSS for Dark background
st.markdown("""
    <style>
    .main{background-color:#12151C; color:#FFFFFF;}
    .stApp{background-color:#12151C;}
    div[data-testid="stSidebar"]{ background-color: #1E222D; }
    .css-1r6594q, .css-vhjld6 { color: white; }
    .result-card-high {
        background-color: #2D1A1E;
        border: 1px solid #FF4B4B;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    .result-card-safe {
        background-color: #1A2D23;
        border: 1px solid #00CC96;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    </style>
""",unsafe_allow_html=True)

st.title("📊 Student Academic Risk Predictor")
#Column Dashboard Layout
col_input,col_display = st.columns([1,1.3])
with col_input:
    st.subheader("ENTER STUDENT DETAILS")
    with st.form("student_form"):
        gender = st.selectbox("GENDER",["Male","Female","Non-Binary"])
        age  = st.number_input("AGE",15,30,19)
        education_level = st.selectbox("EDUCATION LEVEL", ["High School", "College", "University"])
        daily_social = st.number_input("DAILY SOCIAL MEDIA HOURS", 0.0, 15.0, 6.5)
        daily_ai = st.number_input("DAILY AI USAGE", 0.0, 15.0, 2.0)
        sleep = st.number_input("SLEEP HOURS", 0.0, 12.0, 5.5)
        mental_health = st.number_input("MENTAL HEALTH SCORE (0-100)", 0.0, 100.0, 55.0)
        physical_activity = st.number_input("PHYSICAL ACTIVITY (HOURS)", 0.0, 10.0, 1.0)
        physical_health = st.number_input("PHYSICAL HEALTH SCORE", 0.0, 100.0, 60.0)
        isolation = st.number_input("SOCIAL ISOLATION SCORE", 0.0, 10.0, 5.0)
        burnout = st.selectbox("BURNOUT LEVEL", ["Low", "Moderate", "High", "Severe"])
        academic_score = st.number_input("ACADEMIC PERFORMANCE SCORE", 0.0, 100.0, 45.0)


        submit_btn = st.form_submit_button("ANALYZE RISK",type="primary")

    with col_display:
        if submit_btn:
            payload = {
                "Age": age, "Gender": gender, "Education_Level": education_level,
                "Daily_Social_Media_Hours": daily_social, "Daily_AI_Tool_Usage_Hours": daily_ai,
                "Sleep_Hours": sleep, "Physical_Activity_Hours": physical_activity,
                "Mental_Health_Score": mental_health, "Physical_Health_Score": physical_health,
                "Social_Isolation_Score": isolation, "Burnout_Level": burnout,
                "Academic_Performance_Score": academic_score
            }
            try:
                res = requests.post("http://127.0.0.1:8000/predict", json=payload).json()
                risk_score = res["risk_probability"]
                is_high_risk = res["academic_failure_risk"] == 1

                #Guage Meter Chart
                st.subheader("ANALYSIS RESULT")
                fig_gauge = go.Figure(go.Indicator(
                    mode  = "gauge+number",
                    value = risk_score,
                    number = {"suffix":"%"},
                    gauge = {
                        'axis': {'range' : [0,100]},
                        'bar' : {'color' : "#FF4B4B" if is_high_risk else "#00CC96" },
                        'steps' : [
                            {'range' : [0,40], 'color': "#2ECC71"},
                            {'range': [40, 70], 'color': "#F39C12"},
                            {'range': [70, 100], 'color': "#E74C3C"}
                        ]
                    }
                ))
                fig_gauge.update_layout(height = 250,margin = dict(l=20, r=20,b=20),paper_bgcolor = "rgb(0,0,0)",font = {'color' :"white"})
                st.plotly_chart(fig_gauge,use_container_width=True)

                #Risk Result Box
                if is_high_risk:
                    st.markdown(f'<div class = "result-card-high"><h4>HIGH RISK (Score : {risk_score}%)</h4><p>Advisory: High burnout level and social isolation detected. Recommended support: Counseling Services.</p></div>', unsafe_allow_html=True)
                else:

                    st.markdown(f'<div class="result-card-safe"><h4>SAFE / LOW RISK (Score: {risk_score}%)</h4><p>Advisory: Student parameters are in a safe zone.</p></div>',unsafe_allow_html=True)

                    # 2. Feature Importance Graph
                    st.subheader("Feature Importance Contribution")
                    sample_features = pd.DataFrame({
                        'Feature': ['Academic Performance', 'Gender', 'Burnout_Level', 'Social Media Hours',
                                    'Sleep Hours'],
                        'Importance': [45, 30, 15, 7, 3]
                    })
                    fig_bar = go.Figure(go.Bar(
                        x=sample_features['Importance'],
                        y=sample_features['Feature'],
                        orientation='h',
                        marker=dict(color=['#00CC96', '#00CC96', '#FF4B4B', '#FF851B', '#FF851B'])
                    ))
                    fig_bar.update_layout(height=230, margin=dict(l=20, r=20, t=20, b=20),
                                          paper_bgcolor="rgb(0,0,0,0)", plot_bgcolor="rgb(0,0,0,0)",
                                          font={'color': "white"})
                    st.plotly_chart(fig_bar, use_container_width=True)

            except Exception as e :
                st.error(f"Could not connect to FastAPI server.Make sure Backend.py is running. Error: {e}")

