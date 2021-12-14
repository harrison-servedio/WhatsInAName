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
        for i in self.val:
            i = string2(i)
            if i.MyLower() in letters:
                frequency.insert(letters.index(i.MyLower()), frequency[letters.index(i.MyLower())] + 1) 
            
        return f'There are {frequency[0]} a(s) \nThere are {frequency[1]} e(s) \nThere are {frequency[2]} i(s) \nThere are {frequency[3]} o(s) \nThere are {frequency[4]} u(s)\n'
            
    def consonants(self):
        letters = 'bcdfghjklmnpqrstvwxyz'
        frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in self.val:
            i = string2(i)
            if i.MyLower() in letters:
                frequency.insert(letters.index(i.MyLower()), frequency[letters.index(i.MyLower())] + 1) 
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
        lastLetter = 'asdfeaowiunfd'
        TwoBackLetter = 'afuweiaoduscvierqw'
        for letter in self.MyLower():
            if letter == 'a' and lastLetter == 'i':
                TwoBackLetter = lastLetter
                lastLetter = letter
                sylableCounter += 1
                continue
            elif letter == 'o' and lastLetter == 'e':
                TwoBackLetter = lastLetter
                lastLetter = letter
                sylableCounter += 1
                continue
            elif letter == 'o' and lastLetter == 'i':
                TwoBackLetter = lastLetter
                lastLetter = letter
                sylableCounter += 1
                continue
            elif letter == 'e' and lastLetter == 'i':
                TwoBackLetter = lastLetter
                lastLetter = letter
                sylableCounter += 1
                continue
            elif letter == 'a' and lastLetter == 'u':
                TwoBackLetter = lastLetter
                lastLetter = letter
                sylableCounter += 1
                continue
            elif lastLetter in 'aeiouy':
                TwoBackLetter = lastLetter
                lastLetter = letter
                continue
            elif (letter == 'e' == self.MyLower()[-1] and TwoBackLetter in 'aeiou'):
                TwoBackLetter = lastLetter
                lastLetter = letter
                continue
            elif letter in 'aeiouy':
                TwoBackLetter = lastLetter
                lastLetter = letter
                sylableCounter += 1
                continue
            else:
                TwoBackLetter = lastLetter
                lastLetter = letter
                continue
        return sylableCounter
    
    def menu(self):
        print('\nHere you will be able to select a function. The the number that corresponds to the function you want.')
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
        x - input('12-Reverse')
        while True:
            try:
                x = int(x)
                break
            except:
                print('That input is not valid.')

x = string2()
        
while True:            
    x = string2(input("Test: "))
    print(x.sylables())
