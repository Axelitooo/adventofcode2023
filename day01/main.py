def part1():
	total = 0
	for line in lines:
		first = -1
		last = -1
		for char in line:
			if char.isdigit():
				if first == -1:
					first = int(char)
				last = int(char)
		total += 10*first+last
	return total

def part2():
	digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	total = 0
	for line in lines:
		numbers_in_line = []
		for i, char in enumerate(line):
			if char.isdigit():
				numbers_in_line.append(int(char))
			else:
				for j, digit in enumerate(digits):
					if line[i:].startswith(digit):
						numbers_in_line.append(j+1)
		first = numbers_in_line[0]
		last = numbers_in_line[-1]
		total += 10*first+last
	return total

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	print(part1())
	print(part2())