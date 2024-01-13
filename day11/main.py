def expand():
	for line in lines:
		line = [char for char in line.strip()]
		if "#" not in line:
			universe.append(["x" for char in line])
		universe.append(line)
	expansions = []
	for j in range(len(universe[0])):
		if "#" not in [universe[i][j] for i in range(len(universe))]:
			expansions.append(j+len(expansions))
	for j in expansions:
		for i in range(len(universe)):
			universe[i].insert(j, "x")

def get_distance(galaxyA, galaxyB):
	iA, iB, jA, jB = galaxyA[0], galaxyB[0], galaxyA[1], galaxyB[1]
	di, dj = iB-iA, jB-jA
	distance = sum([factor[0]-1 if universe[i][jA] == "x" else 1 for i in range(iA, iA+di)])
	distance += sum([factor[0]-1 if universe[iA][j] == "x" else 1 for j in (range(jA, jA+dj) if dj >= 0 else range(jA+dj, jA))])
	return distance

def get_galaxies():
	return [[i, j] for i in range(len(universe)) for j in range(len(universe[i])) if universe[i][j] == "#"]

def part1():
	galaxies = get_galaxies()
	return sum([get_distance(galaxy, galaxies[l]) for k, galaxy in enumerate(galaxies) for l in range(k+1, len(galaxies))])

def part2():
	factor[0] = 1000000
	return part1()

if __name__ == "__main__":
	factor = [2]
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	universe = []
	expand()
	print(part1())
	print(part2())