def partx(lines, partn):
	lines = open("input.txt", mode = "r", encoding = "utf-8").readlines()
	gears = [[0 for i in range(len(lines))] for j in range(len(lines))]
	ratio = [[1 for i in range(len(lines))] for j in range(len(lines))]
	total = 0
	for i in range(len(lines)):
		line = lines[i].strip()
		value = -1
		ignore = 0
		for j in range(len(line)):
			if ignore == 0:
				if line[j].isdigit():
					if j < len(line) - 1:
						if line[j+1].isdigit():
							if j < len(line) - 2:
								if line[j+2].isdigit():
									value = int(line[j:j+3])
									ignore = 2
									indexes = [j, j+1, j+2]
								else:
									value = int(line[j:j+2])
									ignore = 1
									indexes = [j, j+1]
						else:
							value = int(line[j])
							indexes = [j]
			else:
				ignore -= 1
			if value != -1:
				checks = []
				if indexes[0] != 0:
					indexes = [indexes[0]-1]+indexes
					checks.append(line[indexes[0]])
					if checks[-1] == "*":
						gears[i][indexes[0]] += 1
						ratio[i][indexes[0]] *= value
				if indexes[-1] != len(line)-1:
					indexes = indexes+[indexes[-1]+1]
					checks.append(line[indexes[-1]])
					if checks[-1] == "*":
						gears[i][indexes[-1]] += 1
						ratio[i][indexes[-1]] *= value
				if i != 0:
					for k in indexes:
						checks.append(lines[i-1][k])
						if checks[-1] == "*":
							gears[i-1][k] += 1
							ratio[i-1][k] *= value
				if i != len(lines)-1:
					for k in indexes:
						checks.append(lines[i+1][k])
						if checks[-1] == "*":
							gears[i+1][k] += 1
							ratio[i+1][k] *= value
				if checks.count(".") != len(checks):
					total += value
				value = -1
	if partn == 1:
		return total
	total = 0
	for i in range(len(gears)):
		for j in range(len(gears[i])):
			if gears[i][j] == 2:
				total += ratio[i][j]
	return total

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	print(partx(lines = lines, partn = 1))
	print(partx(lines = lines, partn = 2))