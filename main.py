def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n + 1)]
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

num = int(input("Введите натуральное число: "))
result = sieve_of_eratosthenes(num)

print(f"Простые числа до {num}: {result}")
