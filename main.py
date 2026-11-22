import pandas as pd

data = {
    "Name": ["Shanaya", "Rahul", "Priya", "Amit", "Sneha"],
    "Marks": [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print(df)

print("Average Marks:", df["Marks"].mean())

print("Highest Marks:", df["Marks"].max())

print("Lowest Marks:", df["Marks"].min())

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "D"


df["Grade"] = df["Marks"].apply(calculate_grade)

print(df)

df["Status"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print(df)

df.to_csv("student_data.csv", index=False)

print("CSV file created successfully!")

new_df = pd.read_csv("student_data.csv")

print("Reading Data from CSV:")
print(new_df)

#Charts
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Marks"], color="skyblue", edgecolor="black")

plt.title("Student Marks Analysis", fontsize=16)
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

#pie chart
grade_counts = df["Grade"].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    grade_counts,
    labels=grade_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Grade Distribution")

plt.show()

#barchart
sorted_df = df.sort_values(by="Marks", ascending=True)

plt.figure(figsize=(8, 5))

plt.barh(sorted_df["Name"], sorted_df["Marks"], color="orange")

plt.title("Student Marks Ranking")
plt.xlabel("Marks")
plt.ylabel("Student Name")

plt.xlim(0, 100)

plt.show()
#topper student
topper = df.loc[df["Marks"].idxmax()]

print("Topper Student:")
print("Name:", topper["Name"])
print("Marks:", topper["Marks"])
print("Grade:", topper["Grade"])

#percentage
df["Percentage"] = (df["Marks"] / 100) * 100

print(df[["Name", "Marks", "Percentage"]])

def performance(marks):
    if marks >= 90:
        return "Excellent"
    elif marks >= 75:
        return "Good"
    else:
        return "Needs Improvement"


df["Performance"] = df["Marks"].apply(performance)

print(df[["Name", "Marks", "Performance"]])

print("\n----- STUDENT ANALYSIS REPORT -----")

print("Total Students:", len(df))

print("Class Average:", df["Marks"].mean())

print("Highest Marks:", df["Marks"].max())

print("Lowest Marks:", df["Marks"].min())

print("Total Passed:", (df["Status"] == "Pass").sum())

print("Total Failed:", (df["Status"] == "Fail").sum())

print("Excellent Students:", (df["Performance"] == "Excellent").sum())