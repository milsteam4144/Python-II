import csv
from datetime import date, timedelta

class Movie():
    def __init__(self, name, pricePerDay, movieID, genre, daysRented = 0, dueDate = None, startDate = date.today()):
        
        self._name = name
        self._pricePerDay = pricePerDay
        self._movieID = movieID
        self._genre = genre
        self._daysRented = daysRented
        self._startDate = startDate
        self._dueDate = startDate + timedelta(days=daysRented)
        
    def __str__(self):
        return str(self._movieID) + "." + " " + str(self._name) +" ("+ str(self._genre) + ")" + " at " + str('${:,.2f}'.format(self._pricePerDay)) + " per day"
    
    def get_type(self):
        print(type(self._movieID))
    
    def display_Movies(filename):       #To format price '${:,.2f}'.format
        
        """ 
        input: filename, a string
        output: list of Movie objects
        """
        movieList = []
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                name = line[0]
                pricePerDay = float(line[1])
                movieID = int(line[2])
                genre = line[3]
                movie = Movie(name, pricePerDay, movieID, genre)
                movieList.append(movie)
            return movieList
        
    def get_Movie_ByID(movieList, idNum):
        for item in movieList:
            if idNum == item._movieID:
                return item
        
    def display_Movies_Rented(movieList):
        costOfRental = 0
        for item in movieList:
            costPerMovie = item._pricePerDay * item._daysRented
            costOfRental += costPerMovie
            print ("\nTitle: " + item._name + "\nCost Per Day: " + str('${:,.2f}'.format(item._pricePerDay)) + \
                   "\nDays Rented: " + str(item._daysRented) + "\nTotal Cost for " + item._name + " " + str('${:,.2f}'.format(costPerMovie)))
        print ("\nTotal Cost for Rental: " + str('${:,.2f}'.format(costOfRental)))
        #"\nThe start date is " + str(self._startDate.strftime("%A, %B %d, %Y")) + \
        #"\nThe due date is "+ str(self._dueDate.strftime("%A, %B %d, %Y")))