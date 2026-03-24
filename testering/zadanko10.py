transakcje = [
('2024-01-15', 'Elektronika', 1200),
('2024-01-15', 'Meble', 450),
('2024-01-16', 'Elektronika', 800),
('2024-01-16', 'Elektronika', 350),
('2024-01-15', 'Odzież', 200),
('2024-01-16', 'Meble', 600)
]

modified_transactions = {}

for date, category, value in transakcje:
    if date in modified_transactions:      
        if category in modified_transactions[date]:
            modified_transactions[date][category] += value
        else:
            modified_transactions[date][category] = value
    else:
        modified_transactions[date] = {category: value}

print(modified_transactions)