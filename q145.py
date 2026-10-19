def profit_percentage(cost_price,selling_price):
    profit = selling_price - cost_price
    percentage = (profit/cost_price)*100
    return percentage
print(profit_percentage(800,920))
