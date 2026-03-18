def factorize(N: int) -> dict:
    k = 2
    factors = dict()
    while k <= N/k:
        if N % k == 0:
            N = N // k

            if k not in factors:
                factors[k] = 1
            else:
                factors[k] += 1
            
            continue
        k += 1

    if N > 1:
        if N in factors:
            factors[N] += 1
        else:
            factors[N] = 1
    
    
    return factors




N = int(input())
print(factorize(N))