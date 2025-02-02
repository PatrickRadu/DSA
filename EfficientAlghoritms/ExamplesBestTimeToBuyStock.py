#Best time to buy a stock
import random


#BF
def best_profit(prices):
    n=len(prices)
    best=0
    for i in range(n):
        for j in range(n):
            best=max(best,prices[j]-prices[i])
    return best

#O(N^2) 2 LOOPS
def best_profit(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        min_price = min(prices[0:i+1])
        best = max(best, prices[i] - min_price)
    return best
#O(N^2) FOR LOOP O(N) + Slice operator O(N) - hidden

def best_profit_fst(prices):
    n=len(prices)
    best=0
    min_price=prices[0]
    for i in range(n):
        min_price=min(min_price,prices[i])
        best=max(best,prices[i]-min_price)
    return best
#O(N)

#Testing
# while True:
#     n=random.randint(1,20)
#     prices=[random.randint(1,10)for i in range(n)]
#     results_brute=best_profit(prices)
#     results_fast=best_profit_fst(prices)
#     print(prices,results_brute,results_fast)
#     if  results_brute!=results_fast:
#         print("ERROR")
#         break
