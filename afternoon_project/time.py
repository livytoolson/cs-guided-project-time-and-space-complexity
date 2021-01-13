def do_lots_of_things(items):
    last = len(items) - 1   # O(1) over the number of items

    print(items[last])      # O(1)

    middle = len(items) / 2 # O(1)

    i = 0                   # O(1)

    while i < middle:       # O(n/2) == O(1/2 * n) == O(n)
        print(items[i])         # O(1)
        i += 1                  # O(1)
    
    for num in range(100):  # O(100) == O(100 * 1) == O(1)
        print(num)              # O(1) -- this line is going to run 100 times no matter how many items are passed in