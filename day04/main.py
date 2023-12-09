def part1():
	total = 0
	for line in lines:
		winningS = line[0]
		currentS = line[1]
		winningI = []
		currentI = []
		for j in range(len(winningS)):
			if j < len(winningS) - 1 and j % 3 == 1:
				winningI.append(int(winningS[j:j+2]))
		for j in range(len(currentS)):
			if j < len(currentS) - 1 and j % 3 == 1:
				currentI.append(int(currentS[j:j+2]))
		multi = 0
		for current in currentI:
			if current in winningI:
				multi += 1 if multi == 0 else multi
		total += multi
	return total

def part2():
	total = [1 for i in range(len(lines))]
	for i, line in enumerate(lines):
		winningS = line[0]
		currentS = line[1]
		winningI = []
		currentI = []
		for j in range(len(winningS)):
			if j < len(winningS) - 1 and j % 3 == 1:
				winningI.append(int(winningS[j:j+2]))
		for j in range(len(currentS)):
			if j < len(currentS) - 1 and j % 3 == 1:
				currentI.append(int(currentS[j:j+2]))
		cards = 0
		for current in currentI:
			if current in winningI:
				cards += 1
		for j in range(cards):
			if i+1+j < len(total):
				total[i+1+j] += total[i]
	return sum(total)

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	lines = [line.strip().split(":")[1].split("|") for line in lines]
	print(part1())
	print(part2())