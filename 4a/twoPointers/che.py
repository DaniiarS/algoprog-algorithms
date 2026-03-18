import time

n , k = map(int, input().split())
d = list(map(int, input().split()))

l, r = 0, 0
count = 0

while r < n:
    if d[r] - d[l] <= k:
        r += 1
    else:
        count += n - r
        l += 1
print(count)