LAST = [0]

def find(instr, nodes, node):
	steps = 0
	while True:
		for LorR in instr:
			steps += 1
			node = nodes[node][LorR == "R"]
			if node[0+2*LAST[0]:3] == "ZZZ"[0+2*LAST[0]:3]:
				return steps

def part1(instr, nodes):
	return find(instr = instr, nodes = nodes, node = "AAA")

def part2(instr, nodes):
	LAST[0] = 1
	steps = [find(instr = instr, nodes = nodes, node = node) for node in nodes.keys() if node[2] == "A"]
	ppcm = len(instr)
	for i in [step / len(instr) for step in steps]:
		ppcm *= i
	return int(ppcm)

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	instr = lines[0].strip()
	nodes = {}
	for line in lines[2:]:
		line = line.split(" ")
		nodes[line[0]] = (line[2].replace("(", "").replace(",", ""), line[3].replace(")", "").strip())
	print(part1(instr = instr, nodes = nodes))
	print(part2(instr = instr, nodes = nodes))