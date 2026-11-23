import pandas as pd

data = {
    "Name": ["Pradnya", "Rahul", "Priya"],
    "Attendance": [90, 70, 85]
}

df = pd.DataFrame(data)

print(df)

# Attendance Status
df["Status"] = df["Attendance"].apply(
    lambda x: "Good" if x >= 75 else "Low"
)

print("Student Attendance Report")
print(df)

# Average Attendance
print("\nAverage Attendance:", df["Attendance"].mean())

# Highest Attendance
print("Highest Attendance:", df["Attendance"].max())

# Lowest Attendance
print("Lowest Attendance:", df["Attendance"].min())

print("\nStudents with Low Attendance:")
print(df[df["Attendance"] < 75])