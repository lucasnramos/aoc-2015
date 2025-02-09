'''

--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and
then an elf at the North Pole calls him via radio and tells him where to move
next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his
new location.

However, the elf back at the north pole has had a little too much eggnog, and
so his directions are a little off, and Santa ends up visiting some houses more
than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to
    the east. ^>v< delivers presents to 4 houses in a square, including twice
    to the house at his starting/ending location. ^v^v^v^v^v delivers a bunch
    of presents to some very lucky children at only 2 houses.
'''


file_path = "03/input.txt"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointList:
    def __init__(self):
        self.point_list = []

    def check_point(self,point):
        for p in self.point_list:
            if p.x == point.x and p.y == point.y:
                return False
        return True

    def add_point(self, point):
        self.point_list.append(point)

def my_func(contents):
    x = 0
    y = 0
    counter = 1
    points = PointList()

    for c in contents:
        match c:
            case "^":
                y += 1
            case ">":
                x += 1
            case "v":
                y -= 1
            case "<":
                x -= 1
        point = Point(x, y)
        if points.check_point(point):
            points.add_point(point)
            counter += 1
    
    print(counter)

def main_one():
    with open(file_path, 'r') as f:
        content = f.read()
    my_func(content)

main_one()

'''
Your puzzle answer was 2592.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.


'''