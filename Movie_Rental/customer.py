class Customer:
    def __init__(self, firstName, lastName,idNumber = 0, points = 0, currentRentals = None):
        
        self._idNumber = idNumber + 1
        self._firstName = firstName
        self._lastName = lastName
        self._points = points
        self._currentRentals = currentRentals
        
        def __str__(self):
            """
            string representation of objects
            """
            return "Name: " + (self._firstName) + " " + (self._lastName) \
        + str(self.currentRentals)

