import csv

# a.Read the percent-bachelors-degrees-women-usa.csv file as a list of lists.
with open("C:\\Users\\zenan\\Data Science project\\archive\\percent-bachelors-degrees-women-usa.csv", "r") as file: 
    reader = csv.reader(file)
    BDW = list(reader)

# b. Assign the result to the variable BDW.
# c. Display the first five rows of BDW separately on different lines.
print("The first five rows of BDW:")
for row in BDW[:5]:
    print(row)

# d. Remove the header row (column names) of the dataset and assign the rest of the dataset to BDW1
BDW1 = BDW[1:]

# e. Using slicing, display the first, second, and third row of BDW1.
print("\nFirst three rows of BDW1:")
for row in BDW1[:3]:
    print(row)

    