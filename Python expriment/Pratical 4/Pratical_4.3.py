# Student Marks Statistics 
import math
m1 = float(input("Enter marks of Subject 1: ")) 
m2 = float(input("Enter marks of Subject 2: ")) 
m3 = float(input("Enter marks of Subject 3: ")) 
total = m1 + m2 + m3 
average = total / 3 
print("\n----- Result -----") 
print("Total Marks :", total) 
print("Average     :", average) 
print("Maximum     :", max(m1, m2, m3)) 
print("Minimum     :", min(m1, m2, m3)) 
print("Square Root of Total :", math.sqrt(total))