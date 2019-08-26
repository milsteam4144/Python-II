class Rental():
    def __init__(self, customer, rentalID = 0):
        
        self._rentalID = rentalID + 1
        #self._movies = []
        self._customer = customer
        
    def __str__(self):
        return ("\n\nRental ID: " + str(self._rentalID)+ "\nCustomer Name: " + str(self._customer._firstName) + " " + str(self._customer._lastName))

    def rent_movie(movie, daysRented, movies = []):
        """
        Adds a Movie object to the Rental object's movies(list) property
        input: movie object
        output: updated list property of Rental (movies)
        """
        movie._daysRented = daysRented
        movies.append(movie)
        return movies