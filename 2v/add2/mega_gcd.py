def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a%b
    
    return a


def mega_gcd(nums: list[int]) -> int:
    size = len(nums)

    result = 0
    for i in range(size):
        result = gcd(result, nums[i])
    
    return result


N = int(input())
nums = list(map(int, input().split()))

print(mega_gcd(nums))