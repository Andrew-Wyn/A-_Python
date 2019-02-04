import math

# ------------ 
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def get_points(self):
        return {self.p1, self.p2, self.p3}
    
    def get_linears(self):
        return [(self.p1, self.p2), (self.p2, self.p3), (self.p1, self.p3)]

def make_triagle_obstacle(graph, *triangles):

    DIAGRAM1_WALLS = set()
    
    list(triangles)
    for triangle in triangles:
        points = triangle.get_points()
        linears = triangle.get_linears()

        delimits = []

        i = 0

        for line in linears:
            delimits.append(set())
            p_prim = points.difference(line).pop()
            for y in range(graph.height):
                for x in range(graph.width):
                    to_ins = False
                    coef = (line[0][1] - line[1][1]) / (line[0][0] - line[1][0])
                    funx = (coef*x) - (coef*line[0][0]) + line[0][1]
                    if p_prim[1] > (coef*p_prim[0]) - (coef*line[0][0]) + line[0][1]:
                        if y >= math.floor(funx):
                            to_ins = True
                    else:
                        if y <= math.floor(funx):
                            to_ins = True

                    if to_ins:
                        delimits[i].add((x,y))
            i+=1
        
        DIAGRAM1_WALLS = DIAGRAM1_WALLS.union(delimits[0].intersection(delimits[1], delimits[2]))

    return list(DIAGRAM1_WALLS)