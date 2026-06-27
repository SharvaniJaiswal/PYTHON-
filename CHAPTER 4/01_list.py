friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4]) #last index is not included while printing the list. It will print the elements from index 1 to 3.

#here the main list is changed because lists are mutable in Python. The slicing operation returns a new list with the sliced elements, but it does not change the original list.

