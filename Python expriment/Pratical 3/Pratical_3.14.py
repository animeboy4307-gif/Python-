# Search a Number Using break
numbers = [12, 25, 36, 48, 59, 63] 
search = int(input("Enter number to search: ")) 
for num in numbers: 
    if num == search: 
        print("Number Found") 
        break 
    else: 
        print("Number Not Found")