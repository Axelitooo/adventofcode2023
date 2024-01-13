def horizontal_reflection(pattern):
	for i in range(1, len(pattern)):
		if pattern[i] == pattern[i-1]:
			prev_lines_indexes = [j for j in range(0, i)][::-1]
			next_lines_indexes = [j for j in range(i, len(pattern))]
			match = True
			for j in range(min(len(prev_lines_indexes), len(next_lines_indexes))):
				if pattern[prev_lines_indexes[j]] != pattern[next_lines_indexes[j]]:
					match = False
					break
			if match:
				return i
				break
	return 0

def get_comparable_strings(string, i):
	prev_chars = string[:i][::-1]
	next_chars = string[i:]
	length = min(len(prev_chars), len(next_chars))
	return prev_chars[:length], next_chars[:length]

def vertical_reflection(pattern):
	line = pattern[0]
	for i in range(1, len(line)):
		prev_chars, next_chars = get_comparable_strings(line, i)
		if prev_chars in next_chars or next_chars in prev_chars:
			match = True
			for j in range(1, len(pattern)):
				prev_chars, next_chars = get_comparable_strings(pattern[j], i)
				if not (prev_chars in next_chars or next_chars in prev_chars):
					match = False
					break
			if match:
				return i
				break
	return 0

def score(pattern):
	return 100*horizontal_reflection(pattern)+vertical_reflection(pattern)

def part1():
	summary = 0
	for pattern in patterns:
		summary += score(pattern)
	return summary

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	lines.append("\n")
	patterns = []
	pattern = []
	for i, line in enumerate(lines):
		if line == "\n":
			patterns.append(pattern)
			pattern = []
		else:
			pattern.append(line.strip())
	print(part1())