print("hello world")

itemslist = [1, 2, 3, 4, 5]

# for item in  itemslist:
#     print(item)



# for item in range(1,6):
#     print(item)
#     if(item==1):
#         print("Item is 1, breaking the loop")
#         break
# else:
#     print("Loop completed successfully")




# for item in range(6,1,-3):
#     print(item)


while itemslist:
    # if(itemslist.__len__() == 3):
    #       print("List has 3 items, breaking the loop")
    #       break
    if(itemslist.__len__() == 1):
          print("List has 1 item, continuing the loop")
          itemslist.pop()
          continue
           
    print(itemslist.pop())