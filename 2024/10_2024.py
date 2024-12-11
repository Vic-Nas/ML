inp = list(map(str.strip, open("input.txt").readlines()))

def score(i, j, part, known = 0):
    if not known: known = set()
    elif not part and (i, j) in known: return 0
    known.add((i, j))
    curr = int(inp[i][j])
    if curr == 9: return 1
    next = []
    if i > 0: next.append((i - 1, j))
    if i < len(inp) - 1: next.append((i + 1, j))
    if j > 0: next.append((i, j - 1))
    if j < len(inp[0]) - 1: next.append((i, j + 1))
    return sum(score(x, y, part, known) for x, y in next if int(inp[x][y]) == curr + 1)

res1, res2 = 0, 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == "0":
            res1 += score(i, j, 0)
            res2 += score(i, j, 1)
print(f"\nPart1: {res1}\nPart2: {res2}\n")

