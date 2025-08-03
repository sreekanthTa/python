# LAMBDA FUNCTIONS:
# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can take any number of arguments but can only have one expression.

#  Expression: lambda arguments: expression 
                
def add(x, y):
    return x + y

print("Add Numbers", add(1,2))

lambda_add = lambda x,y : x+y
print("Lambda Add Numbers", lambda_add(1,2))


#  In Javascript:
# const add = (x, y) => x + y;
# console.log(add(3, 5)); // 8


# SQUARE A NUMBER:
def square(x):
    return x**2

list_num = [1, 2, 3, 4, 5]
squared_list = map(square,list_num)

print("Squared List:", list(squared_list))  # Convert map object to list for display

squared_lambda_list =list(map(lambda x: x**2, list_num))
print("Squared List using Lambda:", squared_lambda_list)  # Convert map object to list for display


# FILTER:
# Filter is used to filter items from an iterable based on a condition.
# It returns an iterator that produces items from the iterable for which the function returns True.

def is_even(x):
    return x % 2 == 0

even_list = filter(is_even, list_num)
print("Even List:", list(even_list))  # Convert filter object to list for display

even_lambda_list = list(filter(lambda x: x %2 ==0 , list_num))

# ANY:
# Any returns True if at least one element of the iterable is True.
any_even = any(x % 2 == 0 for x in list_num)
print("Is there any even number in the list?", any_even)

# ALL:
# All returns True if all elements of the iterable are True.
all_even = all(x % 2 == 0 for x in list_num)
print("Are all numbers even in the list?", all_even)



# GENERATOR EXPRESSION AND SYS.GETSIZEOF:
# Generator:
def number_generator(n):
    for i in range(n):
        yield i
gen = number_generator(5)
print("Generator Output:")
for num in gen:
    print(num)

# Generator Expression:
squares_gen = (x * x for x in range(1000))
print("Generator Expression Output:")
for square in squares_gen:
    print(square)

# SYS.GETSZIEOF:

import sys

list_comp = [x * x for x in range(1000)]
gen_expr = (x * x for x in range(1000))

print(sys.getsizeof(list_comp))  # big size
print(sys.getsizeof(gen_expr))   # tiny size


# SORTED, ABS, MIN AND MAX:
# Sorted:
nums = [5, 1, 4, 2]
sorted_nums = sorted(nums)  # [1, 2, 4, 5]

# ABS 
abs_value = abs(-10)  # 10
print("Absolute value of -10:", abs_value)

# MinAndMax:
min([4, 2, 9])  # 2
max([4, 2, 9])  # 9


# SUM, ROUND
# SUM:
nums = [1, 2, 3, 4]
sum(nums)  # 10

# ROUND:
rounded_value = round(3.14159, 2)  # 3.14

# REVERSED:
nums = [1, 2, 3]
rev = reversed(nums)
print(list(rev))  # [3, 2, 1]

# ZIP:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]


# LENGTH:
# Length of a list
len("hello")         # 5
len([10, 20, 30])    # 3
len({"a": 1, "b": 2}) # 2
len(range(0, 10, 2)) # 5
