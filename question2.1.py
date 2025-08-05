import pandas as pd # using the Pandas library

# Loading all of the cleaned datasets 
dataset_exam1_cleaned = pd.read_csv("dataset_exam1_cleaned.csv")
dataset_exam2_cleaned = pd.read_csv("dataset_exam2_cleaned.csv")

# Frequency for the average hours spent on campus studying
hours_spent_freq_exam1 = dataset_exam1_cleaned["HoursStudying"].value_counts()
hours_spent_freq_exam2 = dataset_exam2_cleaned["HoursStudying"].value_counts()

# Frequency table for the student age groups 
age_freq_exam1 = dataset_exam1_cleaned["AgeGroup"].value_counts()
age_freq_exam2 = dataset_exam2_cleaned["AgeGroup"].value_counts()

mark_freq_exam1 = pd.cut(dataset_exam1_cleaned["Mark"], bins=[0, 30, 60, 90, 100], labels=["0-30", "30-60", "60-90", "90-100"]).value_counts()
mark_freq_exam2 = pd.cut(dataset_exam2_cleaned["Mark"], bins=[0, 30, 60, 90, 100], labels=["0-30", "30-60", "60-90", "90-100"]).value_counts()

# Displaying all of the frequency tables
print("Frequency table for Average hours spent studying on campus (Exam 1)")
print(hours_spent_freq_exam1)

print("\nFrequency table for Average hours spent studying on campus (Exam 2)")
print(hours_spent_freq_exam2)

print("\nFrequency table for Student AgeGroups (Exam 1)")
print(age_freq_exam1)

print("\nFrequency table for Student AgeGroups (Exam 2)")
print(age_freq_exam2)

print("\nFrequency table for Student Marks (Exam 1)")
print(mark_freq_exam1)

print("\nFrequency table for Student Marks (Exam 2)")
print(mark_freq_exam2)
