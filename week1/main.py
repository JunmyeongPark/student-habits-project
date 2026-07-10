import pandas as pd
import numpy as np
import matplotlib
import sklearn
import os

    
def load_data(path):
    if os.path.exists(path):
        df = pd.read_csv(path, encoding="utf-8-sig")
        return df
    else:
        print("no file named ", path)
        exit(0)

def explore_structure(df):
    print("structure: ", df.shape)
    print(df.dtypes)
    print(df.head)

def show_statistics(df):
    print(df.describe())
    print(df.mean(numeric_only=True))

def check_missing(df):
    for col in df.columns:
        if col in ["sleep_hours", "phone_hours", "exercise_hours"]:
            missing_ratio = df[col].isnull().sum()/len(df)

            if missing_ratio < 0.05:
                missing_ratio_str = "낮음"
            elif missing_ratio < 20:
                missing_ratio_str = "주의"
            else:
                missing_ratio_str = "높음"
            print(f"{col} mean: {df[col].mean()}, 결측률: {missing_ratio}, 심각도: {missing_ratio_str}")

def numpy_stats(df):
    print(df.describe())

    for col in df.select_dtypes(include="number").columns:
        values = df[col].dropna().values
        print(f"<{col}>")
        print("mean: ", round(np.mean(values), 6), end=" ")
        print("std: ", round(np.std(values), 6), end="\n\n")


if __name__ == "__main__":
    path = "/home/myung/student-habits-project/data/student_habits.csv"
    df = load_data(path)
    print(df.describe())
    explore_structure(df)
    show_statistics(df)
    check_missing(df)
    numpy_stats(df)

