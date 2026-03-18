def factorize(num:int) -> dict:
    if num == 1:
        return {1:1}
    
    k = 2
    factors = dict()

    while k <= num / k:
        if num % k == 0:
            if k not in factors:
                factors[k] = 1
            else:
                factors[k] += 1
            num //= k
            continue
        k += 1
    
    if num > 1:
        if num in factors:
            factors[num] += 1
        else:
            factors[num] = 1

    return factors

def min_divisor(num:int) -> int:
    N = 1
    A_divisors = factorize(num)

    min_divisor = 1
    for i in range(1, num + 1):
        N_divisors = factorize(i)
        found = False

        for A_base, A_exponent in A_divisors.items():
            if A_base in N_divisors.keys():
                if N_divisors[A_base] * i >= A_exponent:     
                    found = True
                else:
                    found = False
                    break
            else:
                found = False
                break
        
        if found:
            min_divisor = i
            return min_divisor
        
A = int(input())
print(min_divisor(A))