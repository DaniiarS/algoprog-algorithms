days, initial_amount = map(int, input().split())
asks = list(map(int, input().split()))
bids = list(map(int, input().split()))

buy_day = -1
sell_day = -1
max_amount = initial_amount
trade_occured = False

for i in range(days):
    shares = initial_amount//asks[i]
    remainder = initial_amount - shares * asks[i]

    for j in range(i, days):
        current_amount = shares * bids[j]

        if current_amount > initial_amount and current_amount > max_amount:
            max_amount = current_amount + remainder
            buy_day, sell_day = i, j
            trade_occured = True

if trade_occured:
    print(max_amount)
    print(buy_day + 1, sell_day + 1)
else:
    print(initial_amount)
    print(buy_day, sell_day)