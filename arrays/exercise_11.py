# Maximise profit as per stock buy and sell
price_list = [7, 4, 6, 7, 5, 9, 9, 2, 8]


def get_maximum_profit(stock_list):
    if not stock_list:
        return -1
    buy_one_index = 0
    max_profit = -1
    for (index, number) in enumerate(stock_list):
        diff_price = number - stock_list[buy_one_index]
        if diff_price < 0:
            buy_one_index = index
        elif diff_price > max_profit:
            max_profit = diff_price
    return max_profit


result = get_maximum_profit(price_list)
print(result)
