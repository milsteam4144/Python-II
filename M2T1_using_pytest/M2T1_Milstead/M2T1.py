# CSC221
# M2T1_Milstead
# Goal: Gold

"""
Author: Mallory Milstead
Allow user to choose from menu to check a string for the vowels and letters
that is contains and display to the user

"""
def main():
    """
    Input: Choose menu option 1 or 2
    Option 1 Input: string to check for vowels
             Output: list of vowels in string (a, e, i, o, u)
             
    Option 2 Input: string and letters to check for in string
             Output: list of letters that appear in the string
    
    """
    runAgain = "y"
    while runAgain == "Y" or runAgain == "y":
        userChoice = getUserChoice()
        if userChoice == 1 or userChoice == "1":
            print(has_which_vowels(str(input("Enter a string to check for vowels: "))))
        elif userChoice == 2 or userChoice == "2":
            print(has_which_letters(str(input("Enter a string to check for letters: ")), list(input("Enter the letters you would like to check for: "))))
        runAgain = input("Would you like to run the program again? Y or N: " + "\n")
    print("Goodbye")
    
    
    
def getUserChoice():
	"""Ask the user to choose option "1" or "2" to run the program"""
	userChoice = int(input('To check a string for vowels, enter "1" \
	 \n \nTo check a string for letters, enter "2"'))
	return userChoice
    
    
def has_which_vowels(string):
    """
    returns a list of the vowels(a, e, i, o, u) that occur in a string
    """
    vowels = "aeiou"
    vowelList = list(vowels)
    vowelsInString = list()
    for char in string:
        if char in vowelList:
            vowelsInString.append(char)
    return (vowelsInString)
    
def has_which_letters(string, lettersToCheck):
    """
    returns a list of the letters that occur in a string
    """
    lettersInString = list()
    for char in lettersToCheck:
        if char in string:
            lettersInString.append(char)
    return (lettersInString)
    

if __name__ == "__main__":
    main()

