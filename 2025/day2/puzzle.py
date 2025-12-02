my_input = [line.rstrip().split(',') for line in open("input").readlines()][0]

def range_repeating_internal(some_number, seq_size):
	num_as_str = str(some_number)
	str_len = len(num_as_str)	
	
	start_sequence = num_as_str[0:seq_size]
	possible_repeats = str_len // seq_size
#	print(f'testing {some_number}, with start {start_sequence}, and {possible_repeats} possible repeats')
	for i in range(1, possible_repeats):
		current_sequence = num_as_str[i*seq_size:(i+1)*seq_size]
		if start_sequence != current_sequence:
#			print(f'sequences {start_sequence} and {current_sequence} differ!')
			return False
	return True


def range_repeating(some_number):
	num_as_str = str(some_number)
	str_len = len(num_as_str)	
	
	for i in range(1, str_len//2+1):
		# we can't repeat this pattern as it wouldn't fit
		if str_len % i != 0:
			continue

		if range_repeating_internal(some_number, i):
			return True

	return False


def is_invalid_part1(some_number):
	# is number repeating?
	num_as_str = str(some_number)
	str_len = len(num_as_str)
	if str_len % 2 == 0:
		# doesn't have a middle
		return num_as_str[0:str_len//2] == num_as_str[str_len//2:str_len]
	else:
		return False

def is_invalid_part2(some_number):
	return range_repeating(some_number)
	
invalid_ids = []
for id_range in my_input:
	start, end = [int(a) for a in id_range.split('-')]
	current = start
	for i in range(start, end+1):
		if is_invalid_part2(i):
#			print(f'INVALID ID DETECTED: {i}')
			invalid_ids.append(i)
	
print(sum(invalid_ids))