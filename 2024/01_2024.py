#VN
l1, l2 = [], []

def divide(row): 
    val1, val2 = row.split()
    global l1, l2
    l1.append(int(val1)); l2.append(int(val2))
    
list(map(divide, open("input.txt", "r")))
l1.sort()
l2.sort()

res1 = sum(abs(l1[i] - l2[i]) for i in range(len(l1)))
res2 = sum(el * l2.count(el) for el in l1)
print(f"\nPart1: {res1}\nPart2: {res2}\n")
#VN
