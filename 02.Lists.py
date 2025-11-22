# list_num = [1,2,3,5,8,9]

# print(list_num)

# # Accessing list items
# print("Accessing list items", list_num[0], list_num[-1])


# # Insert, Append, Extend, Clear, Pop, Remove, Index, Count, Sort, Reverse, Join
# print("Append, Insert and Remove Items of list items", list_num)

# # Insert adds an item at a specific index
# list_num.insert(2, 4) # Rigth Shift After Insertion of an element at index 2
# list_num[2]=5 # Override the value at index 2
# print("After insert, the list items are", list_num)

# # Append adds an item to the end of the list
# list_num.append(10)
# print("After append, the list items are", list_num)

# # Extend adds multiple items to the end of the list
# list_num.extend([11, 12])  # Extend adds multiple items to the end of the list
# print("After extend, the list items are", list_num)

# # Clear removes all items from the list
# list_num.clear()
# print("After clear, the list items are", list_num)

# list_num = [1, 2, 3, 4, 5]
# print("Reinitialized list items", list_num)

# # Pop removes and returns the last item from the list
# list_num.pop()

# # Remove the first occurrence of 5
# # If the item is not found, it raises a ValueError
# try:
#    list_num.remove(5) 
# except ValueError:
#    print("5 is not in the list")

# print("After remove, the list items are", list_num)



# # Index returns the index of the first occurrence of an item
# # If the item is not found, it raises a ValueError
# try:
#     index_of_2 = list_num.index(2)
#     print("Index of 2 in the list is", index_of_2)  
# except ValueError:
#     print("2 is not in the list")


# # Count returns the number of occurrences of an item in the list
# count_of_3 = list_num.count(3)
# print("Count of 3 in the list is", count_of_3)

# # Sort sorts the list in ascending order
# list_num.sort()
# print("After sort, the list items are", list_num)

# # Reverse reverses the order of the list
# list_num.reverse()
# print("After reverse, the list items are", list_num)

# # Join converts the list to a string with a specified separator
# # this is not a list method in Python, it’s a string method!

# list_str = ", ".join(map(str, list_num))
# print("Joined list items as string:", list_str)


# class Person:
#     def __init__(self):
#         self.name= "test"
#         self.age = 10
#         self.area ="testarea"

# p =  Person()

# print("getAtr", getattr(p, "name","default"), p.name, p.age)
# p.test="extra"
# print("setAttr",setattr(p, "et","test"))
# print("hasAttr", hasattr(p,"name"), "name" in p.__dict__, p.__dict__)
# delattr(p, "area")
# print("delAttr", p.__dict__)

# print("vars", vars(p), dir(vars))
 

#Global Variable
x = 10

def test():
    global x
    print(x)
    x=5


test()
