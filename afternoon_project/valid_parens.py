"""
You are given a parentheses sequence, check if it's regular.

Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string, consisting only of '(' and ')'.

Guaranteed constraints:
0 ≤ s.length ≤ 105.

[output] boolean

true is the sequence is regular and false otherwise.
"""

def validParenthesesSequence(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in s:
        
        if char in mapping:
            
            if stack:
                top_elem = stack.pop()
            else:
                top_elem = "#"
                
            if mapping[char] != top_elem:
                return False
        else:
            stack.append(char)
        
    return not stack