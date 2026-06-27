friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry") # append() function is used to add an element at the end of the list.
print(friends)

l1 = [1, 34,62, 2, 6, 11] #here also the indexing starts from 0. So the index of 1 is 0, index of 34 is 1, index of 62 is 2 and so on.
# l1.sort() 
# l1.reverse() 
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
value = l1.pop(3) # will delete element at a particular index and return the deleted value. Here it will delete the element at index 3 which is 2 and return it.
print(value)
print(l1)

#remove() function is used to remove an element from the list. It will remove the first occurrence of the element in the list. If the element is not found, it will raise a ValueError.
