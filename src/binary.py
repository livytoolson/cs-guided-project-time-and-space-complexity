def searc(name, lst):
    for elem in lst:        # O(n) over the length of lst
        if name == elem:    # O(m) over the lengths of the compared strings
            return True

    return False

# O(n*m) where n is the length of the list, and m is the length of the strings in the list

# binary search -- open the book and decide if you need to go earlier or later in the list, move to that half (left or right), etc until you find the thing you want

# ** when you cut the space in half, hints that it's 0(log(n)) **

# each step of the way we cut our data set in half --> 

# 100000
# 50000
# 25000
# 12500
# 6250
# 3125
# 1563
# 781
# 390
# 195
# 97
# 48
# 24
# 12
# 6
# 3
# 1

# 100000 names, 16 comparisons

def foo(n):
    for i in range(math.sqrt(n)):
        print(i)