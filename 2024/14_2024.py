# Bruteforce pypy < 0.1s python < 4mins

X, Y = 101, 103

class Point:
    def __init__(self, t1 = (0, 0), t2 = (1, 0)):
        self.x, self.y = t1
        self.dx, self.dy = t2
    
    def next(self): 
        return Point(((self.x + self.dx) % X, (self.y + self.dy) % Y), (self.dx, self.dy))
    
    def quadrant(self):
        if 0 <= self.y < Y // 2:
            if 0 <= self.x < X // 2: return 1
            elif self.x > X // 2: return 2
        elif self.y > Y // 2:
            if 0 <= self.x < X // 2: return 3
            elif self.x > X // 2: return 4
    
    def __eq__(self, other): return self.x == other.x and self.y == other.y
    
def display(points, ui = 0):
    if not ui:
        map = [[" "] * X for _ in range(Y)]
        for p in points: map[p.y][p.x] = "*"
        print("\n".join("".join(row) for row in map))
    else:
        import matplotlib.pyplot as plt
        import warnings
        warnings.filterwarnings("ignore", category = UserWarning)

        x = [p.x for p in points]
        y = [-p.y for p in points]
        _, ax = plt.subplots(figsize = (5, 9))
        ax.set_yticklabels([f"{abs(tick)}" for tick in y])
        ax.set(title = "Christmas Tree", xlabel = "x", ylabel = "y")
        ax.scatter(x, y, marker = "*", c = "green")
        plt.show()

def looks_like_sapin(points):
    for p in points:
        #   *
        x = p.x; y = p.y
        #  ***
        base_1 = Point((x + 1, y - 1)), Point((x + 1, y)), Point((x + 1, y + 1)) 
        # *****
        base_2 = Point((x + 2, y - 2)), Point((x + 2, y - 1)), Point((x + 2, y)), Point((x + 2, y + 1)), Point((x + 2, y + 2))

        if all(p in points for p in base_1 + base_2): return True
    
    return False
            
sep = lambda s: s.strip()[2:].split(" v=")
inp = map(sep, open("input.txt", "r").readlines())

points = [Point(tuple(map(int, t[0].split(","))), tuple(map(int, t[1].split(",")))) for t in inp]

the_map = points.copy()
for i in range(100):
    the_map = list(map(Point.next, the_map))
    quadrants = {}
    for point in the_map:
        q = point.quadrant()
        if q: quadrants[q] = quadrants.get(q, 0) + 1
print("\nPart1:", eval("*".join(map(str, quadrants.values()))))

the_map = points.copy()
count = 0
while True:
    count += 1
    the_map = list(map(Point.next, the_map))
    if looks_like_sapin(the_map):
        print("Part2:", count, "\n")
        break

display(the_map, ui = 1)