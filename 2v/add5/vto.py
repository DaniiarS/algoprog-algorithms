def gcd(a: int, b: int) -> int:
    while(b!=0):
        a, b = b, a%b
    return a

def count_squares(a: int, b: int, n: int) -> int:
    
    # total squares in a rectangular
    squares_rect = a * b
    crossed_squares = a + b - gcd(a, b)

    squares_triangular = (squares_rect - crossed_squares) // 2
    result = 0 if squares_triangular % n == 0 else n - squares_triangular % n

    return result

a, b, n = map(int, input().split())
print(count_squares(a, b, n))