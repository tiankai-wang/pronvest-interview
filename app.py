import sys
import json

def part1(arg):
    f = open('stocks.json')
    data = json.load(f)
    prices = {}

    for stock in data:
        prices[stock['ticker']] = float(stock['close'])

    inputs = arg.split(',')
    total = 0.0

    for input in inputs:
        ticker = input.split(':')[0]
        quantity = int(input.split(':')[1])
        total += prices[ticker] * quantity
    
    print(total)

def part2(arg):
    prices = [int(x) for x in arg.split(',')]
    if len(prices) == 0:
        print(0)
        return

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    
    print(max_profit)

if sys.argv[1] == "-part1":
    part1(sys.argv[2])
elif sys.argv[1] == "-part2":
    part2(sys.argv[2])