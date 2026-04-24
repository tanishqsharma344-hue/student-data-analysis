import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("student_data.xlsx")

# ---------------- CLEANING ---------------- #

# 1. Useless column remove
df = df.drop(columns=['Specify in "Others" (how did you come to know about this event)'])

# 2. Fill missing values
df['How did you come to know about this event?'] = df['How did you come to know about this event?'].fillna("Unknown")
df['College Name'] = df['College Name'].fillna("Unknown")

# 3. Remove duplicates
df = df.drop_duplicates()

print("Cleaning Done")

# ---------------- ANALYSIS ---------------- #

# 1. CGPA vs Salary
print("\nCGPA vs Salary:")
print(df.groupby('CGPA')['Expected salary (Lac)'].mean())

# 2. Python Experience vs Salary
print("\nExperience vs Salary:")
print(df.groupby('Experience with python (Months)')['Expected salary (Lac)'].mean())

# 3. Leadership vs Salary
print("\nLeadership vs Salary:")
print(df.groupby('Leadership- skills')['Expected salary (Lac)'].mean())

# 4. Family Income vs Salary
print("\nFamily Income vs Salary:")
print(df.groupby('Family Income')['Expected salary (Lac)'].mean())

# ---------------- VISUALIZATION ---------------- #

df.groupby('Leadership- skills')['Expected salary (Lac)'].mean().plot(kind='bar')
plt.title("Leadership vs Salary")
plt.xlabel("Leadership Skills")
plt.ylabel("Average Salary (Lac)")
plt.show()

# ---------------- SAVE CLEAN DATA ---------------- #

df.to_excel("cleaned_student_data.xlsx", index=False)
print("\nCleaned file saved ")

print("Unique students:", df['Email ID'].nunique())
print("Average GPA:", df['CGPA'].mean())
print(df['Year of Graduation'].value_counts())
print(df['Experience with python (Months)'].value_counts())
print(df['Family Income'].value_counts())
print(df.groupby('College Name')['CGPA'].mean().sort_values(ascending=False).head())
print(df['Quantity'].describe())
print(df['Attendee Status'].value_counts())
print(df.groupby('City')['CGPA'].mean().sort_values(ascending=False).head())
print(df.groupby('Family Income')['CGPA'].mean())

print(df.groupby('CGPA')['Expected salary (Lac)'].mean())
print(df.groupby('Family Income')['Expected salary (Lac)'].mean())
print(df.groupby('Experience with python (Months)')['Expected salary (Lac)'].mean())
print(df.groupby('Events')['Designation'].value_counts())
print(df.groupby('Leadership- skills')['CGPA'].mean())
print(df.groupby('Leadership- skills')['Expected salary (Lac)'].mean())
print(df[['CGPA','Expected salary (Lac)','Experience with python (Months)']].corr())
print(df[df['Year of Graduation'] <= 2024].shape[0])
print(df['How did you come to know about this event?'].value_counts())
ds = df[df['Events'].str.contains('Data', case=False)]
print(ds.shape[0])
high = df[(df['CGPA'] > 8.5) & (df['Experience with python (Months)'] > 6)]
print(high['Expected salary (Lac)'].mean())
college_counts = df['College Name'].value_counts()
print(college_counts.head())