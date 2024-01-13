from time import time

def springs_fit_clues(springs, clues):
	group_size = 0
	group_index = 0
	for i, spring in enumerate(springs):
		if spring == "#":
			group_size += 1
		if spring == "." or i == len(springs)-1:
			if group_size > 0:
				if group_index >= len(clues):
					return False
				if clues[group_index] != group_size:
					return False
				group_size = 0
				group_index += 1
	if group_index < len(clues):
		return False
	return True

def start_larger(springs, clues, clue_index):
	if clue_index == len(clues):
		return True
	else:
		clue = clues[clue_index]
	#parameters = springs+str(clue)
	#if parameters in start_larger_dict.keys():
		#calls_successful[0] += 1
		#return start_larger_dict[parameters]
	index = 0
	while springs[index] == ".":
		index += 1
		if index == len(springs):
			#start_larger_dict[parameters] = False
			return False
	start = index
	while springs[index] != ".":
		index += 1
		if index == len(springs):
			#start_larger_dict[parameters] = True
			return True
	group = springs[start:index]
	if "?" not in group:
		if len(group) != clue:
			#start_larger_dict[parameters] = False
			return False
		else:
			return start_larger(springs[index:], clues, clue_index+1)
	if "#" in group:
		#start_larger_dict[parameters] = (len(group) >= clue)
		return (len(group) >= clue)
	#start_larger_dict[parameters] = True
	return True

"""def end_larger(springs, clues, clue_index):
	clue = clues[clue_index]
	index = len(springs)-1
	while springs[index] == ".":
		index -= 1
		if index == 0:
			return (clue == 0) # False
	end = index
	while springs[index] != ".":
		index -= 1
		if index == 0:
			return True
	group = springs[index+1:end+1]
	print(springs)
	print(group)
	if "?" not in group:
		return (len(group) == clue)
	if "#" not in group:
		return (len(group) >= clue)
	return True"""

def get_first_group(springs):
	index = 0
	if not springs:
		return [], -1
	while springs[index] == ".":
		index += 1
		if index == len(springs):
			return [], -1
	start = index
	while springs[index] != ".":
		index += 1
		if index == len(springs):
			return [], -1
	return springs[start:index], index

def get_last_group(springs):
	return get_first_group(springs[::-1])

def check_group(group, clue):
	if "?" not in group:
		return (len(group) == clue)
	if "#" in group:
		return (len(group) >= clue)
	return -1

def possible(springs, clues):
	group_start, index_start = get_first_group(springs)
	group_end, index_end = get_last_group(springs)
	if len(group_start) == 0 or len(group_end) == 0 or (len(clues) == 0 and "#" in springs):
		return True
	index_end = len(springs)-index_end
	clue_start = clues[0]
	clue_end = clues[-1]
	check_start = check_group(group_start, clue_start)
	check_end = check_group(group_start, clue_start)
	if check_start == -1 and check_end == -1:
		return True
	if check_start == -1:
		if check_end:
			if len(clues) == 1:
				return True
			else:
				return possible(springs[:index_end], clues[:len(clues)-1])
		else:
			return False
	if check_end == -1:
		if check_start:
			if len(clues) == 1:
				return True
			else:
				return possible(springs[index_start:], clues[1:])
		else:
			return False
	if check_start and check_end:
		if len(clues) == 2:
			return True
		else:
			return possible(springs[index_start:index_end], clues[1:-1])
	else:
		return False
	if not check_start or not check_end:
		return False

def get_variations(springs, questions, total, clues):
	if start_larger(springs, clues, 0):
	#if possible(springs, clues):
		for i, spring in enumerate(springs):
			if spring == "?":
				prefix = springs[:i]
				suffix = springs[i+1:]
				variation_sharp = prefix+"#"+suffix
				variation_point = prefix+"."+suffix
				if "?" not in prefix+suffix:
					variations.append(variation_sharp)
					variations.append(variation_point)
					return True
				else:
					questions -= 1
					sharps_in_variation = count("#", variation_sharp)
					if sharps_in_variation > total:
						if sharps_in_variation == total+1:
							get_variations(variation_point, questions, total, clues)
							return True
						else:
							return False
					potential_sharps = questions+sharps_in_variation
					if potential_sharps < total:
						return False
					elif potential_sharps == total:
						variations.append(variation_sharp.replace("?", "#"))
						return True
					elif potential_sharps == total+1:
						variations.append(variation_point.replace("?", "#"))
						get_variations(variation_sharp, questions, total, clues)
						return True
					else:
						get_variations(variation_sharp, questions, total, clues)
						get_variations(variation_point, questions, total, clues)
						return False
	else:
		return False

def empty_variations():
	while len(variations) != 0:
		variations.pop()

def count(char, springs):
	return sum([spring == char for spring in springs])

def part1():
	arrangements = 0
	for i, springs in enumerate(all_springs):
		questions = count("?", springs)
		clues = all_clues[i]
		total = sum(clues)
		empty_variations()
		get_variations(springs, questions, total, clues)
		for variation in variations:
			arrangements += springs_fit_clues(variation, all_clues[i])
		print(arrangements)
	return arrangements

def part2():
	for i in range(4):
		for j, line in enumerate(lines):
			line = line.strip().split(" ")
			all_springs[j] += "?"+line[0]
			all_clues[j] += [int(char) for char in line[1].split(",")]
	return part1()

if __name__ == "__main__":
	#start_larger_dict = {}
	#calls_successful = [0]
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	variations = []
	all_springs = []
	all_clues = []
	for line in lines:
		line = line.strip().split(" ")
		all_springs.append(line[0])
		all_clues.append([int(char) for char in line[1].split(",")])
	start = time()
	print(part1())
	print("elapsed time : "+str(round(time()-start, 3)))
	#print(calls_successful[0])
	print(part2())
	print("elapsed time : "+str(round(time()-start, 3)))

	#1
	#16385
	#16386
	#16402
	#18902
	#525152
	#{'count': 2645684, 'get_variations': 4342988, 'start_larger': 56682413, 'springs_fit_clues': 1035823}