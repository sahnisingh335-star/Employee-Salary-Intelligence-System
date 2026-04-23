import pandas as pd
import json
import os
from insights import generate_insights
from sklearn.linear_model import LinearRegression

def run_pipeline():
    print("🚀 Running Pipeline...\n")

    # ================= PATH =================
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "../data/clean.csv")
    output_dir = os.path.join(base_dir, "../Output")

    os.makedirs(output_dir, exist_ok=True)

    # ================= LOAD =================
    df = pd.read_csv(data_path)

    # ================= EXPERIENCE BUCKET =================
    df["exp_level"] = df["experience"].apply(
        lambda x: "Junior" if x <= 2 else "Mid" if x <= 5 else "Senior"
    )

    # ================= KPI =================
    kpi = {
        "avg_salary": float(df["salary"].mean()),
        "max_salary": float(df["salary"].max()),
        "employee_count": int(len(df)),
        "high_performers": int(len(df[df["performance_rating"] >= 4]))
    }

    with open(os.path.join(output_dir, "kpi.json"), "w") as f:
        json.dump(kpi, f, indent=2)

    print("✅ KPI saved")

    # ================= INSIGHTS =================
    insights = generate_insights(df)

    with open(os.path.join(output_dir, "insights.txt"), "w") as f:
        for i in insights:
            f.write(i + "\n")

    print("✅ Insights saved")

    # ================= ML =================
    X = df[["experience", "performance_rating", "tenure"]]
    y = df["salary"]

    model = LinearRegression()
    model.fit(X, y)

    input_data = pd.DataFrame([[5, 4, 3]],
                              columns=["experience", "performance_rating", "tenure"])

    pred = model.predict(input_data)

    print(f"🤖 Predicted salary: {int(pred[0])}")

    # ================= SAFE EXPORT =================
    csv_path = os.path.join(output_dir, "final_report.csv")

    if os.path.exists(csv_path):
        try:
            os.remove(csv_path)
        except:
            csv_path = os.path.join(output_dir, "final_report_new.csv")

    df.to_csv(csv_path, index=False)

    df.to_json(os.path.join(output_dir, "final_report.json"), orient="records", indent=2)

    print("✅ Reports saved")

    print("\n🎉 DONE")

if __name__ == "__main__":
    run_pipeline()