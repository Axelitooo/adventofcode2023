NEXT = [1]

def deeper(sequence):
	return [sequence[i]-sequence[i-1] for i in range(1, len(sequence))]

def higher(sequences, index, value):
	value = sequences[index][len(sequences[index])-1]+value if NEXT[0] else sequences[index][0]-value
	return value if index == 0 else higher(sequences = sequences, index = index-1, value = value)

def part1(lines):
	total = 0
	for line in lines:
		sequence = [int(s) for s in line.strip().split(" ")]
		sequences = [sequence]
		while True:
			sequence = deeper(sequence = sequence)
			if sum([element == 0 for element in sequence]) == len(sequence):
				total += higher(sequences = sequences, index = len(sequences)-1, value = 0)
				break
			else:
				sequences.append(sequence)
	return total

def part2(lines):
	NEXT[0] = 0
	return part1(lines)

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	print(part1(lines = lines))
	print(part2(lines = lines))