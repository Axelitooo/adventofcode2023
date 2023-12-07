def part1(lines):
	total = 0
	for i in range(len(lines)):
		line = lines[i].strip().split(":")[1].split("|")
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

def part2(lines):
	total = [1 for i in range(len(lines))]
	for i in range(len(lines)):
		line = lines[i].strip().split(":")[1].split("|")
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
	print(part1(lines = lines))
	print(part2(lines = lines))