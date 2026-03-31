wynagrodzenia = [3500, 4200, 5800, 7200, 9500, 4800, 6100]



def normalize_minmax(dane):
    min_val = min(dane)
    max_val = max(dane)
    normalized_data = [(x-min_val)/(max_val-min_val) for x in dane]
    normalized_data_rounded = [round(x,3) for x in normalized_data]
    return normalized_data_rounded

print(normalize_minmax(wynagrodzenia))