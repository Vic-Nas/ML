X, Y = 101, 103

class Point:
    def __init__(self, t1, t2 = (0, 1)):
        self.x, self.y = t1
        self.dx, self.dy = t2
    
    def next(self, dx = 0, dy = 0): 
        if not (dx or dy): dx, dy = self.dx, self.dy
        return Point(((self.x + dx) % X, (self.y + dy) % Y), (self.dx, self.dy))
    
    def quadrant(self):
        if 0 <= self.y < Y // 2:
            if 0 <= self.x < X // 2: return 1
            elif self.x > X // 2: return 2
        elif self.y > Y // 2:
            if 0 <= self.x < X // 2: return 3
            elif self.x > X // 2: return 4
    
    def __eq__(self, other): return self.x == other.x and self.y == other.y
    
def display(points):
    map = [[" "] * X for _ in range(Y)]
    for p in points: map[p.y][p.x] = "*"
    print("\n".join("".join(row) for row in map))

def look_like_sapin(points):
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

for i in range(10000):
    points = list(map(Point.next, points))
    if look_like_sapin(points):
        print("Part2:", i + 1, "\n")
        break

# display(points)