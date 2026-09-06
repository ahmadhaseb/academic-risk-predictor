# 🎓 Student Academic Risk Predictor

An end-to-end Machine Learning web application that evaluates student demographic, lifestyle, and mental well-being factors to predict academic failure risk in real-time. Built with a **FastAPI** backend, deployed on **Vercel**, and featuring an interactive **CSS Grid Dashboard** with dynamic AI academic recommendations.

---

## 🚀 Live Demo

- **Live Web App:** [https://academicriskpredictor.vercel.app](https://academicriskpredictor.vercel.app)
- **API Documentation (Swagger UI):** [https://academicriskpredictor.vercel.app/docs](https://academicriskpredictor.vercel.app/docs)

---

## ✨ Features

- **Real-Time Risk Scoring:** Machine Learning model trained on student lifestyle and performance parameters.
- **Dynamic Dual-Column UI:** Responsive grid dashboard featuring an input panel alongside a live analytical summary.
- **Speedometer Risk Gauge:** Visual probability score rendering with color-coded risk indicators (Low vs. High Risk).
- **Tailored AI Guidelines:** Actionable academic recommendations generated based on individual student risk profiles.
- **RESTful FastAPI Architecture:** High-performance, fully validated API endpoints powered by Pydantic schemas.
- **Serverless Vercel Deployment:** Fast, zero-card free hosting setup configured via serverless routes.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, FastAPI, Uvicorn, Pydantic
- **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
- **Frontend:** HTML5, CSS3 (CSS Grid & Flexbox), Vanilla JavaScript (Fetch API)
- **Hosting & Deployment:** Vercel (Serverless Functions), Git/GitHub

---

## 📊 Dataset Features & Parameters

| Parameter | Type | Description / Range |
| :--- | :--- | :--- |
| `Age` | Numerical | Student age in years |
| `Gender` | Categorical | Male, Female, Non-Binary |
| `Education_Level` | Categorical | High School, College, University |
| `Daily_Social_Media_Hours` | Numerical | Daily social media consumption (Hours) |
| `Daily_AI_Tool_Usage_Hours` | Numerical | Daily academic AI usage (Hours) |
| `Sleep_Hours` | Numerical | Average nightly sleep (Hours) |
| `Physical_Activity_Hours` | Numerical | Weekly/daily physical exercise (Hours) |
| `Mental_Health_Score` | Numerical | Self-reported rating (1 to 10) |
| `Physical_Health_Score` | Numerical | Self-reported rating (1 to 10) |
| `Social_Isolation_Score` | Numerical | Self-reported rating (1 to 10) |
| `Burnout_Level` | Categorical | Low, Moderate, High, Severe |
| `Academic_Performance_Score` | Numerical | Academic evaluation rating (1 to 10) |

---

## 💻 Local Setup & Installation

Follow these steps to run the application locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
2. Create and Activate Virtual Environment  
Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Launch Application
Bash
uvicorn app:app --reload
Open http://127.0.0.1:8000 in your web browser to access the dashboard.

📡 API Endpoint Overview
Predict Academic Risk
Endpoint: /predict

Method: POST

Content-Type: application/json

Request Body Example:
JSON
{
  "Age": 20,
  "Gender": "Male",
  "Education_Level": "University",
  "Daily_Social_Media_Hours": 3.5,
  "Daily_AI_Tool_Usage_Hours": 2.0,
  "Sleep_Hours": 7.0,
  "Physical_Activity_Hours": 1.0,
  "Mental_Health_Score": 6.0,
  "Physical_Health_Score": 7.0,
  "Social_Isolation_Score": 4.0,
  "Burnout_Level": "Moderate",
  "Academic_Performance_Score": 6.5
}
Response Example:
JSON
{
  "academic_failure_risk": 0,
  "risk_probability": 2.0,
  "status": "Safe Academic Standing"
}
📁 Project Directory Structure
Plaintext
├── static/
│   ├── index.html       # Single-page dashboard interface
│   ├── style.css        # Dashboard grid styles and layout
│   └── script.js        # Dynamic API request & UI handlers
├── app.py               # Main FastAPI server script
├── vercel.json          # Vercel serverless build & routing configuration
├── model.joblib         # Serialized Machine Learning model
├── requirements.txt     # Python dependencies list
└── README.md            # Project documentation

---

### Terminal Commands (Git Update):
```bash
git add README.md
git commit -m "Update README with Vercel deployment link"
git push origin main
