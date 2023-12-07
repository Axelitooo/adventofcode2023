def part1(lines):
	times = [int(element) for element in lines[0].strip().split(" ")[6:] if element != ""]
	dists = [int(element) for element in lines[1].strip().split(" ")[2:] if element != ""]
	ways = [0 for i in range(len(times))]
	for i in range(len(times)):
		for j in range(times[i]):
			if (times[i]-j)*j > dists[i]:
				ways[i] += 1
	return ways[0]*ways[1]*ways[2]*ways[3]

def part2(lines):
	times = [element for element in lines[0].strip().split(" ")[6:] if element != ""]
	dists = [element for element in lines[1].strip().split(" ")[2:] if element != ""]
	time = int(times[0]+times[1]+times[2]+times[3])
	dist = int(dists[0]+dists[1]+dists[2]+dists[3])
	a = -1
	b = time
	c = -dist
	d = b**2-4*a*c
	tmax = (-b-d**0.5)/(2*a)
	tmin = (-b+d**0.5)/(2*a)
	ways = int(tmax)-int(tmin)
	return ways

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	print(part1(lines = lines))
	print(part2(lines = lines))