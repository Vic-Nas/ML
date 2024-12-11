#VN
def check(to_check, orders):
    for i in range(len(orders)) :
        if orders[i][0] in to_check and orders[i][1] in to_check :
            if to_check.index(orders[i][0]) >= to_check.index(orders[i][1]) : 
                return False
    return True

def sorter(to_sort, orders):
    res = []
    left = to_sort.copy()
    while left:
        for element in left:
            if all(element != b or b not in left
                for a, b in orders
                if a in left and b in left):
                res.append(element)
                left.remove(element)
                break
    return res

#VN

inp = list(map(lambda row: row.split(), open("input.txt", "r")))

for i in range(len(inp)):
    if not inp[i]:
        orders = list(map(lambda row : row[0].split("|"), inp[:i]))
        updates = list(map(lambda row : row[0].split(","), inp[i+1:]))
        break

res1, res2 = 0, 0
for update in updates :
    if check(update, orders) : res1 += int(update[len(update) // 2])
    else : res2 += int(sorter(update, orders)[len(update) // 2])

print(f"\nPart1: {res1}\nPart2: {res2}\n")

#VN
