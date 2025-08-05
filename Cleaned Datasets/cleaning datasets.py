"""
Before performing operations on your data, you need to clean your data, remove any zero values 
and document the process thoroughly in your report.
"""
import pandas as pd

# Loading the datasets 
dataset_exam1 = pd.read_csv("dataset_exam1.csv")
dataset_exam2 = pd.read_csv("dataset_exam2.csv")

# Displaying the initial dataset statistics 
print("Initial dataset statistics:")
print("Dataset Exam 1:")
print(dataset_exam1.describe())
print("\nDataset Exam 2:")
print(dataset_exam2.describe())

# Remove rows with zero/no values 
dataset_exam1_cleaned = dataset_exam1[(dataset_exam1 != 0).all(1)]
dataset_exam2_cleaned = dataset_exam2[(dataset_exam2 != 0).all(1)]

# Display cleaned datasets statistics 
print("\nCleaned dataset statistics:")
print("Dataset Exam 1 (after removing zero values):")
print(dataset_exam1_cleaned.describe())
print("\nDataset Exam 2 (after removing zero values):")
print(dataset_exam2_cleaned.describe())

dataset_exam1_cleaned.to_csv("dataset_exam1_cleaned.csv", index=False)
dataset_exam2_cleaned.to_csv("dataset_exam2_cleaned.csv", index=False)

print("\nDatasets have now been cleaned and have been saved to 'dataset_exam1_cleaned' and 'dataset_exam2_cleaned'")
