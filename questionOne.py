Systolic = [110, 125, 128, 135, 128, 142, 138, 182, 170]
Diastolic = [73, 75, 75, 75, 88, 88, 95, 100, 125]

output = []
number = 0

for i in range(9):
    if data[("person" + str(i+1))][0] < 120:
        number += 1
    print(data[("person" + str(i+1))])

output.append(number)

for i in range(9):
    if data[("person" + str(i+1))][0] < 120:
        number += 1
    print(data[("person" + str(i+1))])

output.append(number)