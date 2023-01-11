# Naive Approch to solve buy and sell stock in o(n2) timem


def buySellStock(array):
    res = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] > array[i]:
                profit = array[j] - array[i]
                res = max(res, profit)
    return res


array = [7, 1, 5, 3, 6, 4]


# buySellStock(array)


# Sliding Window approch to find the best time to buy and sell


def buySellStockSliding(prices):

    l, r = 0, 1

    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)

        else:
            l += 1

        r += 1
    return maxP


sales = [7, 1, 5, 3, 6, 4]

buySellStockSliding(sales)


# Will be working on this now
