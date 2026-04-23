import pandas as pd
from sklearn.linear_model import LinearRegression

def run_prediction():
    print("🤖 Running Advanced Salary Prediction...\n")

    df = pd.read_csv("../data/clean.csv")

    # features
    X = df[["experience", "performance_rating", "tenure"]]
    y = df["salary"]

    model = LinearRegression()
    model.fit(X, y)

    # sample input
    input_data = pd.DataFrame([[5, 4, 3]], 
                              columns=["experience", "performance_rating", "tenure"])

    pred = model.predict(input_data)

    print(f"💰 Predicted salary: {int(pred[0])}")

if __name__ == "__main__":
    run_prediction()