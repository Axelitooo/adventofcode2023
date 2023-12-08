JOKERS = [False]

def value(card):
	values = { "J":9-9*JOKERS[0], "T":8+JOKERS[0], "Q":10, "K":11, "A":12 }
	return int(card)-(2-JOKERS[0]) if card.isdigit() else values[card]

def get_highest(hands, rank, cardi):
	indexes = [[] for i in range(13)]
	for index in rank:
		indexes[value(hands[index][cardi])].append(index)
	for rank in indexes[::-1]:
		if len(rank) > 0:
			return rank[0] if len(rank) == 1 else get_highest(hands = hands, rank = rank, cardi = cardi+1)

def get_ranks(hands):
	ranks = [[] for i in range(7)]
	for i, hand in enumerate(hands):
		cards = [0 for i in range(13)]
		for card in hand:
			cards[value(card)] += 1
		if JOKERS[0] and cards[0] > 0:
			if len([j for j in cards if j != 0]) <= 2:
				ranks[6].append(i)
			else:
				if 3 in cards:
					ranks[5].append(i)
				elif 2 in cards:
					if cards[0] == 2:
						ranks[5].append(i) if 2 in cards[1:] else ranks[3].append(i)
					else:
						ranks[4].append(i) if sum([j == 2 for j in cards]) == 2 else ranks[3].append(i)
				else:
					ranks[1].append(i)
		else:
			if 5 in cards:
				ranks[6].append(i)
			elif 4 in cards:
				ranks[5].append(i)
			elif 3 in cards:
				ranks[4].append(i) if 2 in cards else ranks[3].append(i)
			elif 2 in cards:
				ranks[2].append(i) if sum([j == 2 for j in cards]) == 2 else ranks[1].append(i)
			else:
				ranks[0].append(i)
	return ranks

def order_all(hands, ranks):
	order = []
	for rank in ranks[::-1]:
		while len(rank) > 0:
			highest = get_highest(hands = hands, rank = rank, cardi = 0)
			order.append(highest)
			rank.remove(highest)
	return order

def part1(lines):
	hands = []
	bidds = []
	for line in lines:
		line = line.strip().split(" ")
		hands.append(line[0])
		bidds.append(int(line[1]))
	ranks = get_ranks(hands = hands)
	order = order_all(hands = hands, ranks = ranks)
	return sum([bidds[index]*(i+1) for i, index in enumerate(order[::-1])])

def part2(lines):
	JOKERS[0] = True
	return part1(lines = lines)

if __name__ == "__main__":
	lines = open(file = "input.txt", mode = "r", encoding = "utf-8").readlines()
	print(part1(lines = lines))
	print(part2(lines = lines))