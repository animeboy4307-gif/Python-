#Mathematical Operations using math Module
import math  
num = float(input("Enter a number: ")) 
square_root = math.sqrt(num) 
square = math.pow(num, 2) 
cube = math.pow(num, 3) 
ceiling = math.ceil(num) 
floor = math.floor(num) 
print("\n----- Mathematical Operations -----") 
print("Square Root :", square_root) 
print("Square :", square)   
print("Cube :", cube) 
print("Ceiling     :", ceiling) 
print("Floor       :", floor)  
if num >= 0 and num.is_integer():
    print("Factorial   :", math.factorial(int(num))) 
else: 
    print("Factorial   : Not possible for decimal/negative numbers") 