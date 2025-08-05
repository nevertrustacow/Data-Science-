import pandas as pd
import matplotlib.pyplot as plt #imports the pyplot module of the Matplotlib 
import seaborn as sns #imports the Seaborn library

sns.set(style="whitegrid") #enhances readability by adding gridlines to the plot's background

dataset_exam1_cleaned = pd.read_csv("dataset_exam1_cleaned.csv") # reads the csv file 
dataset_exam2_cleaned = pd.read_csv("dataset_exam2_cleaned.csv") # raeds the csv file 

# First task: Bar chart for ages and number of students
plt.figure(figsize=(10, 6)) # the given size 
sns.countplot(x="AgeGroup", data=dataset_exam1_cleaned, order=["18-25", "25-35", "35-45", "over 45"], palette="viridis", hue = "AgeGroup") 
plt.title("Number of Students in Each Age Group (Exam 1)") # this line sets the title
plt.xlabel("Age Group") #lables the x-axis
plt.ylabel("Number of Students") #lables the y-axis
plt.show() # displays the plot

# First Task: Bar chart for ages and number of students Exam 2
plt.figure(figsize=(10, 6))  
sns.countplot(x="AgeGroup", data=dataset_exam2_cleaned, order=["18-25", "25-35", "35-45", "over 45"], palette="viridis", hue = "AgeGroup")
plt.title("Number of Students in Each Age Group (Exam 2)")
plt.xlabel("Age Group") 
plt.ylabel("Number of Students") 
plt.show() 

# Second Task: Line graph between higher marks and more time spent on campus
plt.figure(figsize=(10, 6)) # the given size 
sns.lineplot(x="Mark", y="ExamTime", data=dataset_exam1_cleaned, markers="o", color="blue") # it displays the relationship between exam results and student attendance
plt.title("Correlation between Marks and Time Spent on Campus (Exam 1)") # the title of the graph
plt.xlabel("Student Marks") # the title for the x-axis
plt.ylabel("Time Spent on Campus (minutes)") # the title for the y-axis
plt.show() # displays the line graph

# Second Task: Line graph between higher marks and more time spent on campus (Exam 2)
plt.figure(figsize=(10, 6))
sns.lineplot(x="Mark", y="ExamTime", data=dataset_exam2_cleaned, markers="o", color="blue")
plt.title("Correlation between Marks and Time Spent on Campus (Exam 2)")
plt.xlabel("Student Marks")
plt.ylabel("Time Spent on Campus (minutes)")
plt.show()

# Third Task: Scatter chart for each student's marks and the time taken on the exam
plt.figure(figsize=(10, 6)) # the given size 
sns.scatterplot(x="Mark", y="ExamTime", data=dataset_exam1_cleaned, hue="AgeGroup", palette="coolwarm", s=80) # a scatter plot is produced on this line 
plt.title("Scatter Plot of Student Marks and Exam Time (Exam 1)") # the title for the scatter plot
plt.xlabel("Student Mark") # title for the x-axis
plt.ylabel("Time Taken on Exam (minutes)") # title for the y-axis
plt.legend(title="Age Group") # inserts legend with name AgeGroup
plt.show() # displays the scatterplot

# Third Task: Scatter chart for each student's marks and the time taken on the exam (Exam2)
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Mark", y="ExamTime", data=dataset_exam2_cleaned, hue="AgeGroup", palette="coolwarm", s=80)
plt.title("Scatter Plot of Student Marks and Exam Time (Exam 2)")
plt.xlabel("Student Mark")
plt.ylabel("Time Taken on Exam (minutes)")
plt.legend(title="Age Group")
plt.show()

# Fourth Task: Scatter chart for the relationship between time spent on campus and student's age
plt.figure(figsize=(10, 6)) # the given size 
sns.scatterplot(x="HoursStudying", y="AgeGroup", data=dataset_exam1_cleaned, hue="Mark", palette="viridis", s=80) # a scatter plot is produced on this line 
plt.title("Scatter Plot of Time Spent on Campus and Student Age (Exam 1)") # the title of the graph
plt.xlabel("Hours Spent on Campus") # title of the x-axis 
plt.ylabel("Age Group") # title for the y-axis
plt.legend(title="Student Mark") # inserts legend with the name Student Mark
plt.show() # Displays the scatter plot

# Fourth Task: Scatter chart for the relationship between time spent on campus and student's age (Exam 2)
plt.figure(figsize=(10, 6))
sns.scatterplot(x="HoursStudying", y="AgeGroup", data=dataset_exam2_cleaned, hue="Mark", palette="viridis", s=80)
plt.title("Scatter Plot of Time Spent on Campus and Student Age (Exam 2)")
plt.xlabel("Hours Spent on Campus")
plt.ylabel("Age Group")
plt.legend(title="Student Mark")
plt.show()
