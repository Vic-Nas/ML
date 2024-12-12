#Mine was too slow and too long again

with open("input.txt") as fd:
    _data = [i.strip() for i in fd.readlines()]

    data = [[j for j in i] for i in _data]
    rows, cols = len(data), len(data[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    score = 0
    score1 = 0

    def is_same(x, y):
        i, j = x
        k, l = y
        return 0 <= i < rows and 0 <= j < cols and 0 <= k < rows and 0 <= l < cols and data[i][j] == data[k][l]

    for i in range(rows):
        for j in range(cols):
            if visited[i][j]:
                continue

            lv = [[False for _ in range(cols)] for _ in range(rows)]
            q = [(i, j)]
            perimeter = 0
            area = 0
            sides = 0

            while q:
                x, y = q.pop(0)
                if lv[x][y] or visited[x][y]:
                    continue

                area += 1
                visited[x][y] = True
                lv[x][y] = True

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    px, py = x + dy, y - dx
                    pnx, pny = px + dx, py + dy

                    if is_same((x, y), (nx, ny)):
                        q.append((nx, ny))
                    else:
                        perimeter += 1
                        if not is_same((x, y), (px, py)) or is_same((px, py), (pnx, pny)):
                            sides += 1

            score += area * perimeter
            score1 += area * sides

            for r in range(rows):
                for c in range(cols):
                    visited[r][c] = visited[r][c] or lv[r][c]

    print(score)
    print(score1)
