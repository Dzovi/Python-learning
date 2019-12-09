# Working with lists

names = ["Sean", "Tom", "Eddie", "George", "Stephen"]

print("List: " + str(names))
print("Name on index 1: " + names[1])
print("N on index -2 from back: " + names[-2])
print("Names from index 1 to end: " + str(names[1:]))
print("Grabing strings on index 1 and 2: " + str(names[1:3]))

names[1] = "Jim"
print("Changing name on index 1: " + names[1])
