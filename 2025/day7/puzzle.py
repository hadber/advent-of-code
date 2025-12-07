my_input = [[x for x in line.rstrip()] for line in open("input").readlines()]

start = set([len(my_input[0])//2])
def part1():
	copied_input = my_input.copy()
	tachyons = start # starts in the middle of first line
	splits = 0
	for line in copied_input[1:]:
		next_tachyons = set()
		for tachyon in tachyons:
			location = line[tachyon]
			if location == '^':
				splits += 1
				next_tachyons.add(tachyon+1)
				next_tachyons.add(tachyon-1)
				line[tachyon+1] = '|'
				line[tachyon-1] = '|'
			elif location == '.':
				next_tachyons.add(tachyon)
				line[tachyon] = '|'
		tachyons = next_tachyons
	return splits

columns = [0 for _ in my_input[0]]
def part2():
	tachyons = start # starts in the middle of first line
	columns[len(my_input[0])//2] += 1
	for line in my_input[1:]:
		next_tachyons = set()
		for tachyon in tachyons:
			location = line[tachyon]
			if location == '^':
				next_tachyons.add(tachyon+1)
				next_tachyons.add(tachyon-1)
				current_value = columns[tachyon]
				columns[tachyon+1] += columns[tachyon]
				columns[tachyon-1] += columns[tachyon]
				columns[tachyon] = 0
			elif location == '.':
				next_tachyons.add(tachyon)
		tachyons = next_tachyons
	return sum(columns)

#print(part1())
print(part2())
