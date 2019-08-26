# CSC221
# M3T1_Milstead
# Goal: Gold

"""
Author: Mallory Milstead
Reads CSV data into Student objects, creates an array of objects and manipulates and displays the objects in the Array
"""


from arrays import Array
import engine
from student import Student

def main():

    runAgain = "y"

    while runAgain == "y":
        
        userOption = input("-" * 45 + """\nChoose a menu option:\n
        1. Load CSV/Create Array
        2. List all Students
        3. List Students by Program
        4. Exit\n""" + "-" * 45)

        if userOption == "1":
    
            #Call load_csv method from engine module--it returns a list of student objects
            student_object_array = engine.load_csv("student_advisees_testdata.csv")
            print("CSV has been loaded and Array created...")
        if userOption == "2":
            #Calls list_object method to display all objects in the array
            engine.list_objects(student_object_array)
        if userOption == "3":
            #get_program method changes the Student object's _program property from a code to english
            comp_prog_dev, security_program, network_program = engine.get_program(student_object_array)
    
            print("Computer Programming & Development\n".upper())
            engine.list_objects(comp_prog_dev)
            print("\nSystem Security and Analysis\n".upper())
            engine.list_objects(security_program)
            print("\nNetwork Managment\n".upper())
            engine.list_objects(network_program)

        if userOption == "4":
            runAgain = "n"

    
if __name__ == "__main__":
    main()

