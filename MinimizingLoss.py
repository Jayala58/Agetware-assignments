'''
This optimized code helps Rajeev minimize financial loss when buying and selling a house by analyzing projected prices over the years. It uses sorting and indexing to efficiently find the smallest loss where buying happens before selling. The approach improves performance from O(n²) to O(n log n), making it scalable.
'''
def min_loss(prices):
    n = len(prices)
    price_to_year = {price: i for i, price in enumerate(prices)}
    
    sorted_prices = sorted(prices, reverse=True)
    
    min_loss = float('inf')
    buy_year = sell_year = -1

    for i in range(len(sorted_prices) - 1):
        p1 = sorted_prices[i]
        p2 = sorted_prices[i+1]
        if price_to_year[p2] > price_to_year[p1]:
            loss = p1 - p2
            if loss < min_loss:
                min_loss = loss
                buy_year = price_to_year[p1] + 1
                sell_year = price_to_year[p2] + 1

    if min_loss == float('inf'):
        return "No valid loss found...!!!"
    else:
        return f"Buy in year {buy_year}, sell in year {sell_year}, loss = {min_loss}"
prices = list(map(int,input().split()))
print(min_loss(prices))
