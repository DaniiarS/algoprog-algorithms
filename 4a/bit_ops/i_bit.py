def main():
    a, i = map(int, input().split())

    print( (a >> i) % 2 )

if __name__ == '__main__':
    main()