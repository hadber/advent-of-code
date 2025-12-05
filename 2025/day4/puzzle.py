my_input = [[x for x in line.rstrip()] for line in open("input").readlines()]

len_x = len(my_input[0])
len_y = len(my_input)

movements = [(0,-1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def is_pos_roll(some_x, some_y):
	return my_input[some_y][some_x] == '@'

def is_x_valid(some_x):
	return some_x >= 0 and some_x < len_x
	
def is_y_valid(some_y):
	return some_y >= 0 and some_y < len_y
	
def get_filled_neighbours(some_position):
	current_x, current_y = some_position
	neighbours_count = 0
	for delta_x, delta_y in movements:
		next_x = current_x + delta_x
		next_y = current_y + delta_y
		
		if not is_x_valid(next_x) or not is_y_valid(next_y):
#			print(f'invalid next at: {next_x},{next_y} bcs: {is_x_valid(next_x)} | {is_y_valid(next_y)}')
			continue
		
#		print(f'neighbour at: {next_x},{next_y}  ({my_input[next_y][next_x]})')
		if is_pos_roll(next_x, next_y):
#			print(f'neighbour is roll')
			neighbours_count += 1
	
#	print(f'position {some_position} has {neighbours_count} neighbours!')
	return neighbours_count < 4

total_removed = 0
removed_last_turn = True
while removed_last_turn: # skip the loop for part 1
	accessible = []
	for y in range(len_y):
		for x in range(len_x):
			current_pos = (x, y)
			
			if not is_pos_roll(*current_pos):
				continue
			
			if get_filled_neighbours(current_pos):
				accessible.append(current_pos)
		
	removed_last_turn = len(accessible) > 0 # list is not empty	
	for pos_x, pos_y in accessible:
		my_input[pos_y][pos_x] = 'x'
		total_removed += 1
			
#print(accessible)
print(total_removed)