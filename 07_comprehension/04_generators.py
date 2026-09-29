daily_sales = [10, 20, 30, 40, 50]

# total_sales = sum(daily_sales) Little inefficient

# More efficient because we don't need to store all the values in memory at once. It is like streaming the data one by one
total_sales = sum(daily_sale for daily_sale in daily_sales)
print(total_sales)
