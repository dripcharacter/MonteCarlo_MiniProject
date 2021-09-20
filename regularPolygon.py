import math

class RegularPolygon:

    def __init__(self):

        self.xCoordList = list()
        self.yCoordList = list()

    def append_coord(self, xCoord, yCoord):
        self.xCoordList.append(xCoord)
        self.yCoordList.append(yCoord)

    def get_xList_yList(self):
        return self.xCoordList, self.yCoordList
