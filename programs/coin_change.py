def coin_change1(coins_list, change):
    '''Recursive fucntion to calculate coin change

    This is very in-efficient as it qould require lot of function calls and does lot of
    duplciate work
    '''

    min_coins = change

    if change in coins_list:
        return 1
    else:
        for i in [c for c in coins_list if c <= change]:
            num_coins = 1 + coin_change1(coins_list, change-i)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


print(coin_change1([1, 5, 10, 25], 63))


def coin_change2(coins_list, change, known_results):
    '''This function extends above func coin_change1 by memoizing already known coins there by
    avoiding duplicate work. Essentially reduces # of function calls drastically.
    '''

    min_coins = change

    if change in coins_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coins_list if c <= change]:
            num_coins = 1 + coin_change2(coins_list, change-i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins

print(coin_change2([1, 5, 10, 25], 63, [0]*64))


def coin_change3(coinValueList, change, minCoins, coinsUsed):
    '''Dynamic programming technic'''

    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
        return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for", amnt, "requires")
    print(coin_change3(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()
