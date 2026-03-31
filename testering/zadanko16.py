klienci = [
{"id": 1, "wiek": 25, "dochod": 4500},
{"id": 2, "wiek": 45, "dochod": 9200},
{"id": 3, "wiek": 32, "dochod": 6800},
{"id": 4, "wiek": 28, "dochod": 5200},
{"id": 5, "wiek": 55, "dochod": 12000}
]

for k in klienci:
    if k["wiek"] < 30:
        k["kat_wiekowa"] = "mlody"
    elif 30 < k["wiek"] < 50:
        k["kat_wiekowa"] = "sredni"
    else:
        k["kat_wiekowa"] = "starszy"
    if k["dochod"] < 5000:
        k["kat_dochodu"] = "niski"
    elif 5000 < k["dochod"] < 10000:
        k["kat_dochodu"] = "sredni"
    else:
        k["kat_dochodu"] = "wysoki"

print(klienci)

