#Working with strings and numbers

from math import *

word = "smh"
num = 5

print(word.upper().isupper())
print("Lenght of string: " + str(len(word)))
print("Looking for word on index: " + word[1])
print("On which index is the word: " + str(word.index("h")))
print("Replacement of strings: " + word.replace("h", "th"))
print("Printing nums with strings: " + str(num) + "!")
print("Power: " + str(pow(3, 2)))
print("Max from nums: " + str(max(4, 23)))
print("Min from nums: " + str(min(21, 13)))
print("Round num: " + str(round(3.3)))
print("Deleting decimal: " + str(floor(3.7)))
print("Going on higher num: " + str(ceil(3.7)))
print("Square num: " + str(sqrt(16)))
