import pandas as pd

def clean_data():
    print("🧹 Cleaning data...")

    # ✅ correct path (you are inside Script folder)
    df = pd.read_csv("../data/raw_employee.csv")

    # fix column names
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    # remove duplicates
    df.drop_duplicates(inplace=True)

    # ✅ fill missing values (FIXED)
    df = df.ffill()

    # standardize text
    if 'city' in df.columns:
        df['city'] = df['city'].str.title()

    if 'department' in df.columns:
        df['department'] = df['department'].str.title()

    if 'gender' in df.columns:
        df['gender'] = df['gender'].str.title()

    # salary cleaning
    if 'salary' in df.columns:
        df = df[df['salary'] > 0]
        df = df[df['salary'] < 200000]

    # experience cleaning
    if 'experience' in df.columns:
        df = df[df['experience'] >= 0]

    # tenure handling
    if 'tenure' in df.columns:
        df['tenure'] = df['tenure'].fillna(df['tenure'].mean())

    # ✅ save cleaned file
    df.to_csv("../data/clean.csv", index=False)

    print("✅ Clean data saved to ../data/clean.csv")


if __name__ == "__main__":
    clean_data()