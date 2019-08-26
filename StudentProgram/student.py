class Student():
    def __init__(self, student_id, first_name, last_name, program, start_date, advisor_name, recent_term, gpa):
        """constructor"""
        self._student_id = student_id
        self._first_name = first_name
        self._last_name = last_name
        self._program = program
        self._start_date = start_date
        self._advisor_name = advisor_name
        self._recent_term = recent_term
        self._gpa = gpa
        
        
    def __str__(self):
        """string representation"""

        #return str(self._student_id) + " " + str(self._first_name) + " " + str(self._last_name) +\
                 #" " + str(self._program) +" " + str(self._start_date) + \
                  #" " + str(self._advisor_name) + " " + str(self._recent_term) + " " + str(self._gpa)

        return (self._first_name) + " " + (self._last_name)
        
    
        
        

