# Space complexity -- how much memory does the algorithm use?

# Space complexity *includes* the original data
# Auxiliary Space Complexity does not include the original data
def foo(a):
    b = a.copy()    # O(n) aux space complexity over the length of a

foo([1,2,3,4])
foo([1,2,3,4,5,6,7,8])

#--------------------------------------------------------------------------#

def bar(a):
    x = a[0]        # O(1) aux space complexity over the length of a
    return x * 2

bar([1,2,3,4])
bar([1,2,3,4,5,6,7,8])