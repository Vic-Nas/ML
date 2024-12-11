#VN
from itertools import product
from tqdm import tqdm

def eval(expr):
    to_eval = expr.split()
    res = int(to_eval[0])
    for i in range(1, len(to_eval), 2):
        op, n = to_eval[i], int(to_eval[i + 1])
        if op == '+': res += n
        elif op == '*': res *= n
        elif op == '|': res = int(str(res) + str(n))
    return res

inp = list(map(lambda s : "".join(c if c.isdigit() else " " for c in s).split(), open("input.txt", "r")))
ops = [("Part1", "+*"), ("Part2", "+*|")]

#VN

for part, valid_ops in ops:
    res = 0
    for row in tqdm(inp, desc = part):
        goal = int(row[0])
        for combi in product(valid_ops, repeat = len(row) - 2):
            expr = f"{row[1]}"
            for i, op in enumerate(combi): expr += f" {op} {row[i + 2]}"
            if eval(expr) == goal : res += goal; break
    print(res)
    
#VN