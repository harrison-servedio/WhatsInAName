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
        self.val = self.nameInputValid()
        self.uppercase = list(string.ascii_uppercase)
        self.lowercase = list(string.ascii_lowercase)
        self.valLower = self.MyLower()
    
    def nameInputValid(self):
        print('\n____________________________________________________________________________________________________________________')
        print('\nWelcome to "What\'s in a Name"!\n')
        return input('Note: Some of the functions may not work well unless you enter an actual name\nWhat is your name? ')
        
    
    def __str__(self):
        return self.val
    
    def MyLower(self):
        temp = ""
        for i in self.val:
            if i in self.uppercase:
                place = self.uppercase.index(i)
                temp += self.lowercase[place]
            else:
                temp += i
        return temp
    
    def MyUpper(self):
        temp = ""
        for i in self.val:
            if i in self.lowercase:
                place = self.lowercase.index(i)
                temp += self.uppercase[place]
            else:
                temp += i
        return temp
    
    reverse = lambda self : self.val[::-1]
    
    length = lambda self: self.val.rindex(self.val[-1])+1
    
    def vowel(self):
        letters = 'aeiou'
        frequency = [0, 0, 0, 0, 0]
        for i in self.MyLower():
            if i in letters:
                frequency[letters.index(i)] += 1
            
        return f'There are {frequency[0]} a(s) \nThere are {frequency[1]} e(s) \nThere are {frequency[2]} i(s) \nThere are {frequency[3]} o(s) \nThere are {frequency[4]} u(s)\n'
            
    def consonants(self):
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
        temp = []
        temp2 = ''
        for i in self.val:
            if i == x:
                temp.append(temp2)
                temp2 = ''
            else:
                temp2 += i
        if self.val[-1] != x:
            temp.append(temp2)
        return temp
    
    def names(self):
        temp = self.MySplit(' ')
        if len(temp) == 2:
            print(f'Your first name is {temp[0]}.\nYour last name is {temp[1]}.')
        elif len(temp) == 3:
            print(f'Your first name is {temp[0]}.\nYour middle name is {temp[1]}.\nYour last name is {temp[2]}.')
        elif len(temp) == 1:
            print(f'Your first name is {temp[0]}.')
        elif len(temp) > 3:
            print('Here are your names in order:')
            for i in temp:
                print(i)
                
    isHyphen = lambda self : 'There is a hyphen in your name.' if '-' in self.val else 'There is not a hyphen in your name.'
    
    def randomName(self):
        temp = list(self.val)
        for i in range(r.randint(100, 200)):
            temp2 = r.randint(0, len(temp)-1)
            temp.append(temp.pop(temp2))
        stringList = ''
        for i in temp:
            stringList += i
        return stringList
    
    isPalindrome = lambda self : 'Your name is a palindrome.' if self.valLower[::-1] == self.valLower else 'Your name is not a palindrome.'
    
    def sortedCharacter(self):
        temp = list(self.val)
        result = []
        result.insert(0, temp[0])
        temp.pop(0)
        for i in temp:
            for j in result:
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
        sylableCounter = 0
        # Both of the next variables cant be empty otherwise it would messes up the function
        lastLetter = 'asdfeaowiunfd'            
        TwoBackLetter = 'afuweiaoduscvierqw'
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
    # This code lets the user run any of the functions
    def menu(self):
        # This code displays all the options for the user to select
        print('\nHere you will be able to select a function. Enter the the number that corresponds to the function you want.')
        print('1-Lower')
        print('2-Upper')
        print('3-Syllable Counter')
        print('4-Sorted Characters')
        print('5-Palendrome Check')
        print('6-Randomise Characters')
        print('7-Hyphen Check')
        print('8-Names')
        print('9-Consonants')
        print('10-Vowels')
        print('11-Length')
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
