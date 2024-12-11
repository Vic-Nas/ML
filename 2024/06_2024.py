# Not really mine
# Mine was too slow

grid = []
from tqdm import tqdm
def rotate(_direction):
    return _direction[1], -_direction[0]

for i, line in enumerate(open("input.txt", "r").readlines()):
    line = line.rstrip()
    if '^' in line:
        position = i, line.find('^')
        line = line.replace('^', '.')
    grid.append(list(line))

def solve_grid(_grid, _position, _direction):
    _seen_positions_directions = set()
    _seen_positions_directions.add((_position, _direction))
    while True:
        next_square = _position[0] + _direction[0], _position[1] + _direction[1]
        try:
            if next_square[0] < 0 or next_square[1] < 0:
                raise IndexError
            grid_square_next = _grid[next_square[0]][next_square[1]]
        except IndexError:
            return "out", _seen_positions_directions
        _seen_positions_directions.add((_position, _direction))
        if grid_square_next == '#':
            _direction = rotate(_direction)
        else:
            if (next_square, _direction) in _seen_positions_directions:
                return "loop", _seen_positions_directions
            _position = next_square

_, seen_positions_directions = solve_grid(grid, position, (-1, 0))
seen_positions = {p for p, _ in seen_positions_directions}
print(f"\nPart1: {len(seen_positions) + 1}")
loopies = 1

for i in tqdm(range(0, len(grid)), desc = "Part2"):
    for j in range(0, len(grid[0])):
        if (i, j) not in seen_positions:
            continue
        if grid[i][j] == '#':
            continue
        grid[i][j] = '#'
        end, _ = solve_grid(grid, position, (-1, 0))
        if end == 'loop':
            loopies += 1
        grid[i][j] = '.'
print(loopies, "\n")