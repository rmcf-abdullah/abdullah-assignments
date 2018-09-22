# NAME: Abdullah Qamaruzzaman
# DATE: September 22, 2018

import re

# A regular expression (or RE) specifies a set of strings that matches it;
# the functions in this module let you check if a particular string matches a given regular
# expression (or if a given regular expression matches a particular string, which comes down to
# the same thing).

def main():


    def pal (): #defining function

        userInput = str(input("Enter a word to test and see if it qualifies as a palindrome: ")) # retreiving user input
        userInput = re.sub(r"\s+", "", userInput) # removes spaces # referenced https://stackoverflow.com/questions/3739909/how-to-strip-all-whitespace-from-string

        tempString = userInput[::-1] # storing the reverse if the user input
# Referenced https://www.youtube.com/watch?v=WBRpLjshGwI to determine how to reverse string

        if (userInput == tempString): # check to see if the reverse results in the same, in that case the if statement runs
            print("It's a palindrome!!") # prints corresponding response
        
        else: #else
                print("Sorry not a palindrome  ") # prints corresponding response 

    pal()


main()


