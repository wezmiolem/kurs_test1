squares_dict = {x: x**2 for x in range(1,21) }

squares_dict_evenonly = {number: squared for number, squared in squares_dict.items() if number % 2 == 0}

print(squares_dict)

print(squares_dict_evenonly)