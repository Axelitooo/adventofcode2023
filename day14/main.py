def get_new_place(i, j, cardinal):
	if cardinal % 2 == 0:
		if cardinal == 0:
			index = i
			while index != 0 and rows[index-1][j] == ".":
				index -= 1
		else:
			index = i
			while index != len(rows)-1 and rows[index+1][j] == ".":
				index += 1
	else:
		if cardinal == 1:
			index = j
			while index != 0 and rows[i][index-1] == ".":
				index -= 1
		else:
			index = j
			while index != len(rows[i])-1 and rows[i][index+1] == ".":
				index += 1
	return index

def roll(cardinal):
	for i in range(len(rows)):
		if cardinal == 2:
			i = len(rows)-1-i
		for j in range(len(rows[i])):
			if cardinal == 3:
				j = len(rows[i])-1-j
			if rows[i][j] == "O":
				index = get_new_place(i, j, cardinal)
				if cardinal % 2 == 0:
					if index != i:
						rows[index][j] = "O"
						rows[i][j] = "."
				else:
					if index != j:
						rows[i][index] = "O"
						rows[i][j] = "."

def calculate_load():
	load = 0
	for i in range(len(rows)):
		for j in range(len(rows[i])):
			if rows[i][j] == "O":
				load += len(rows)-i
	return load

def part1():
	roll(0)
	return calculate_load()

def do_a_barrel_roll():
	for cardinal in range(4):
		roll(cardinal)

def arrays_equal(array_1, array_2):
	for i in range(len(array_1)):
		if array_1[i] != array_2[i]:
			return False
	return True

def determine_cycle_and_final_load(loads):
	cycle = []
	for i in range(2 * len(loads) // 3):
		if len(cycle) != 0:
			break
		for j in range(6, len(loads) // 3):
			if arrays_equal(loads[i:i+j], loads[i+j:i+2*j]):
				cycle = [load for load in loads[i:i+j]]
				break
	return cycle[(1000000000-i)%len(cycle)]

def part2():
	steps = 300
	loads = []
	for i in range(steps):
		do_a_barrel_roll()
		load = calculate_load()
		loads.append(load)
	load = determine_cycle_and_final_load(loads)
	return load

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	rows = [[char for char in line.strip()] for line in lines]
	print(part1())
	print(part2())