import numpy as np

# defining the lists 
Maths_Stats = [65.57092343, 64.55648516, 63.6642632]
Physic_Sci = [73.8, 73.9, 74.6]
Engine = [44.4, 46.2, 47.6]
Comp_Sci = [68.4, 65.5, 62.6]
Year = [1970, 1971, 1972]

# a. Create a Numpy array called “Selected4Majors (converted into floats)
Selected4Majors = np.array([Maths_Stats,Physic_Sci,Engine, Comp_Sci], dtype=float)

# b. crating a dictionary called Majors

majors_dict = {
    "Math and Statistics": 0,
    "Physical Science": 1,
    "Engineering":2,
    "Computer Science": 3
}

#printing the numpy array and the dictionary 
print("Selected4Majors:")
print(Selected4Majors)

print("\nMajors Dictionary:")
print(majors_dict)
