def part1(lines):
	valid = { "red" : 12, "green" : 13, "blue" : 14 }
	total = 0
	for i in range(len(lines)):
		possible = True
		for handful in lines[i].split(":")[1].replace(" ", "").strip().split(";"):
			for finding in handful.split(","):
				for color in valid.keys():
					if color in finding:
						number = int(finding[:2]) if finding[1] in "0123456789" else int(finding[0])
						if number > valid[color]:
							possible = False
		if possible:
			total += i+1
	return total

def part2(lines):
	total = 0
	for i in range(len(lines)):
		valid = { "red" : 0, "green" : 0, "blue" : 0 }
		for handful in lines[i].split(":")[1].replace(" ", "").strip().split(";"):
			for finding in handful.split(","):
				for color in valid.keys():
					if color in finding:
						number = int(finding[:2]) if finding[1] in "0123456789" else int(finding[0])
						if valid[color] < number:
							valid[color] = number
		total += valid["red"]*valid["green"]*valid["blue"]
	return total

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	print(part1(lines = lines))
	print(part2(lines = lines))