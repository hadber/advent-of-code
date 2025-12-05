my_input = [line.rstrip() for line in open("input").readlines()]

class RangeContainer:
	# this could also be a range or kd tree but i think we're fine
	_ranges = []
	
	def add_range(self, some_range):
		print(f'Adding new range: {some_range}')
		left, right = some_range
		overlapping_ranges = []
		indices_to_delete = []
		for idx, (start, end) in enumerate(self._ranges):
			print(f'Looking at: {start}, {end}')
			if start <= left and right <= end:
				# new range is already fully contained
				print(f'New range is fully contained.')
				return		
			
			elif left <= start and end <= right:
				# new range fully encapsulates current range
				print(f'New range fully encapsulate existing range.')
				indices_to_delete.append(idx)
				overlapping_ranges.append((start, end))
			
			elif (left <= start and right >= start) or (left <= end and right >= end):
				# range overlaps on the left
				print(f'New range overlaps on the left.', start, end)
				indices_to_delete.append(idx)
				overlapping_ranges.append((start, end))
			
			elif (right >= end and left <= start):
				# range overlaps on the right
				print(f'New range overlaps on the right.', start, end)
				indices_to_delete.append(idx)
				overlapping_ranges.append((start, end))
		
		if not overlapping_ranges:		
			# if range hasn't been found yet, simply add it, means it's a brand new range
			print(f'Brand new range.')
			self._ranges.append((left, right))
			return

		overlapping_ranges.append(some_range)
		min_left = 100000000000000000000000000000000 # big enough
		min_right = -1
		for l, r in overlapping_ranges:			
			if l < min_left:
				min_left = l
			
			if r > min_right:
				min_right = r
				
		self._ranges.append((min_left, min_right))

		# clear out all of the old ranges
		for i in sorted(indices_to_delete, reverse=True):
			del self._ranges[i]


	def contains_id(self, some_id):
		for start, end in self._ranges:
			if some_id >= start and some_id <= end:
				return True
		return False

	def print_ranges(self):
		for a in self._ranges:
			print(a)

	def get_ranges_range(self):
		total = 0
		for l, r in self._ranges:
			total += r - l + 1
		return total

ranges = RangeContainer()
processing_ranges = True
fresh_ingredients = 0
for line in my_input:
	if not line:
		processing_ranges = False
		ranges.print_ranges()
		continue
		
	if processing_ranges:
		# add ranges
		start, end = [int(x) for x in line.split('-')]
		ranges.add_range((start, end))
	else:
		# verify ingredients
		if ranges.contains_id(int(line)):
			print(f'Ingredient {line} is fresh!')
			fresh_ingredients += 1
		else:
			print(f'Ingredient {line} is spoiled :(')
		
print(fresh_ingredients) # part 1
print(ranges.get_ranges_range()) # part 2
