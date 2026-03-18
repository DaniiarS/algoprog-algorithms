import math

log2 = math.log2
ceil = math.ceil

def ceil_log_2(num: int) -> int:
    return ceil(log2(num)) - 1


def sequence(k: int) -> int:
    if k == 2:
        return 1
    elif k <= 1:
        return 0

    return (sequence(k - 2**ceil_log_2(k)) + 1) % 3
    

k = int(input())
print(sequence(k))