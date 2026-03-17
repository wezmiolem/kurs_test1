min_in_col = 50
max_in_col = 100
values = [75, 50, 100, 62.5]

def normalized_value(x,min,max):
    normalized = (x-min)/(max-min)
    print(f"{x:<4} | {normalized:<4}")

for i in values:
    normalized_value(i,min_in_col,max_in_col)

