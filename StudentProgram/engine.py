import csv
from student import Student
from arrays import Array
from itertools import islice

def load_csv(filename):
    """
    Loads a CSV file and creates an array of Student objects from the data
    input: filename (a string)
    output: an Array of Student objects
    """
    with open(filename, "r") as inputFile:
        csv_reader = csv.reader(inputFile)
    
        index = 0
        student_object_array = Array(10)
    
        for line in islice(csv_reader, 1, 11):
            student_id = line[0]
            first_name = line[1]
            last_name = line[2]
            program = line[3]
            start_date = line[4]
            advisor_name = line[5]
            recent_term = line[6]
            gpa = line[7]
        
            new_student = Student(student_id, first_name, last_name, program, start_date, advisor_name, recent_term, gpa)
            student_object_array[index]= new_student
            index += 1
    return student_object_array

def get_program(given_array):
    """
    Separates Student objects into lists by the program code
    input: an array of Student objects
    output: three lists of Student objects
    """
    #Create empty lists to hold the Students objects that correspond to the particular program
    comp_prog_dev = list()
    security_program = list()
    network_program = list()
    
    for item in given_array:
        if item._program == "A25590C":
            comp_prog_dev.append(item)
        if item._program == "A25590S":
            security_program.append(item)
        if item._program == "A25590N":
            network_program.append(item)
            
    return comp_prog_dev, security_program, network_program


def list_objects(given_array):
    """
    Prints __str__ of all objects in an array
    input: an array
    output: __str__ of each object in the array
    """
    for item in given_array:
        print (str(item))
