console.log("Script loaded successfully!");

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("predictionForm");

    if (!form) {
        console.error("Form element 'predictionForm' missing from HTML!");
        return;
    }

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        console.log("Form submit event triggered!");

        const resultDiv = document.getElementById("result");
        resultDiv.style.display = "block";
        resultDiv.className = "";
        resultDiv.innerHTML = "<p style='color: #38bdf8; text-align: center; margin-top: 20px;'>Calculating Risk Metrics & Summary...</p>";

        const payload = {
            Age: parseFloat(document.getElementById("Age")?.value) || 20,
            Gender: document.getElementById("Gender")?.value || "Male",
            Education_Level: document.getElementById("Education_Level")?.value || "University",
            Daily_Social_Media_Hours: parseFloat(document.getElementById("Daily_Social_Media_Hours")?.value) || 0,
            Daily_AI_Tool_Usage_Hours: parseFloat(document.getElementById("Daily_AI_Tool_Usage_Hours")?.value) || 0,
            Sleep_Hours: parseFloat(document.getElementById("Sleep_Hours")?.value) || 0,
            Physical_Activity_Hours: parseFloat(document.getElementById("Physical_Activity_Hours")?.value) || 0,
            Mental_Health_Score: parseFloat(document.getElementById("Mental_Health_Score")?.value) || 0,
            Physical_Health_Score: parseFloat(document.getElementById("Physical_Health_Score")?.value) || 0,
            Social_Isolation_Score: parseFloat(document.getElementById("Social_Isolation_Score")?.value) || 0,
            Burnout_Level: document.getElementById("Burnout_Level")?.value || "Moderate",
            Academic_Performance_Score: parseFloat(document.getElementById("Academic_Performance_Score")?.value) || 0
        };

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await response.json();
            console.log("Server Response Received:", data);

            if (data.error) {
                resultDiv.innerHTML = `<h3 style="color: #ef4444; margin-top: 20px; text-align: center;">Backend Error</h3><p style="text-align: center;">${data.error}</p>`;
            } else {
                const isHigh = data.academic_failure_risk === 1;
                const prob = data.risk_probability;
                const statusColor = isHigh ? '#ef4444' : '#22c55e';

                // Streamlit Speedometer Needle Rotation (-90deg to +90deg)
                const rotationAngle = -90 + (prob * 1.8);

                // Dynamic AI Suggestions
                let aiSuggestions = [];
                if (isHigh) {
                    aiSuggestions = [
                        "⚠️ <strong>Burnout Alert:</strong> Reduce daily screen and social media usage. Aim for 7-8 hours of sleep.",
                        "🎯 <strong>Academic Focus:</strong> Schedule structured study routines using Pomodoro techniques.",
                        "🧘 <strong>Well-being:</strong> Incorporate physical activity to lower social isolation and stress."
                    ];
                } else {
                    aiSuggestions = [
                        "✅ <strong>Balanced Lifestyle:</strong> Maintain your existing study-rest schedule.",
                        "🚀 <strong>Productivity:</strong> Use AI tools constructively for academic learning.",
                        "💪 <strong>Consistency:</strong> Keep up good physical activity and sleeping habits."
                    ];
                }

                const suggestionsHTML = aiSuggestions.map(s => `<li style="margin-bottom: 8px; font-size: 0.85rem; color: #cbd5e1;">${s}</li>`).join("");

                resultDiv.innerHTML = `
                    <div style="border: 1px solid #334155; padding: 25px; border-radius: 16px; background-color: #0f172a; margin-top: 25px; text-align: center;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                            <h3 style="margin: 0; color: ${statusColor};">${data.status}</h3>
                            <span style="background: ${statusColor}22; color: ${statusColor}; padding: 4px 14px; border-radius: 20px; font-weight: bold; border: 1px solid ${statusColor}; font-size: 0.85rem;">
                                ${isHigh ? 'High Risk' : 'Low Risk'}
                            </span>
                        </div>

                        <!-- Speedometer Gauge -->
                        <div style="position: relative; width: 200px; height: 100px; margin: 20px auto 10px auto; overflow: hidden;">
                            <div style="width: 200px; height: 200px; border-radius: 50%; border: 18px solid #1e293b; border-top-color: ${statusColor}; border-right-color: ${statusColor}; box-sizing: border-box; transform: rotate(-45deg);"></div>
                            <div style="position: absolute; bottom: 0; left: 50%; width: 14px; height: 14px; background-color: #f8fafc; border-radius: 50%; transform: translate(-50%, 50%); z-index: 3;"></div>
                            <div id="gaugeNeedle" style="position: absolute; bottom: 0; left: 50%; width: 4px; height: 75px; background-color: #f8fafc; transform-origin: bottom center; transform: translateX(-50%) rotate(-90deg); transition: transform 1.2s cubic-bezier(0.1, 1, 0.1, 1); z-index: 2; border-radius: 4px;"></div>
                        </div>

                        <div style="font-size: 2rem; font-weight: bold; color: #f8fafc; margin-top: 5px;">
                            ${prob}%
                        </div>
                        <span style="font-size: 0.85rem; color: #94a3b8;">Risk Probability Score</span>

                        <!-- Submitted Data Summary Table -->
                        <div style="margin-top: 20px; text-align: left; background-color: #1e293b; padding: 15px; border-radius: 12px; border: 1px solid #334155;">
                            <h4 style="margin: 0 0 10px 0; color: #38bdf8; font-size: 0.95rem;">📊 Input Data Summary</h4>
                            <table style="width: 100%; font-size: 0.82rem; color: #cbd5e1; border-collapse: collapse;">
                                <tr><td style="padding: 4px 0; border-bottom: 1px solid #334155;"><strong>Age / Gender:</strong></td><td style="text-align: right; border-bottom: 1px solid #334155;">${payload.Age} yrs | ${payload.Gender}</td></tr>
                                <tr><td style="padding: 4px 0; border-bottom: 1px solid #334155;"><strong>Education Level:</strong></td><td style="text-align: right; border-bottom: 1px solid #334155;">${payload.Education_Level}</td></tr>
                                <tr><td style="padding: 4px 0; border-bottom: 1px solid #334155;"><strong>Social Media / AI Hours:</strong></td><td style="text-align: right; border-bottom: 1px solid #334155;">${payload.Daily_Social_Media_Hours}h / ${payload.Daily_AI_Tool_Usage_Hours}h</td></tr>
                                <tr><td style="padding: 4px 0; border-bottom: 1px solid #334155;"><strong>Sleep / Activity Hours:</strong></td><td style="text-align: right; border-bottom: 1px solid #334155;">${payload.Sleep_Hours}h / ${payload.Physical_Activity_Hours}h</td></tr>
                                <tr><td style="padding: 4px 0; border-bottom: 1px solid #334155;"><strong>Burnout Level:</strong></td><td style="text-align: right; border-bottom: 1px solid #334155;">${payload.Burnout_Level}</td></tr>
                                <tr><td style="padding: 4px 0;"><strong>Academic Score:</strong></td><td style="text-align: right;">${payload.Academic_Performance_Score} / 10</td></tr>
                            </table>
                        </div>

                        <!-- AI Suggestions Section -->
                        <div style="margin-top: 15px; text-align: left; background-color: #1e293b; padding: 15px; border-radius: 12px; border: 1px solid #334155;">
                            <h4 style="margin: 0 0 10px 0; color: #38bdf8; font-size: 0.95rem;">💡 AI Academic Guidelines</h4>
                            <ul style="padding-left: 18px; margin: 0;">
                                ${suggestionsHTML}
                            </ul>
                        </div>
                    </div>
                `;

                // Gauge Animation
                setTimeout(() => {
                    const needle = document.getElementById("gaugeNeedle");
                    if (needle) needle.style.transform = `translateX(-50%) rotate(${rotationAngle}deg)`;
                }, 100);
            }
        } catch (err) {
            console.error("Fetch Request Failed:", err);
            resultDiv.innerHTML = `<h3 style="color: #ef4444; margin-top: 20px; text-align: center;">Connection Error</h3><p style="text-align: center;">Could not reach FastAPI server at /predict</p>`;
        }
    });
});