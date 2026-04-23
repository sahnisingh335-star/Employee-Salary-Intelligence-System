import pandas as pd

def generate_insights(df):
    insights = []

    # fix column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # 1. Highest paying department
    if 'department' in df.columns and 'salary' in df.columns:
        dept_salary = df.groupby('department')['salary'].mean()
        top_dept = dept_salary.idxmax()
        insights.append(f"{top_dept} department pays highest salary")

    # 2. Salary vs Experience
    if 'experience' in df.columns and 'salary' in df.columns:
        corr = df['experience'].corr(df['salary'])
        if corr > 0.3:
            insights.append("Salary increases with experience")

    # 3. Gender Pay Gap
    if 'gender' in df.columns and 'salary' in df.columns:
        gender_salary = df.groupby('gender')['salary'].mean()
        if len(gender_salary) >= 2:
            gap = gender_salary.max() - gender_salary.min()
            insights.append(f"Gender salary gap is {int(gap)}")

    # 4. High performers
    if 'performance_rating' in df.columns and 'salary' in df.columns:
        high_perf = df[df['performance_rating'] >= 4]['salary'].mean()
        if not pd.isna(high_perf):
            insights.append(f"High performers avg salary: {int(high_perf)}")

    # 5. City salary comparison
    if 'city' in df.columns and 'salary' in df.columns:
        city_salary = df.groupby('city')['salary'].mean()
        top_city = city_salary.idxmax()
        insights.append(f"{top_city} has highest average salary")

    if not insights:
        insights.append("No strong insights found")

    return insights