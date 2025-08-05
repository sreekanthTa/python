list_items = [ 5,9,1,2]

# ITERATORS:
# An iterator is an object that implements the iterator protocol, consisting of the methods __iter__() and __next__().
# An iterator allows you to traverse through all the elements in a collection (like a list)
# Using iter() to create an iterator from a list
# Using next() to get the next item from the iterator

# Example of an iterator
iterator = iter(list_items)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# GENERATORS:
def test_generator():
    for item in list_items:
        yield item

# Using the generator
gen = test_generator()
print(next(gen))  # Output: 5
print(next(gen))  # Output: 9
print(next(gen))  # Output: 1