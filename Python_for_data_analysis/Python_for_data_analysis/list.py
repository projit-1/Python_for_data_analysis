# list1 = ["aam", "jam", "kola", "lichu", "pepe"]
# # print(list1)
# # print(type(list1))
# # print(len(list1))
# # print(list1[0])

# #The list() Constructor

# list2 = list(("aam", "jam", "kola", "lichu", "pepe"))
# # #print(list2)
# # print(list2[0])
# # print(type(list2))
# # print(len(list2))


# list3 = ["apple", "banana", "cherry"]
# if "apple" in list3:
# #   print("Yes, 'apple' is in the fruits list")

# list4 = ["apple", "banana", "cherry"]
# list4[0] = "blackcurrant"
# # print(list4)


# list5 = ["apple", "banana", "cherry"]
# list6 = ("Ford", "BMW", "Volvo")
# list5.extend(list6)
# # print(list5)


# # loops in list

# list7 = ["apple", "banana", "cherry"]
# for x in list7:
# #    print(x)

# list8 = ["apple", "banana", "cherry"]
# i = 0
# while i < len(list8):
#   #print(list8[i])
#   i = i + 1

# list9 = ["aam", "jam", "kala", "lichu", "pepe"]
# i = 0
# while i< len(list9):
#     #print(list9[i])
#     i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# list1 = ["apple", "banana", "cherry"]
# [print(x) for x in list1]

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

#List Comprehension

# list = ["apple", "banana", "cherry"]
# newlist = []
# for x in list:
#     if "y" in x:
#         newlist.append(x)
#         print(newlist)
      

# list = ["apple", "banana", "cherry"]
# newlist = [ x for x in list if 'a' in x ]
# print(newlist)


# list = ["paka aam", "jam", "kala", "lichu", "pepe", "kacha aam"]
# # newlist= [x for x in list if "k" in x]
# newlist = [x for x in list if x != "kacha aam"]
# print(newlist)

# list = ["paka aam", "jam", "kala", "lichu", "pepe", "kacha aam"]
# list.sort(reverse=True)
# print(list)



