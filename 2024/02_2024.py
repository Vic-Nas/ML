#VN

def safe(report):
    inc = report[1] - report[0] > 0
    for i in range(len(report) - 1) :
        diff = report[i + 1] - report[i]
        if not (0 < abs(diff) < 4) or (diff > 0 and not inc) or (diff < 0 and inc): 
            return False
    return True
  
res1, res2 = 0, 0
for row in open("input.txt", "r").readlines() :
    report = list(map(int, row.split()))
    if safe(report): res1 += 1
    for i in range(-1, -len(report)-1, -1):
        minus = report.copy()
        minus.pop(i)
        if safe(minus): 
            res2 += 1
            break 

print(f"\nPart1: {res1}\nPart2: {res2}\n")
#VN
