'''
Author: Harrison Servedio
Bugs:

Features:

Bonues:
    Sylable Counter
    Length of String
    Totals of vowels and consonants
'''

import string # Used to get an uppercase and lowercase alphabet
import random as r

'''
The class string2 has many of the functions that the original string class and some others
This class is used to make running some of the functions easier
Some of the functions of this class return a statement which should be printed and others just return a value
'''
class string2:
    def __init__(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Does not return anything
        # initializes all the variables
        self.val = self.name()
        self.uppercase = list(string.ascii_uppercase)
        self.lowercase = list(string.ascii_lowercase)
        self.valLower = self.MyLower()
    
    def name(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Returns the persons name
        # This function introduces the user to the program and asked for their name
        print('\n____________________________________________________________________________________________________________________')
        print('\nWelcome to "What\'s in a Name"!\n')
        return input('Note: Some of the functions may not work well unless you enter an actual name\nWhat is your name? ')
        
    
    def __str__(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Returns the name
        # This function makes it possible to print the class as the important values which is the name
        return self.val
    
    def MyLower(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Returns the string in lowercase
        # Iterates through the characters and puts them in lower case
        temp = ""
        for i in self.val:
            if i in self.uppercase:
                place = self.uppercase.index(i)
                temp += self.lowercase[place]
            else:
                temp += i
        return temp
    
    def MyUpper(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Returns the string in upper case
        # iterates the the chracters and capitolised the characters
        temp = ""
        for i in self.val:
            if i in self.lowercase:
                place = self.lowercase.index(i)
                temp += self.uppercase[place]
            else:
                temp += i
        return temp
    
    reverse = lambda self : self.val[::-1]
    # Takes the class which contains the name and the functions require to modify the string
    # Returns the reversed string
    # Reverses the string by use interesting string indexing

    length = lambda self: self.val.rindex(self.val[-1])+1
    # Takes the class which contains the name and the functions require to modify the string
    # Returns the length of the string
    # Find the length of a string by finding the index position of the last letter and adding one
    
    def vowel(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Returns the number of vowels in a name as printable string
        # Iterates through the vowels and checks if the chracters are vowels and counts the vowels
        letters = 'aeiou'
        frequency = [0, 0, 0, 0, 0]
        for i in self.MyLower():
            if i in letters:
                frequency[letters.index(i)] += 1
            
        return f'There are {frequency[0]} a(s) \nThere are {frequency[1]} e(s) \nThere are {frequency[2]} i(s) \nThere are {frequency[3]} o(s) \nThere are {frequency[4]} u(s)\n'
            
    def consonants(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Returns the number of consonants in a name as a printable string
        # Iterates through the characters and checks if the chracters are consonants and counts the consonants
        letters = 'bcdfghjklmnpqrstvwxyz'
        frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in self.MyLower():
            if i in letters:
                frequency[letters.index(i)] += 1
        ret = ''
        for i in letters:
            ret += f"There are {frequency[letters.index(i)]} {i}(s) \n"
        return ret
    
    def MySplit(self, x):
        # Takes the class which contains the name and the functions require to modify the string
        # The character that the string is split at
        # The string that is split into a list
        # Splits the string into a list at the character represented by the variable x
        temp = []                                                                       # This variable stores the output
        temp2 = ''                                                                      # This varible is added on too in the for loop until the for loop detects the x 
        for i in self.val:
            if i == x:                                                                  # If the i is the x, temp gets another value and temp2 is reset
                temp.append(temp2)
                temp2 = ''
            else:
                temp2 += i                                                              # When the i is not x temp2 grows
        if self.val[-1] != x:                                                           # This piece of code make sure that there is not a problem when the variable does not end in x
            temp.append(temp2)
        return temp
    
    def names(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Returns the fisrt middle and last name split up
        # Finds the first middle and last names by spliting the name at the space character
        temp = self.MySplit(' ')                                                        # Their name is split by spaces
        if len(temp) == 2:                                                              # This code is run if they only entered two names(first and last)
            print(f'Your first name is {temp[0]}.\nYour last name is {temp[1]}.')
        elif len(temp) == 3:                                                            # This code is run if they entered 3 names(first, middle, last)
            print(f'Your first name is {temp[0]}.\nYour middle name is {temp[1]}.\nYour last name is {temp[2]}.')
        elif len(temp) == 1:                                                            # This code accounts for the user only entering first names
            print(f'Your first name is {temp[0]}.')
        elif len(temp) > 3:                                                             # This code runs if they entered more than 3 and just lists off the names
            print('Here are your names in order:')
            for i in temp:
                print(i)

    # This function checks if there is a hyphem in a name with and if statement and returns one of two strings based on the result           
    isHyphen = lambda self : 'There is a hyphen in your name.' if '-' in self.val else 'There is not a hyphen in your name.'
    # Takes the class which contains the name and the functions require to modify the string
    # Returns if there is a hyphen in your name
    # Checks if there is a hyphen in the name and returns the output as txt

    def randomName(self):
        # Takes the class which contains the name and the functions require to modify the string
        # returns a the character in the name randomised
        # Randomises the chracters in a name and returns the output
        temp = list(self.val)                                                           # First the name is converted to a list
        for i in range(r.randint(100, 200)):                                            # The for loop is used to run the next two lines a random amount of times
            temp2 = r.randint(0, len(temp)-1)                                           # Picks a random list index 
            temp.append(temp.pop(temp2))                                                # Moves that list index to the end of the list
        # The next four lines convert the list back into a string and return the output
        stringList = ''
        for i in temp:
            stringList += i
        return stringList
    
    
    isPalindrome = lambda self : 'Your name is a palindrome.' if self.valLower[::-1] == self.valLower else 'Your name is not a palindrome.'
    # Takes the class which contains the name and the functions require to modify the string
    # Returns if the name is a palendrome 
    # Checks if the name is a palendrome by checking if the reverse vertion of a name is equal to the name
    
    
    def sortedCharacter(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Returns a list of the sorted characters
        # Sorts the character in the name
        temp = list(self.val)                                                           # First the string is converted to a list
        result = []                                                                     # A blank list that will stores the results
        result.insert(0, temp[0])                                                       # This line and the next moves the first character from the temp list into the results list so the is a starting point for the code
        temp.pop(0)
        for i in temp:                                                                  # Iterates through all the letters in temp
            for j in result:                                                            # Iterates through all the letters in the results list, comparing the value of the letters to the temp list and inserting the letters in the correct position
                if i == j:
                    result.insert(result.index(j),i)
                    break
                elif i < j:
                    result.insert(result.index(j), i)
                    break
                elif i > result[-1]:
                    result.insert(len(result), i)
                    break
        return result


    def sylables(self):
        # Takes the class which contains the name and the functions require to modify the string
        # Returns the number of sylables
        # By using a combonation of looking for vowels and combonations of letters it produces a estimation of the number of sylables
        sylableCounter = 0                                                              # A integer that stores the number of characters
        # Both of the next variables can't be empty otherwise it would messes up the functions so I set them to a random string
        lastLetter = 'asdfeaowiunfd'                                                    # When iterating through the letter this value will represent previous letter
        TwoBackLetter = 'afuweiaoduscvierqw'                                            # When iterating through the letter this value will represent the letter two back from the current one
        vowelCombonations = (('i', 'a'), ('e', 'o'), ('i', 'o'), ('i', 'e'), ('u', 'a'))# This is a list with all the two vowel combonations that make 2 sylables
        for letter in self.MyLower():
            '''
            This next block of code uses vowels to find the amount of sylables in a word
            Any time two vowels come in a row it is treated as 1 sylable unless the combonation is in the list above
            '''
            if (lastLetter, letter) in vowelCombonations:                               # Checks if the vowel combonation is in the list
                TwoBackLetter = lastLetter
                lastLetter = letter
                sylableCounter += 1
                continue
            elif lastLetter in 'aeiouy':                                                # If the previous letter is a vowels than the program does not count the second vowel as a sylable unless the combonation is in the list
                TwoBackLetter = lastLetter
                lastLetter = letter
                continue
            # This elif statement checks if the letter two behind an e is a vowel because if it is a vowels than the e is note counted as a sylable
            elif (letter == 'e' == self.MyLower()[-1] and TwoBackLetter in 'aeiou'):
                TwoBackLetter = lastLetter
                lastLetter = letter
                continue
            elif letter in 'aeiouy':                                                    # If not of the previouse statements have run and the current letter is a vowels, the program assumes the vowel is it's own sylable
                TwoBackLetter = lastLetter
                lastLetter = letter
                sylableCounter += 1
                continue
            else:                                                                       # This else statement catches all consonants
                TwoBackLetter = lastLetter
                lastLetter = letter
                continue
        return sylableCounter                                                           # Returns the number of sylables as an integer
    

    def menu(self):
        # Takes class for information about the name
        # does not return anything but managed user input
        # manages the functions and runs them based on user input
        # This code displays all the options for the user to select
        print('\nHere you will be able to select a function. Enter the the number that corresponds to the function you want.')
        f = open('funcs.txt')
        text = f.read()
        print(text)
        x = input('12-Reverse\n')
        '''
        This block of code does the input validation
        '''
        while True:
            try:
                x = int(x)                                                              # Tries to convert the user input to an integer to make sure the input is correct
                if x < 1 or x > 12:
                    raise ValueError                                                    # Raises an error if the number is too small or too great
                break                                                                   # Breaks the loop if everything runs correctly
            except:                                                                     # Repeats asking for input if the input is not correct
                print('\nThat input is not valid.')
                x = input("Please enter a valid input: ")
        '''
        This next block of code check what the input is and runs the correct function
        It is not the best way to do it but it works
        '''
        if x == 1:
            print(f"You name in lowercase is {self.MyLower()}.")
        elif x == 2:
            print(f'Your name in uppercase is {self.MyUpper()}.')
        elif x == 3:
            print(f"You have {str(self.sylables())} sylables in your name.")
        elif x == 4:
            print(f'Here is you name as sorted characters: {self.sortedCharacter()}')
        elif x == 5:
            print(self.isPalindrome())
        elif x == 6:
            print(f'Here is you name as random characters: {self.randomName()}')
        elif x == 7:
            print(f'{self.isHyphen()}')
        elif x == 8:
            self.names()
        elif x == 9:
            print(self.consonants())
        elif x == 10:
            print(self.vowel())
        elif x == 11:
            print(f'Your name is {self.length()} characters long')
        elif x == 12:
            print(f'Here is your name in reverse: {self.reverse()}')
        temp = input("Enter 'yes' if you want to try another function. Otherwise, enter anything else to quit. ") # Makes the instuctions clear so the user know what will happen if they don't enter 'yes'
        if temp == 'yes':
            self.menu()                                                                 # Runs the menu function again if the user enter 'Yes'



x = string2()                                                                           # Creates an instance of the string2 class
x.menu()                                                                                # Runs the menu function so the user can run functions
