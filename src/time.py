def foo(n):
    for i in range(n):
        print(i)

foo(10)     # 10 prints, if this takes a certain amount of time, 
foo(20)     # 20 prints, how much more time does this take? TWICE as long
foo(10000)  # 10000 prints

foo(n)      # n prints

0(n)        # "Order n" --> scales linearly

#--------------------------------------------------------------------------#

def bar(n):
    for i in range(n):      # this outer loop will run 10 times
        for j in range(n):  # this inner loop will run 10 x 10
            print(i, j)

bar(10)     # 100 prints
bar(20)     # 400 prints -- run time went up by 4 times
bar(10000)  # 100,000,000 prints

bar(n)      # n^2 prints

0(n^2)      # scales exponentially

#--------------------------------------------------------------------------#

def foo(a):
    for elem in a:      # O(n) over length of "a", n refers to the length of "a"
        print(elem)     

foo([1,2,3,4])
foo([1,2,3,4,5,6,7,8])  # if we double the elements we double the run time

#--------------------------------------------------------------------------#

def bar(a):
    print(a[0])         # O(1) over the length of "a", "constant time"

bar([1,2,3,4])          # no matter how long the list is, it will take the same time to run this
bar([1,2,3,4,5,6,7,8])

#--------------------------------------------------------------------------#

def baz(a):
    for i in range(10000000000):    # O(1) over the length of "a"
        print(a[0])                 

bar([1,2,3,4])
bar([1,2,3,4,5,6,7,8])
bar([1,2,3,4,5,6,7,8,9,10,11,12])   

# it takes the same amount of time to run regardless of the length of the list that is passed into the function

#--------------------------------------------------------------------------#

def qux(n):
    for i in range(n // 2):     # O(n/2) == O(1/2 * n) == O(n)
        print(i)

#--------------------------------------------------------------------------#
