#Random Password Generator
import random 
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234 56789" 
length = int(input("Enter password length: ")) 
password = "" 
for i in range(length): 
    password += random.choice(characters) 
    print("\nGenerated Password :", password)