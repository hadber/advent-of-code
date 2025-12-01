my_input = [line.rstrip() for line in open("input").readlines()]

times_on_zero = 0
times_over_zero = 0
current_position = 50

for line in my_input: 
	rotation = -1 if line[0] == 'L' else 1
	amount = rotation * int(line[1:])
	
	next_position = current_position + amount
	
	print(f'currently on: {current_position}\tmoving by: {amount}\tnext: {next_position % 100}')
	if current_position != 0 or abs(amount) >= 100:
		changed = False
		if rotation == -1 and next_position < 0:
			# we're going left and we skipped over 0, but by how much?
			times_over_zero += (abs(next_position) // 100) + (1 if current_position != 0 else 0)
			changed = True
			print(f'left over zero by: {(abs(next_position) // 100) + 1}')
		elif rotation == 1 and next_position > 100:
			# we're going right and went over at least once
			times_over_zero += next_position // 100
			changed = True
			print(f'right over zero by: {next_position // 100}')
	
		# if we land on a 0 while rotating around, take away that final 0
		if next_position % 100 == 0 and changed:
			times_over_zero -= 1
	
	current_position = next_position % 100
	if current_position == 0:
		times_on_zero += 1
		print(f'we are on zero')
		
print(f'part1: {times_on_zero}')
print(f'part2: {times_over_zero}')
print(f'total: {times_over_zero + times_on_zero}')