from Line import Line
from Point import Point

class Cube:
    def __init__(self):
        self.points = []
        self.points.append(Point(0,0,0))
        self.points.append(Point(0,100,0))
        self.points.append(Point(100,100,0))
        self.points.append(Point(100,0,0))
        self.points.append(Point(0,0,100))
        self.points.append(Point(0,100,100))
        self.points.append(Point(100,100,100))
        self.points.append(Point(100,0,100))

        self.lines = []

        self.createLines()

    def createLines(self):
        #Front Face
        self.lines.append(Line(self.points[0], self.points[1]))
        self.lines.append(Line(self.points[1], self.points[2]))
        self.lines.append(Line(self.points[2], self.points[3]))
        self.lines.append(Line(self.points[3], self.points[0]))

        #Back Face
        self.lines.append(Line(self.points[4], self.points[5]))
        self.lines.append(Line(self.points[5], self.points[6]))
        self.lines.append(Line(self.points[6], self.points[7]))
        self.lines.append(Line(self.points[7], self.points[4]))

        #Connecting Lines
        self.lines.append(Line(self.points[0], self.points[4]))
        self.lines.append(Line(self.points[1], self.points[5]))
        self.lines.append(Line(self.points[2], self.points[6]))
        self.lines.append(Line(self.points[3], self.points[7]))

    #To transform the Cube
    def transform(self, angle, axis):

        for point in self.points:
            point.transform(angle, axis)

        self.lines = []

        self.createLines()

    # To Find New Corner Points:
    # In an Orthographic view, if the faces aren't parallel to the X-Y-Z Planes, the Nearest and the Farthest point from the screen do not form Corner points. 
    # So, we find the set of nearest and furthest points from the screen (Which is along the Z axis), and not include them in the List of Corner Points.
    def findCornerPoints(self):
        points = []
        zs = self.zArray()
        zs = sorted(zs)

        if(len(zs) > 2):
            for point in self.points:
                if(point.z != zs[0] and point.z != zs[-1]):
                    points.append(point)
        else:
            for point in self.points:
                if(point.z != zs[0]):
                    points.append(point)

        return points

    # To Find the unique Z values of all the vertices.
    def zArray(self):
        zs = {0}
        for point in self.points:
            zs.add(point.z)

        return zs