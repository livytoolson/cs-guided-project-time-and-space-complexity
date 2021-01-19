"""
Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.

Examples:
csSortedTwoSum([3,8,12,16], 11) -> [0,1]
csSortedTwoSum([3,4,5], 8) -> [0,2]
csSortedTwoSum([0,1], 1) -> [0,1]

Notes:
Each input will have exactly one solution.
You may not use the same element twice.
[execution time limit] 4 seconds (py3)

[input] array.integer numbers
[input] integer target
[output] array.integer
"""

# def csSortedTwoSum(numbers, target):
#     # get indexes of numbers list
#     for i in range(len(numbers)):
#         for j in range(i, len(numbers)):
            
#             # if number at index i + number at index j is equal to target
#             if numbers[i] + numbers[j] == target:
                
#                 # return index i and index j
#                 return [i, j]

# def csSortedTwoSum(array, targetSum): 
# 	nums = {}; 
# 	for num in array: 
# 		potentialMatch = targetSum - num; 
# 		if potentialMatch in nums: 
# 			return [potentialMatch, num]; 
# 		else: 
# 			nums[num] = True; 
# 	return []; 

def csSortedTwoSum(numbers, target):
    for n in numbers:
        for m in numbers:
            if n + m == target:
                return [numbers.index(n), numbers.index(m)]

print(csSortedTwoSum([3,8,12,16], 11))
print(csSortedTwoSum([3,4,5], 8))
print(csSortedTwoSum([0,1], 1))