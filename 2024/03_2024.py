#VN
memory = ""
for row in open("input.txt", "r") : memory += row

def prod(array):
    res = 1
    for el in array : res *= el
    return res

res1, res2, dont, do = 0, 0, 0, 0
for i in range(len(memory)):
    if memory[i:i + 7] == "don't()" : dont = 1
    if memory[i:i + 4] == "do()" : do = 1
    if memory[i:i + 4] == "mul(" :
        index = i + 4
        curr = ""
        while memory[index] != ")" :
            if not (memory[index].isdigit() or memory[index] == ",") : break
            else : curr += memory[index]
            index += 1
        else : 
            curr = list(map(int, curr.split(",")))
            if len(curr) == 2 and all(x <= 999 for x in curr) : 
                if do : dont, do = 0, 0
                p = prod(curr)
                res1 += p
                res2 += 0 if dont else p
        
print(f"\nPart1: {res1}\nPart2: {res2}\n")

#VN
