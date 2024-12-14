cut2 = lambda s: int(s[2:])

def check(inp, error = 0):
    i = 0; res = []
    while i < len(inp):
        data = {"A": tuple(map(cut2, inp[i][10:].split(", "))),
                "B": tuple(map(cut2, inp[i + 1][10:].split(", "))), 
                "P": tuple(map(cut2, inp[i + 2][7:].split(", ")))}
        den = data["A"][0] * data["B"][1] - data["B"][0] * data["A"][1]
        
        if den:
            a = (data["P"][0] + error) * data["B"][1] - (data["P"][1] + error) * data["B"][0]
            b = (data["P"][1] + error) * data["A"][0] - (data["P"][0] + error) * data["A"][1]
            if not (a % den or b % den): res.append((a // den, b // den))
        i += 4
    return res

inp = list(map(str.strip, open("input.txt", "r").readlines()))
prize = lambda t: 3 * t[0] + t[1]
inf100 = lambda t: t[0] <= 100 and t[1] <= 100

print("\nPart1:", sum(prize(tup) for tup in filter(inf100, check(inp))))
print("Part2:", sum(prize(tup) for tup in check(inp, 10 ** 13)), "\n")