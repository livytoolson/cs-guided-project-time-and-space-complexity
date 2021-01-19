"""
Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

Examples:
csFirstUniqueChar(input_str = "lambdaschool") -> 2
csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
csFirstUniqueChar(input_str = "vvv") -> -1

Notes:
input_str will only contain lowercase alpha characters.
[execution time limit] 4 seconds (py3)
[input] string input_str
[output] integer
"""

# find character with a frequency of 1
# traverse through input string 
# use .count() method
# if count is > 1, return -1
# return index of first character with a count of 1

def csFirstUniqueChar(input_str):
    for s in input_str:
        if input_str.count(s) == 1:
            return input_str.index(s)
    return -1

print(csFirstUniqueChar(input_str = "lambdaschool"))
print(csFirstUniqueChar(input_str = "ilovelambdaschool"))
print(csFirstUniqueChar(input_str = "vvv"))

# def csFirstUniqueChar(input_str):
#     for letter in input_str:
#         li = input_str.find(letter) + 1
#         if letter not in input_str[li:]:
#             return input_str.find(letter)
#     return -1

import nump as nump
def csFirstUniqueChar(input_str):
    y = list(input_str)
    x = np.unique(y, return_index=True, return_counts=True)
    z = []
    for i, j enumerate(x[2]):
        if x[1][i] < z and j == 1:
            z = x[1][i]
        print (i, j, x[1][i])
    if z == 9999:
        z = -1
    return z

# could use a dictionary to keep track of the total of all the letters 
# take a second pass through the string  

# return -1 if z == 9999 else z
# return z == 9999 ? -1:z --> the Ternary Operator