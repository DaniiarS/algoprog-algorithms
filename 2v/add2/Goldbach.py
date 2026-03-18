def sieve(N: int) -> list[bool]:
    primes = [True] * (N +1)
    
    primes[0] = primes[1] = False
    primes[2] = True

    k = 2
    while k <= N//k + 1:
        for i in range(k*k, N, k):
            primes[i] = False
        k += 1
    
    return primes
    
    

def Goldbach(num: int) -> tuple:
    primes = sieve(num)
    result = tuple()

    for i in range(num):
        if primes[i] and (primes[num - i]):
            result = (i, num - i)
    
    return result

num = int(input())
result = Goldbach(num)
print(result[0], result[1])