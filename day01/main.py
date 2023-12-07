def part1(lines):
	total = 0
	for line in lines:
		first = -1
		last = -1
		for char in line:
			if char in "123456789":
				if first == -1:
					first = int(char)
				last = int(char)
		total += 10*first+last
	return total

def part2(lines):
	digits = ["one","two","three","four","five","six","seven","eight","nine"]
	total = 0
	for line in lines:
		numbers = []
		for i, char in enumerate(line):
			if char in "123456789":
				numbers.append(int(char))
			for j, digit in enumerate(digits):
				if line[i:].startswith(digit):
					numbers.append(j+1)
		total += 10*numbers[0]+numbers[-1]
	return total

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	print(part1(lines = lines))
	print(part2(lines = lines))