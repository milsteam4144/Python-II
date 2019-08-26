# CSC221
# M3HW
# 11/11/2018

"""
Author: Mallory Milstead
Reads in a csv file, creates lists from the data and displays it
in a web browser in plain HTML
"""

import csv
from flask import Flask


def load_csv(filename):
    """ 
    input: filename, a string
    output: list of names and list of GPAs
    """
    studentNames = []
    studentGPAs = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader) #skips the first line in the CSV file
        for row in reader:
            studentNames.append(row[0])
            studentGPAs.append(float(row[2]))
    return studentNames, studentGPAs

app = Flask(__name__)

@app.route('/')
def main():
    studentsList, gradesList = load_csv("students2.csv")

    newList = []
    newList.append("  Name&nbsp &nbsp &nbsp Grade ")

    for item in studentsList:
        string =item +"&nbsp &nbsp &nbsp " + str(gradesList[studentsList.index(item)])
        newList.append(string)
    
    return("<p>" + "</p><p>".join(newList) + "</p>")
    
#if __name__ == '__main__':
	#app.run(debug=True)
    
