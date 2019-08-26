# CSC221
# M3HW
# 11/11/2018

"""
Author: Mallory Milstead
Reads in a csv of movies, creates objects, allows user to create a list (rental) of objects and displays the details and total cost
of all items in the rental
"""

from rental import Rental
from customer import Customer
from movie import Movie

#Input: movie and number of days
#Output: total charges for number of days

def main():
    """
    Allows the user to add movies to their cart(Rental)
    Input: The menu choice that the user would like to add (an int) or 
    Output: The string representation of a list of movies and the total cost to rent them all
    """

    movieList = Movie.display_Movies("movie_csv.txt")#Read the movies from CSV, create objects

    for item in movieList:
        print(str(item))#Display the objects to the user
        
    newCustomer = Customer("Mister", "Customer") #Create customer object

    newRental = Rental(newCustomer) #Create a new rental
        
    keepGoing = "yes"
    
    while keepGoing != "no":

        movieChoice = int(input("Enter the number of the movie to rent: "))
        daysRented = int(input("Enter the number of days to keep the movie: "))
        
        rented_movie_list = Rental.rent_movie(Movie.get_Movie_ByID(movieList, movieChoice), daysRented)
        #Get the movie by it's id property, pass the movie object and the number of days rented to the rent_movie method.
        #Rental.rent_movie adds it to a list and returns that list
    
        keepGoing = input("Would you like to rent another movie? ").lower()


    print(str(newRental)) #Display the poroperties of the Rental object
    Movie.display_Movies_Rented(rented_movie_list)#Display the movies in rented_movie_list and their relevant properties

if __name__ == '__main__':
	main()


