from a_star import *
from triangolo import *


if __name__ == '__main__':
    g = GridWithWeights(15, 15, DIAGRAM1_WALLS)
    tr = Triangle((1,1), (2,2), (0,3))
    tr2 = Triangle((3,3), (4,4), (2,5))
    tr3 = Triangle((4,3), (7,10), (11,2))
    g.modify_walls(make_triagle_obstacle(g, tr, tr2, tr3))

    x_st = int(input("inserisci x dello start: "))
    y_st = int(input("inserisci y dello start: "))

    while (x_st, y_st) in g.walls:
        x_st = int(input("inserisci x dello start: "))
        y_st = int(input("inserisci y dello start: "))

    st = (x_st, y_st)

    x_gl = int(input("inserisci x dell'arrivo: "))
    y_gl = int(input("inserisci y dell'arrivo: "))

    while (x_gl, y_gl) in g.walls:
        x_gl = int(input("inserisci x dell'arrivo: "))
        y_gl = int(input("inserisci y dell'arrivo: "))

    gl = (x_gl, y_gl)

    came_from, cost_so_far = a_star_search(g, st, gl)
    draw_grid(g, width=3, point_to=came_from, start=st, goal=gl)
    print()
    draw_grid(g, width=3, number=cost_so_far, start=st, goal=gl)
    print()
    path = reconstruct_path(came_from, start=st, goal=gl)
    draw_grid(g, width=3, path=path)
    print("- Costo del percorso ({})".format(calculate_path_cost(path, cost_so_far)))

