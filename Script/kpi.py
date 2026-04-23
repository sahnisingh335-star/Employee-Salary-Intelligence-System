import pandas as pd

def generate_kpi(df):
    kpi = {}

    # Average salary
    if 'salary' in df.columns:
        kpi['avg_salary'] = int(df['salary'].mean())

    # High performers (rating >=4)
    if 'performance rating' in df.columns:
        kpi['high_performers'] = int((df['performance rating'] >= 4).sum())

    # Total employees
    kpi['total_employees'] = len(df)

    return kpi