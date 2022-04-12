coins = [50, 20, 10, 5, 1]
def change(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for higher in range(coin, amount + 1):
            ways[higher] += ways[higher - coin]
    return ways[amount]

'''import random
coins = [50, 20, 10, 5, 1]
listofpossibilities = []
count = 0
def waystogetadollar():
    global coins
    global listofpossibilities
    global count
    total = 0
    hmm = []
    while total < 100:
        number = random.choice(coins)
        if number + total < 100:
            total += number
            hmm.append(number)
    print(hmm)
    count += 1
    print(str(count) + 'possibilities')'''