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

    def transform(self, angle, axis):

        for point in self.points:
            point.transform(angle, axis)

        self.lines = []

        self.createLines()

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


    def zArray(self):
        zs = {0}
        for point in self.points:
            zs.add(point.z)

        return zs