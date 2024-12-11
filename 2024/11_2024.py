def blink(inp, times):
    stones = {}
    for n in inp: stones[n] = stones.get(n, 0) + 1
    for _ in range(times):
        knowns = {}
        for n, stone in stones.items():
            if n == 0: knowns[1] = knowns.get(1, 0) + stone
            else:
                size = len(str(n))
                if size % 2:
                    res = 2024 * n
                    knowns[res] = knowns.get(res, 0) + stone
                else:
                    size //= 2
                    part1, part2 = int(str(n)[:size]), int(str(n)[size:])
                    knowns[part1] = knowns.get(part1, 0) + stone
                    knowns[part2] = knowns.get(part2, 0) + stone
        stones = knowns
    return sum(stones.values())

inp = list(map(int, map(str.strip, open("input.txt", "r").readlines()[0].split(" "))))
print(f"\nPart1: {blink(inp, 25)}\nPart2: {blink(inp, 75)}\n")
