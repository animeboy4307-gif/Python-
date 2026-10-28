# Random Number Generator 
import random 
lower = int(input("Enter lower limit: ")) 
upper = int(input("Enter upper limit: ")) 
random_integer = random.randint(lower, upper) 
random_float = random.uniform(lower, upper) 
print("\n----- Random Numbers -----") 
print("Random Integer :", random_integer) 
print("Random Float   :", random_float)