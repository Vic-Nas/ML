inp = list(map(str.strip, open("input.txt", "r").readlines()))

prize = lambda tup: 3 * tup[0] + tup[1]
cut2 = lambda s: int(s[2:])

def check(inp, error = 0):
    i = 0
    res = []
    while i + 4 < len(inp):
        data = {"A": tuple(map(cut2, inp[i][10:].split(", "))), 
                "B": tuple(map(cut2, inp[i + 1][10:].split(", "))), 
                "P": tuple(map(cut2, inp[i + 2][7:].split(", ")))}
        den = data["A"][0] * data["B"][1] - data["B"][0] * data["A"][1]
        if den:
            a = (data["P"][0] + error) * data["B"][1] - (data["P"][1] + error) * data["B"][0]
            b = (data["P"][1] + error) * data["A"][0] - (data["P"][0] + error) * data["A"][1]
            if den and not a % den and not b % den: res.append((a // den, b // den))
        i += 4
    return res

res1 = filter(lambda tup: tup[0] <= 100 and tup[1] <= 100, check(inp))
res2 = check(inp, 10 ** 13)
print("\nPart1:", sum(prize(tup) for tup in res1), "\nPart2:", sum(prize(tup) for tup in res2))
print()