import json
from tqdm import tqdm

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in tqdm(range(2, int(limit ** 0.5) + 1), desc = "Generating Primes"):
        if sieve[i]:
            for j in tqdm(range(i * i, limit + 1, i), desc = "Step"): sieve[j] = False
    return [x for x in range(limit + 1) if sieve[x]]

def generate_primes_optimized(n):
    from math import log
    if n < 6: upper_limit = 15
    else: upper_limit = int(n * log(n) + n * log(log(n)))
    primes = sieve_of_eratosthenes(upper_limit)
    return primes[:n]

n = 10 ** 8
prime_numbers = generate_primes_optimized(n)
print(n, "nombres premiers sont generes avec succes.")

json.dump(prime_numbers, open("PRIMES.json", "w"))