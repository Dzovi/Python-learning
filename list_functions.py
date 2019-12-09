# Working with lists

names = ["Sean", "Tom", "Eddie", "George", "Stephen", "Sean"]
nums = [4, 12, 27, 51, 32, 43]

# names.extend(nums) # merging two lists
names.append("Creed")  # adding item to the end of the list
names.insert(1, "Kevin")  # adding item on specific position, pushing others
names.remove("Eddie")  # removing element from list
# names.clear() # clearing the list
names.pop(1)  # poping an element from list
names.sort()  # sorting list in order
nums.sort() 
nums.reverse()  # reversing the list
print("Nums: " + str(nums))
print("Names: " + str(names))
print("Searching for specific element: " + str(names.index("Tom")))
print("Counting same strings: " + str(names.count("Sean")))

names2 = names.copy()
print("Copying names1 to names2: " + str(names2))
