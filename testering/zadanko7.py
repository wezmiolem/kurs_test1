transactions = [
('food', 50),
('transport', 20),
('food', 30),
('entertainment', 40),
('transport', 15),
('food', 25)
]

totals = {}

for category, amount in transactions:
    if category in totals:
        totals[category] += amount
    else:
        totals[category] = amount

print(totals)
