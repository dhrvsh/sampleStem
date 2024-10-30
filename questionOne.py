s = [110, 125, 128, 135, 128, 142, 138, 182, 170]
d = [73, 75, 75, 75, 88, 88, 95, 100, 125]

output = []
number = 0

for i in range(9):
    if s[i] < 120 and d[i] < 80:
        number += 1

output.append(number)

number = 0

for i in range(9):
    if s[i] >= 120 and s[i] <= 129 and d[i] < 80:
        number += 1

output.append(number)


number = 0

for i in range(9):
    if s[i] >= 130 and s[i] <= 139 and d[i] >= 80 and d[i] <= 89:
        number += 1
        print("yes")
output.append(number)


print(output)