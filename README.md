# 🎓 Student Academic Risk Predictor

An end-to-end Machine Learning web application that evaluates student demographic, lifestyle, and mental well-being factors to predict academic failure risk in real-time. Built with a **FastAPI** backend and an interactive **CSS Grid Dashboard** featuring dynamic AI academic recommendations.

---

## 🚀 Live Demo

- **Live Web App:** [https://academic-risk-predictor.onrender.com](https://academic-risk-predictor.onrender.com)
- **API Documentation (Swagger UI):** [https://academic-risk-predictor.onrender.com/docs](https://academic-risk-predictor.onrender.com/docs)

---

## ✨ Features

- **Real-Time Risk Scoring:** Machine Learning model trained on student lifestyle and performance parameters.
- **Dynamic Dual-Column UI:** Responsive grid dashboard featuring an input panel alongside a live analytical summary.
- **Speedometer Risk Gauge:** Visual probability score rendering with color-coded risk indicators (Low vs. High Risk).
- **Tailored AI Guidelines:** Actionable academic recommendations generated based on individual student risk profiles.
- **RESTful FastAPI Architecture:** High-performance, fully validated API endpoints powered by Pydantic schemas.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, FastAPI, Uvicorn, Pydantic
- **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
- **Frontend:** HTML5, CSS3 (CSS Grid & Flexbox), Vanilla JavaScript (Fetch API)
- **Deployment:** Railway, Git/GitHub

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
