# https://github.com/LiquidFun/adventofcode/blob/main/2024/15/15.py

def solve(field):
    coords = {x+1j*y: c for y, r in enumerate(field.split("\n")) for x, c in enumerate(r)}

    pos = [c for c in coords if coords[c] == "@"][0]
    coords[pos] = "."

    def find_boxes(c):
        if coords[c] not in "]O[":
            return {}
        c_adj = c + ("]O[".index(coords[c]) - 1 if dir.imag else 0)
        return {c: coords[c], c_adj: coords[c_adj]} \
               | find_boxes(c+dir) \
               | find_boxes(c_adj+dir)

    for move in moves.replace("\n", ""):
        dir = {'>': 1, 'v': 1j, '<': -1, '^': -1j}[move]
        if coords[pos+dir] == '#': continue

        boxes = find_boxes(pos+dir)
        if all(coords[box+dir] != "#" for box in boxes):
            coords |= {box: '.' for box in boxes}
            coords |= {box+dir: boxes[box] for box in boxes}
            pos += dir
        
    return int(sum(c.imag*100 + c.real for c in coords if coords[c] in '[O'))

field, moves = "".join(open("input.txt").readlines()).split("\n\n")

print("\nPart1:", solve(field))
for r1, r2 in [("#", "##"), ("O", "[]"), (".", ".."), ("@", "@.")]:
    field = field.replace(r1, r2)
print("Part2:", solve(field), "\n")