import numpy as np

exams = np.array([
[78, 85, 92, 88],
[65, 72, 68, 70],
[90, 88, 95, 92],
[55, 60, 58, 62],
[82, 79, 85, 80]
])

bonus = [5, 10, 5, 10]


exams_wbonus = exams + bonus

print(exams_wbonus)

multipliers = np.array([1.0, 1.1, 0.95, 1.15, 1.0])

exams_wmulti = exams_wbonus * multipliers.reshape(5,1)

print (exams_wmulti)