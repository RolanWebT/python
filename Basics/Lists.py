"""
There are 4 built-in data types in 
Python used to store collections of data:
    1. List: ordered and changeable. Allows duplicate members.
    2. Tuple: which is ordered and unchangeable. Allows duplicate members.
    3. Set: unordered, unchangeable*, and unindexed. No duplicate members.
    4. Dictionary: ordered(V 3.7) and changeable. No duplicate members.
"""

# List 
myList = ["banana", "apple", "cherry", "orange", "kiwi", "melon", "mango"]
print("myList:\n",myList)
print("myList[1]: ", myList[1])

# len() function
print("Has the length:", len(myList))

print("Type:", type(myList))

# List Constructor: list()

# Check if Item Exists
# if "item" in myList:
#    print
if "apple" in myList:
    print("Yes, Apple is in the List")

# Change items in a List
myList[1:3] = ["new", "new"]
print("\n changed List [1:3]:\n ",myList)
# NOTICE 
# myList[1:2] = ["blackcurrant", "watermelon"] 
# will change the second item with two new items!!

""" Add items to a List Methods: """
# 1. insert(index, "item"): 

# insert an item in a specific index
myList.insert(2, "watermelon")
print("\n insert a new item in the third index:\n", myList)

# 2. append("item")

# 3. extend(another list)
newList = ["mango", "papaya"]
myList.extend(newList)
print("\n Extend a List:\n", myList)


""" Remove From a List """
# 1. .remove("item") // will remove ONLY the first matched item
myList.remove("new")
print("\n Remove first 'new':\n", myList)
# 2. .pop(index)
myList.pop(1)
print("\n Remove the second item [1]:\n", myList)
#  .pop() remove the last item
myList.pop()
print("\n Remove the last item:\n", myList)

# 3. del Keyword
del myList[3] # delete the fourth item
print("\n delete the fourth item with 'del' :\n", myList)
del myList # delete the entire List 
# print(type(myList))

# 4. .Clear() will clear the List but it still remain
