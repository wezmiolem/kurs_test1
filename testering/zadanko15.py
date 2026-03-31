transakcje = [
{"produkt": "laptop", "wartosc": 2999},
{"produkt": "mysz", "wartosc": 89},
{"produkt": "laptop", "wartosc": 2999},
{"produkt": "klawiatura", "wartosc": 249},
{"produkt": "mysz", "wartosc": 89},
{"produkt": "mysz", "wartosc": 89}
]

from collections import defaultdict

grouped_transactions = defaultdict(int)
for t in transakcje:
    grouped_transactions[t["produkt"]] += t["wartosc"]

print(grouped_transactions)
