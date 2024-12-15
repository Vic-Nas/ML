Empty = "."
Robot = "R"
Obstacle = "#"

the_map, moves = "".join(open("input.txt", "r").readlines()).split("\n\n")
the_map = list(map(lambda row: list(row[1:-1]), the_map.split("\n")[1:-1]))

end = False
for i in range(len(the_map)):
    for j in range(len(the_map[i])):
        if the_map[i][j] == '@': 
            the_map[i][j] = Robot
            x = i; y = j
            end = True
            break
    if end: break


def transpose2D(matrix): return [list(row) for row in zip(*matrix)]
def display(the_map): 
    new = Obstacle * (len(the_map[0]) + 2)
    print(new)
    print("\n".join(Obstacle + "".join(row) + Obstacle for row in the_map))
    print(new)


def fd(sense, x, y):
    global the_map
    safe = the_map[x].copy()
    try:
        if sense == ">":
            index = the_map[x][y + 1:].index(Empty) + y + 1
            for j in range(index, y, -1): 
                if the_map[x][j] != Obstacle: the_map[x][j] = the_map[x][j - 1]
                else: the_map[x] = safe; break
            else: the_map[x][y] = Empty; y += 1
        elif sense == "<":
            the_map = transpose2D(transpose2D(the_map)[::-1])
            x, y = fd(">", x, len(the_map[x]) - 1 - y)
            y = len(the_map[x]) - y - 1
            the_map = transpose2D(transpose2D(the_map)[::-1])
        else:
            the_map = transpose2D(the_map)
            y, x = fd("<" if sense == "^" else ">", y, x)
            the_map = transpose2D(the_map)
    except: pass
    return x, y


for i, move in enumerate(moves): 
    x, y = fd(move, x, y)
    print(f"After Move {i + 1} ({move}):")
    display(the_map)
    print("\n" + "=" * 20 + "\n")

res = 0
for i in range(len(the_map)):
    for j in range(len(the_map[i])):
        if the_map[i][j] == "O": res += 100 * (i + 1) + j + 1
print(res)