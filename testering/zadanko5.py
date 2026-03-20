import re

string_example = "model_results_2024_Q3.csv"

numbers = re.findall(r'\d+', string_example)
print(f"year: {numbers[0]}, quarter: {numbers[1]}")
