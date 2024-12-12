#Mine was too slow and too long again

import numpy as np
with open("input.txt") as fd:
    _data = [i.strip() for i in fd.readlines()]
    
    data = np.array([[j for j in i] for i in _data])
    visited = np.zeros_like(data, dtype=bool)
    score = 0
    score1 = 0
    def is_same(x, y):
        i, j = x
        k, l = y
        return 0 <= i < data.shape[0] and 0 <= j < data.shape[1] and 0 <= k < data.shape[0] and 0 <= l < data.shape[1] and data[i, j] == data[k, l]
            
        
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if visited[i, j]:
                continue
            lv = np.zeros_like(data, dtype=bool)
            q = [(i, j)]
            perimiter = 0
            area = 0
            sides = 0

            while len(q) > 0:
                x, y = q.pop(0)
                if lv[x, y] or visited[x, y]:
                    continue

                area += 1
                visited[x, y] = True
                lv[x, y] = True
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    px, py = x + dy, y - dx
                    pnx, pny = px + dx, py + dy
                    if is_same((x, y), (nx, ny)):
                        q.append((nx, ny))
                    else:
                        perimiter += 1
                        if not is_same((x, y), (px, py)) or is_same((px, py), (pnx, pny)):
                            sides += 1
                    

                        
            print(data[i, j], area, perimiter)
            score += area * perimiter
            score1 += area * sides
            visited |= lv
    print(score)
    print(score1)
