# 4. Write a program that takes a list of numbers and prints the prime numbers from the list.


num = list(range(1,100))

for n in num:
    if n < 2:
        continue  
    is_prime = True  
    for i in range(2, n): 
        if n % i == 0:
            is_prime = False
            break 
    if is_prime:
        print(f" {n} is prime number:\n")