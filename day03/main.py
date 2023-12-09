def check_gear(i, j, value):
	if lines[i][j] == "*":
		gears[i][j] += 1
		ratio[i][j] *= value
	return lines[i][j]

def around(i, value, indexes):
	checks = []
	if indexes[0] != 0:
		indexes = [indexes[0]-1]+indexes
		checks.append(check_gear(i = i, j = indexes[0], value = value))
	if indexes[-1] != len(lines[i])-1:
		indexes = indexes+[indexes[-1]+1]
		checks.append(check_gear(i = i, j = indexes[-1], value = value))
	if i != 0:
		for j in indexes:
			checks.append(check_gear(i = i-1, j = j, value = value))
	if i != len(lines)-1:
		for j in indexes:
			checks.append(check_gear(i = i+1, j = j, value = value))
	return checks

def part1():
	total = 0
	for i, line in enumerate(lines):
		value = -1
		ignore = 0
		for j, char in enumerate(line):
			if ignore > 0:
				ignore -= 1
			elif char.isdigit() and j < len(line)-1:
				if not line[j+1].isdigit():
					digits = 1
				elif j < len(line)-2:
					digits = 2 if not line[j+2].isdigit() else 3
				value = int(line[j:j+digits])
				ignore = digits-1
				indexes = [j+k for k in range(digits)]
			if value != -1:
				checks = around(i = i, value = value, indexes = indexes)
				if checks.count(".") != len(checks):
					total += value
				value = -1
	return total

def part2():
	return sum([ratio[i][j] for i in range(len(gears)) for j in range(len(gears[i])) if gears[i][j] == 2])

if __name__ == "__main__":
	lines = [line.strip() for line in open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()]
	gears = [[0 for i in range(len(lines))] for j in range(len(lines))]
	ratio = [[1 for i in range(len(lines))] for j in range(len(lines))]
	print(part1())
	print(part2())