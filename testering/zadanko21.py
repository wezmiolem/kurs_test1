import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42) 
sales = np.random.randint(50, 200, size=(6, 30))
print(sales)

first_7_avg = sales[:, :7].mean(axis=1)
last_7_avg = sales[:, -7:].mean(axis=1)
trend = last_7_avg - first_7_avg


week1 = sales[:, 0:7].sum()
week2 = sales[:, 7:14].sum()
week3 = sales[:, 14:21].sum()
week4 = sales[:, 21:28].sum()

weeks_sums = [week1, week2, week3, week4]
best_week_idx = np.argmax(weeks_sums)
best_week_val = weeks_sums[best_week_idx]


print("Sales Trend per Product (Last 7 vs First 7 avg):")
for i, t in enumerate(trend):
    print(f" Product {i+1}: {t:.2f}")

print(f"\nBest Week: Week {best_week_idx + 1} with total sales of {best_week_val}")


plt.figure(figsize=(12, 6))
for i in range(sales.shape[0]):
    plt.plot(sales[i], label=f'Product {i+1}')

plt.title('Product Sales Over 30 Days')
plt.xlabel('Day')
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()