# CSC221
# M2T2_Milstead
# Goal: Gold
# Uses student2.csv

"""
Author: Mallory Milstead
User chooses from menu options to load CSV, pickle and unpickle two lists and display sorted data
"""

import csv
import pickle


def main():
    """
    Allows the user to choose an option from the menu.

    Input: The menu choice that the user would like to run (an int)
    Output: Student and GPA data specific to the menu choice
    """

    chooseOption = ""

    while chooseOption != "6":
    
        chooseOption = str(input("\nEnter a number to execute that menu choice: \n1. Load CSV\n2. Create Pickle File\n3. Load Pickle File\n4. Show Students by Name\n5. Show Students by GPA\n6. Exit Program\n"))
        if chooseOption == "1":
            names, grades = load_csv('students2.csv')
            print("The CSV file has been loaded...")

        if chooseOption == "2":
            try:
                pickle_file(names, grades, "pickled_names_grades")
                print("Your data has been pickled...")
            except UnboundLocalError:
                print("You must load CSV before pickling data")

        if chooseOption == "3":
            try:
                names, grades = unpickle_file(names, grades, "pickled_names_grades")
                print("Your data has been unpickled/loaded...")
            except UnboundLocalError:
                print("You must load CSV and pickle data before unpickling")
            

        if chooseOption == "4":
            try:
                student_grade_list = []
                for i in range(0, len(names)):
                    student_data = [names[i], grades[i]]
                    student_grade_list.append(student_data)
                student_grade_list.sort(key = lambda x: x[0])
                for item in student_grade_list:
                    print('{:10s}{:5.1f}'.format(item[0],item[1]))
            except UnboundLocalError:
                print("You must load CSV pickle and unpickle data before referencing it")
            

        if chooseOption == "5":
            try:
                student_grade_list.sort(key = lambda x: x[1])
                for item in student_grade_list:
                    print('{:10s}{:5.1f}'.format(item[0],item[1]))
            except UnboundLocalError:
                print("You must load CSV pickle and unpickle data before referencing it")

        if chooseOption == "6":
           exit()
            

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

def pickle_file(list1, list2, filename):
    """
    Pickles two lists

    Input: first list to pickle, second list to pickle, filename to hold pickled data
    Output: a pickled file containing the two lists
    """

    writeFile = open(filename, "wb")
    pickle.dump(list1, writeFile)
    pickle.dump(list2, writeFile)
    writeFile.close()

def unpickle_file(list1, list2, filename):
    """
    Unpickles a file into 2 lists

    Input: the names to give to the (2)unpickled list, the filename to unpickle
    Output: two pickled lists with the given listname
    """
    list1 = []
    list2 = []

    readFile = open(filename, "rb")
    while True:
        try:
            list1 = pickle.load(readFile)
            list2 = pickle.load(readFile)
        except EOFError:
            readFile.close()
        return list1, list2
            
            
    
    
		
if __name__ == '__main__':
	main()
	
