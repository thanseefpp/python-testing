# number = int(input('Enter numbers size: '))
# expenses = []

# for i in range(1,number+1):
#     number_two = int(input('Enter numbers to array :\n'))
#     expenses.append(number_two)

expenses = [2200,2350,2600,2130,2190]
compare = expenses[1] - expenses[0]
quarter = expenses[0] + expenses[1] + expenses[2]

print(compare)
print(quarter)
values = 0
for i in range(0,len(expenses)):
    if i == len(expenses)//2:
        break
    else:
        print(i)
        values += int(expenses[i])
print()
print(values)

