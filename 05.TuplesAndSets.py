# Tuples:
# Think of them like immutable lists — once created, you can’t change them.
t=(1, 2, 3, 4, 5)
print("Tuple items:", t)
# Accessing tuple items
print("First item:", t[0])
# Tuples are immutable, so you cannot add or remove items
# t.append(6)  # This will raise an AttributeError


# Sets:
# Sets are unordered collections of unique items.
s = {1, 2, 3, 4, 5}
print("Set items:", s)
#Accessing items in a set is not possible like lists or tuples, as sets are unordered.
# However, you can check for membership
print("Is 3 in the set?", 3 in s)

# Adding items to a set
s.add(6)
print("Set after adding an item:", s)
# Removing items from a set
s.remove(2)  # Raises KeyError if item not found
print("Set after removing an item:", s)
# Looping through a set
for item in s:
    print("Set item:", item)
# Set operations
s2 = {4, 5, 6, 7}   
print("Union of sets:", s.union(s2))  # Union
print("Intersection of sets:", s.intersection(s2))  # Intersection
print("Difference of sets:", s.difference(s2))  # Difference
# Set comprehensions
squared_set = {x**2 for x in s if x % 2 == 0}
print("Squared set of even numbers:", squared_set)
# Accessing a value using the key
# name = s.get("name")  # Using get() to avoid KeyError if key doesn't exist
area = s.get("area", "Not specified")  # Default value if key not found    