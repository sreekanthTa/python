# def func_one(obj):
#     try:
#       print("hello", int("je"))
     
#     except ValueError as err:
#         print("ValueError", err)
#         raise
#     except Exception as ee:
#         print("Eception",ee)   

# obj = {"name":"krish", "age":10}
# try:

#   func_one(obj)
# except Exception as ee:
#    print("Partnetas",ee)

obj = {"name":"krish", "age":10}
# obj["gs"] = "haris"
# del obj["gs"]
# print(obj["name"])
# print(obj.get("g"), obj)

# class test:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

# test_person = test("krish",10)
# print(test_person)
# obj1 = {"test":"test"}
# obj.update(obj1)
# for key, val in obj.copy().items():
#     print("Key and Val", key, val)

# print(obj.pop("asd","no val"))
# print(obj.popitem())
# print(obj)

keys = ["one", "two"]
print(dict.fromkeys(keys))