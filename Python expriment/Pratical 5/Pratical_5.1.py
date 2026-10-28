# Binary Search Using Strings
names = ["Amit", "Neha", "Priya", "Rahul", "Sneha"]
search = input("Enter name to search: ")

low = 0
high = len(names) - 1

while low <= high:
    mid = (low + high) // 2
    if names[mid] == search:
        print("Name found at position", mid + 1)
        break
    elif search > names[mid]:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Name not found")