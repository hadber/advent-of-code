my_input = [[x for x in line.rstrip().split(' ') if x] for line in open("input").readlines()]

numbers_y_len = len(my_input) - 1

#part 1
totals = 0
for idx, operation in enumerate(my_input[-1]):
	operation_total = 0
	if operation == '+':
		for y in range(numbers_y_len):
			operation_total += int(my_input[y][idx])
	else:
		operation_total = 1
		for y in range(numbers_y_len):
			operation_total *= int(my_input[y][idx])
	totals += operation_total
			
#print(totals)

#part 2
new_input = open("input").readlines()

dividers = []
for idx in range(len(new_input[-1])):
#	print(f'current character: [{new_input[-1][idx]}]')
	if new_input[-1][idx] != ' ':
		dividers.append(idx)
dividers.append(len(new_input[0])) # for the last column of numbers

numbers = []
for d in range(len(dividers)-1):
	tmp_numbers = []
	for y in range(numbers_y_len):
		start_i = dividers[d]
		end_i = dividers[d+1]
		tmp_numbers.append(new_input[y][start_i:end_i-1])
	numbers.append(tmp_numbers)

good_numbers = []
for column in numbers:
	tmp = []
	for y in range(len(column[0])):
		nr = ''
		for x in range(len(column)):
			nr += column[x][y]
		tmp.append(int(nr))
	good_numbers.append(tmp)

new_totals = 0
for idx, operation in enumerate(my_input[-1]):
	operation_total = 0
	if operation == '+':
		for nr in good_numbers[idx]:
			operation_total += nr
	else:
		operation_total = 1
		for nr in good_numbers[idx]:
			operation_total *= nr
	new_totals += operation_total

print(new_totals)


# too cool to remove, but alas it doesn't work since
# i assumed numbers are always right-aligned
#
#def construct_numbers(some_x):
#	numbers = []
#	start = 1
#	while True:
#		current_number = 0
#		for y in range(numbers_y_len):
#			digit = (int(my_input[y][some_x]) // start) % 10
#			current_number += digit * (10**y)
#		if current_number == 0:
#			break
#		else:
#			numbers.append(int(str(current_number)[::-1]))
#			start *= 10
#	return numbers

#p2_totals = 0
#for idx, operation in enumerate(my_input[-1]):
#	operation_total = 0
#	print(construct_numbers(idx), idx)
#	if operation == '+':
#		operation_total += sum(construct_numbers(idx))
#	else:
#		operation_total = 1
#		for x in construct_numbers(idx):
#			operation_total *= x
#	print(operation_total)
#	p2_totals += operation_total
	
#print(p2_totals)

