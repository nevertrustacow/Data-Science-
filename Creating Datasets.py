import csv  #This module offers CSV reading and writing capabilities. 
import random #To generate random numbers,select random elements from lists, and shuffle sequences.

# function to generae a random percentage mark based on the individual age groups 
def generate_percentage_mark(age_group):
    if age_group == "18-25":
        return random.uniform(60, 100)
    elif age_group == "26-35":
        return random.uniform(50, 100)
    elif age_group == "36-45":
        return random.uniform(40, 100)
    else:
        return random.uniform(30, 100)

# Function to generate datasets
def generate_datasets(filename, rows):
    with open(filename + ".csv", "w", newline="") as csvfile:
        fieldnames = ["StudentNumber", "AgeGroup", "HoursStudying", "Mark", "ExamTime"]
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        for _ in range(rows):
            student_number = random.randint(1000, 9999)
            age_group = random.choice(["18-25", "26-35", "36-45", "over 45"])
            hours_studying = random.choice(["1-2", "2-3", "4-5"])
            mark = generate_percentage_mark(age_group)
            exam_time = random.uniform(60, 180)

            csv_writer.writerow({
                "StudentNumber": student_number,
                "AgeGroup": age_group,
                "HoursStudying": hours_studying,
                "Mark": mark,
                "ExamTime": exam_time
            })

#generate the first dataset
generate_datasets("dataset_exam1", 150)

#generate the second dataset
generate_datasets("dataset_exam2", 150)

print("Datasets successfully created.")

    
        
