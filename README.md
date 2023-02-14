# Future Capital Coding Interview

This repository is created for the ProNvest coding interview. The tasks are solved in Python.

##  Part  1  -  Calculate  the  total  value  of  a  stock  portfolio

A sample stock portfolio is passed in as an argument to a console application. The application parses the input, lookup the current stock price from the sample stocks.json feed file, and then return the total value of the portfolio.

### Input

`-part1 [<TICKER>:<QUANTITY>]`

### Output

`<TOTAL>`

###  Test Cases

1) `python3 app.py -part1 "FB:12,PLTR:5000"  =>  119887.4`

2) `python3 app.py -part1 "BABA:1,TSLA:5,WISH:1200"  =>  9891.9`

## Part 2 - Maximize profits

Given a list of `prices` where `prices[i]` is the price of a given stock on the `ith` day, try to maximize the profit by choosing a single day to buy one stock and choosing one different day to sell in the future. Return the maximum profit that the client can achieve from this transaction. If the client cannot achieve any profit, then return 0.

### Input

`-part2 [<PRICE>]`

### Output

`<PROFIT>`

### Test Cases

1) `python3 app.py -part2 "7,1,5,3,6,4"  =>  5` 

* In this example, you would buy on day 2 (price = 1) and sell on day 5 (price = 6) for a profit of 5.

2) `python3 app.py -part2 "7,6,4,3,1"  =>  0`

* In this example, no buy or sells are performed.
