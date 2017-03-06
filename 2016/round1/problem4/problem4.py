from collections import namedtuple
file = open("DATA41.txt")
Point = namedtuple("Point", "x y")
Building = namedtuple("Building", "x y Party")


def distSqrtd(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def test_case():
    # Our town array
    # Point (200, 200) is the origin
    town = [["" for x in range(401)] for y in range(401)]

    area_x, area_y = map(int, file.readline().split())

    # Populate build locs with locations within the range of the r = 50 circle
    build_locs = []
    for x in range(-200, 201):
        for y in range(-200, 201):
            if distSqrtd(x, y, area_x, area_y) <= 50 ** 2:
                build_locs.append(Point(x, y))

    buildings = []
    for i in range(100):
        x, y, party = file.readline().split()
        x = int(x)
        y = int(y)
        buildings.append(Building(x, y, party))

    d = 0.0
    r = 0.0
    for loc in build_locs:
        buildings = sorted(buildings, key=lambda building: distSqrtd(building[0], building[1], loc[0], loc[1]))
        neighbours = [None] * 3
        neighbours[0] = buildings[0]
        neighbours[1] = buildings[1]
        neighbours[2] = buildings[2]

        # Extra neighbours
        dist = distSqrtd(loc[0], loc[1], neighbours[2][0], neighbours[2][1])
        for i in range(0, len(buildings)):
            if i < 3:
                continue
            if distSqrtd(loc[0], loc[1], buildings[i][0], buildings[i][1]) == dist:
                neighbours.append(buildings[i])

        num_d = 0
        num_r = 0
        for neighbour in neighbours:
            if neighbour[2] == "D":
                num_d += 1
            else:
                num_r += 1

        if num_d >= num_r:
            d += 1.0
        else:
            r += 1.0

    print("{0:.3g}".format(d*100/(d+r)))





for case in range(10):
    test_case()
