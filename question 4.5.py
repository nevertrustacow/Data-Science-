import matplotlib.pyplot as plt
majors_dict = {
    'Math and Statistics': 0,
    'Physical Sciences': 1,
    'Engineering': 2,
    'Computer Science': 3
}

data = {
    "Year": [1970, 1971, 1972],
    "Selected4majors": [
        [65.57092343, 64.55648516, 63.6642632],
        [73.8, 73.9, 74.6],
        [44.4, 46.2, 47.6],
        [68.4, 65.5, 62.6]
    ]
}

def plot_selected4majors(data, majorlist):
    # Creating a figure and axis
    fig, ax = plt.subplots() 

    # Iterate through majorlist and plot each major
    for major in majorlist:
        major_index = majors_dict.get(major, None)
        if major_index is not None:
            ax.plot(data["Year"], data["Selected4majors"][major_index], label=major)

    # Display the legend in the upper left corner
    ax.legend(loc="upper left")  

    ax.set_title("Percentage of Selected4Degrees Awarded per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Selected4Degrees") 
    # Show the plot
    plt.show()  


plot_selected4majors(data, ['Math and Statistics', 'Physical Sciences', 'Engineering', 'Computer Science'])
