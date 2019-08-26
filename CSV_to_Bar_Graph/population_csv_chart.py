# CSC221
# M3HW
# 11/11/2018

"""
Author: Mallory Milstead
Reads in data from csv and creates two lists which are used to
create a bar graph of the population of Maryland corresponding to a year
"""


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv
from itertools import islice

def main():
    yearsList, populationList = load_csv("Maryland_Population.csv")
    
    rangeOfYears = np.arange(len(yearsList)) #Returns the range (difference between highest and lowest)
    plt.bar(rangeOfYears, populationList, align = "center", color = "purple", width = .8)
    plt.xticks(rangeOfYears, yearsList, rotation = "vertical")
    plt.ylabel("Population of Maryland")
    plt.xlabel("Year")
    
    plt.show()

def load_csv(filename):
    """ 
    input: filename, a string
    output: list of years from 2000-2013 and list of numbers representing the population of Maryland for a corresponding year
    """
    
    yearsList = []
    populationList = []
    with open(filename) as f:
        reader = csv.reader(f)
        for line in islice(reader,112,128): #or 129
            yearsList.append(int(line[0]))
            populationList.append(int(line[1]))
    return yearsList, populationList


if __name__ == '__main__':
	main()
