wagi = [70, 85, 62, 95, 78]
wzrosty = [1.75, 1.80, 1.65, 1.78, 1.72]

for i in range(len(wagi)):
    bmi = wagi[i] / wzrosty[i] ** 2
    if bmi < 18.5:
        print(f"patient weight: {wagi[i]}, height: {wzrosty[i]}, bmi: {bmi}, underweight")
    elif bmi < 25:
        print(f"patient weight: {wagi[i]}, height: {wzrosty[i]}, bmi: {bmi}, normal weight")
    else:
        print(f"patient weight: {wagi[i]}, height: {wzrosty[i]}, bmi: {bmi}, overweight")


