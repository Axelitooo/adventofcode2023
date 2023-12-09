def part1():
	valid = { "red" : 12, "green" : 13, "blue" : 14 }
	total = 0
	for i, line in enumerate(lines):
		possible = True
		for handful in line:
			for finding in handful.split(","):
				for color in valid.keys():
					if color in finding:
						number = int(finding[:2]) if finding[1].isdigit() else int(finding[0])
						if number > valid[color]:
							possible = False
		if possible:
			total += i+1
	return total

def part2():
	total = 0
	for line in lines:
		valid = { "red" : 0, "green" : 0, "blue" : 0 }
		for handful in line:
			for finding in handful.split(","):
				for color in valid.keys():
					if color in finding:
						number = int(finding[:2]) if finding[1].isdigit() else int(finding[0])
						if valid[color] < number:
							valid[color] = number
		total += valid["red"]*valid["green"]*valid["blue"]
	return total

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	lines = [line.split(":")[1].replace(" ", "").strip().split(";") for line in lines]
	print(part1())
	print(part2())