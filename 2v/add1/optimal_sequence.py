def converter(i: int, j: int) -> int:
    num = j
    power = 0
    while(num != 0):
        num = num // 10
        power += 1
    
    return i * (10**power) + j

def is_prime(N: int) -> bool:
    k = 2

    while(k <= N//k + 1):
        if N % k == 0:
            return False
        k += 1

    return True

def max(a: int, b: int) -> int:
    if a > b:
        return a
    
    return b

def optimal_sequence(N: int) -> int:    
    dp = []

    # initialize dp
    for i in range(N): 
        line = [0 for j in range(N)]
        dp.append(line)

    # calculate max primes in the route
    for i in range(N):
        for j in range(N):

            if is_prime( converter(i + 1, j + 1) ):
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + 1
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    dp[i][j] = max(dp[i][j -1], dp[i - 1][j]) + 1
            else:
                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i -1][j])

    return dp[-1][-1] - 1

N = int(input())
print(optimal_sequence(N))