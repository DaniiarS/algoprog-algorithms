def counter(n: int, k: int) -> int:
    players = [False] * n
    start = 0

    while(True):
        stop = (start + k%n - 1) % n
        if players[stop]:
            break
        players[stop] = True
        start = (stop + 1) % n
    
    count = 0
    for player in players:
        if not player:
            count += 1
    
    return count


n, k = map(int, input().split())
print(counter(n, k))

