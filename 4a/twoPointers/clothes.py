n = int(input())
shirts = list(map(int, input().split()))

m = int(input())
pants = list(map(int, input().split()))

i, j = 0, 0
result = ()

optimalSum = 1e7
while i < n and j < m:
    
    if abs(shirts[i] - pants[j]) < optimalSum:
        optimalSum = abs(shirts[i] - pants[j])
        result = (i,j)
    
    if shirts[i] < pants[j]:
        i += 1
    else:
        j += 1

        
print( shirts[ result[0] ] , pants[ result[1] ] )