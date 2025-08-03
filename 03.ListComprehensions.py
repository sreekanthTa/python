# List comprehensions are only the specific pattern that builds a new list using:
list_num = [1, 2, 3, 4, 5]


# List Comprehensions are a concise way to create lists in Python.
# [expression for x in iterable if condition]

squared_list = [x**2 for x in list_num if x %2 == 0]
print("Squared list of even numbers:", squared_list)
#  [4, 16]



inner_list = [ (x,y) for x in list_num for y in list_num]
print("Inner list with tuples of all combinations:", inner_list)

#  [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), 
#   (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), 
#   (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), 
#   (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), 
#   (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]