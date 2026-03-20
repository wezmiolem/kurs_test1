string_example = "Alice,28,Data Scientist,75000"
string_parts = string_example.split(",")
print(f"{string_parts[0]} ma {int(string_parts[1])} lat, pracuje jako {string_parts[2]} i zarabia ${int(string_parts[3])}.")