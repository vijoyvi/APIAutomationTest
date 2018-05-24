import math


class Solver:

    def demo(self, a, b, c):
        print "Testing the Version Control System Options"
        print "Adding a line from the Git HUb"
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            print "Adding a second line from the Git HUb"
            return root1, root2
        elif d == 0:
            return -b / (2 * a)
        else:
            return "This equation has no roots"

        print "Trying to add a line and commit"

        print "Revert FIrst Change"


if __name__ == '__main__':
    solver = Solver()

while True:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    result = solver.demo(a, b, c)
    print(result)
