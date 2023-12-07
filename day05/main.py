def buildMapps(lines):
	mapps = []
	mapindex = -1
	for i in range(2, len(lines)):
		if lines[i][0] in "0123456789":
			numbers = lines[i].strip().split(" ")
			mapp = [int(number) for number in numbers]
			mapps[mapindex].append(mapp)
		elif lines[i][0] != "\n":
			mapindex += 1
			mapps.append([])
	return mapps

def part1(seeds, mapps):
	minimum = 10E12
	for seed in seeds:
		for mapp in mapps:
			for line in mapp:
				destin = line[0]
				source = line[1]
				ranges = line[2]
				if seed >= source and seed < source+ranges:
					seed += destin-source
					break
		if seed < minimum:
			minimum = seed
	return minimum

def part2(seeds, mapps):
	minimum = 10E12
	i = 0
	while i < len(seeds):
		j = 0
		while j < seeds[i+1]:
			same = []
			seed = seeds[i]+j
			for mapp in mapps:
				found = False
				for line in mapp:
					destin = line[0]
					source = line[1]
					ranges = line[2]
					if seed >= source and seed < source+ranges:
						same.append(ranges-(seed-source))
						seed += destin-source
						found = True
						break
				if not found:
					if seed > max([line[1]+line[2] for line in mapp]):
						same.append(10E12)
					else:
						same.append(min([line[1] for line in mapp if line[1] > seed]))
			if seed < minimum:
				minimum = seed
			j += 1 if len(same) == 0 else min(same)
		i += 2
	return minimum

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	mapps = buildMapps(lines = lines)
	seeds = [int(seed) for seed in lines[0].strip().split(":")[1:][0].split(" ")[1:]]
	print(part1(seeds = seeds, mapps = mapps))
	print(part2(seeds = seeds, mapps = mapps))