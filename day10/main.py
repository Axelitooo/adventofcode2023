from shapely import *

def inrange(x, a = 0, b = 140):
	return (a <= x and x < b)

def vicinity(i, j, exclude = -1):
	IJ = [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]
	return [IJ[k] if k != exclude and inrange(IJ[k][0]) and inrange(IJ[k][1]) else [] for k in range(len(IJ))]

def get_s():
	for i in range(len(pipes)):
		for j in range(len(pipes[i])):
			if pipes[i][j] == "S":
				loop.append(Point(i, j))
				return i, j

def extendable(pipe, k):
	extendables = {
	"S":True,
	"L":k==0 or k==1, "|":k==0 or k==2, "J":k==0 or k==3,
	"F":k==1 or k==2, "-":k==1 or k==3,
	"7":k==2 or k==3,
	".":False
	}
	return extendables[pipe]

def extends(pipe, k):
	extendors = [["|", "7", "F"], ["-", "7", "J"], ["|", "L", "J"], ["-", "L", "F"]]
	return (pipe in extendors[k] or pipe == "S")

def next(i, j, exclude = -1):
	for k, ij in enumerate(vicinity(i, j)):
		if k != exclude and len(ij) > 0 and extendable(pipes[i][j], k) and extends(pipes[ij[0]][ij[1]], k):
			loop.append(Point(ij[0], ij[1]))
			return ij[0], ij[1], (k+2)%4

def part1():
	i0, j0 = get_s()
	i, j, exclude = next(i0, j0)
	steps = 1
	while (i != i0 or j != j0):
		i, j, exclude = next(i, j, exclude)
		steps += 1
	return steps//2

def part2():
	poly = Polygon(loop)
	return sum([contains(poly, Point(i, j)) for i in range(len(pipes)) for j in range(len(pipes[i]))])

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	pipes = [[pipe for pipe in line.strip()] for line in lines]
	loop = []
	print(part1())
	print(part2())