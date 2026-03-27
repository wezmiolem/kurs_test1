import math

list_of_primes = []

for n in range(2, 101):
    is_prime = True  
    if n > 2 and n % 2 == 0:
        is_prime = False
    else:
        for i in range(3, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break 
    
    if is_prime:
        list_of_primes.append(n)

print(f"{list_of_primes}, count {len(list_of_primes)}")