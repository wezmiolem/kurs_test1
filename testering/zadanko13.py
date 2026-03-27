sales = [1200, 1350, 1290, 1480, 1520, 1510, 1680, 1720, 1700, 1890, 1950, 2100]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for i in range(1, len(sales)):
    diff = sales[i] - sales[i-1]
    if diff > 0:
        percentage_increase = diff / sales[i-1]
        print(f"{sales[i]} - {months[i]} - increase {percentage_increase:.2%}")