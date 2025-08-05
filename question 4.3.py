BDW1 = [
    [1970, 4.22979798, 11.92100539, 59.7, 29.08836297, 9.064438975, 35.3, 13.6, 74.53532758, 0.8, 65.57092343, 73.8, 77.1, 38, 13.8, 44.4, 68.4, 36.8],
    [1971, 5.452796685, 12.00310559, 59.9, 29.39440285, 9.503186594, 35.5, 13.6, 74.14920369, 1, 64.55648516, 73.9, 75.5, 39, 14.9, 46.2, 65.5, 36.2],
    [1972, 7.42071022, 13.21459351, 60.4, 29.81022105, 10.5589621, 36.6, 14.9, 73.55451996, 1.2, 63.6642632, 74.6, 76.9, 40.2, 14.8, 47.6, 62.6, 36.1]
   
]

# Initialize lists for each major and years
Maths_Stats = []
Physic_Sci = []
Engine = []
Comp_Sci = []
Year = []

#Itereate through each roe in BDW1
for row in BDW1:
    #extract the year
    year = row[0]
    Year.append(year)

    #extracting the precentages for each major
    Maths_Stats.append(row[13])
    Physic_Sci.append(row[14])
    Engine.append(row[9])
    Comp_Sci.append(row[7])

print("Maths_Stats:", Maths_Stats)
print("Physical Science:", Physic_Sci)
print("Engineering:",Engine)
print("Computer Science:", Comp_Sci)
print("Year:",Year)