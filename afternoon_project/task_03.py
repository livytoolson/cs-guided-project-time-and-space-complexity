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

def csFirstUniqueChar(input_str):
    for s in input_str:
        if input_str.count(s) == 1:
            return input_str.index(s)
    return -1

print(csFirstUniqueChar(input_str = "lambdaschool"))
print(csFirstUniqueChar(input_str = "ilovelambdaschool"))
print(csFirstUniqueChar(input_str = "vvv"))

# find character with a frequency of 1
# traverse through input string 
# use .count() method
# if count is > 1, return -1
# return index of first character with a count of 1