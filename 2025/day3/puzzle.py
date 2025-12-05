my_input = [line.rstrip() for line in open("input").readlines()]

def find_highest_in_range(some_array, search_start, search_end):
	highest = '0'
	find_id = -1
#	print(f'looking in: {some_array[search_start:search_end]} (subarray: {search_start}-{search_end})')
	for idx, a_number in enumerate(some_array[search_start:search_end]):
		if a_number > highest:
			highest = a_number
			find_id = idx
#	print(f'found number: {highest} at {find_id}')
	return find_id

found_numbers = []
digits_amount = 12 # for part 1, change this to 1

for line in my_input:
	digits = []
	offset = 0
	for left_to_find in range(digits_amount):
		found_digit = find_highest_in_range(line, offset, len(line)-(digits_amount-(left_to_find+1))) + offset
		offset = found_digit+1
		digits.append(line[found_digit])

	found_numbers.append(int(''.join(digits)))

print(sum(found_numbers))