values_list = [23, 24, 22, 150, 23, 25, -10, 24, 23]
min_val = 20
max_val = 30

clean_values = [x for x in values_list if min_val <= x <= max_val]

print(clean_values)