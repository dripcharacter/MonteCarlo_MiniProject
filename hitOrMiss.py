import random
import math
from regularPolygon import RegularPolygon
import numpy as np
import matplotlib.pyplot as plt


def makeRegularPolygon(angleNum, radius):
    regPolygon = RegularPolygon()
    distFromCenter = radius / abs(math.cos(math.pi / angleNum))

    for i in range(angleNum):
        angle = (math.pi / 2) - (2 * i) * (2 * math.pi) / (2 * angleNum)
        xCoord = distFromCenter * math.cos(angle)
        yCoord = distFromCenter * math.sin(angle)
        regPolygon.append_coord(xCoord, yCoord)

    return regPolygon.get_xList_yList()


def HitOrMissSampling(angleNum, radius, simulTimeList):
    touchedTimes = 0
    tmpResultList = []

    for i in range(simulTimeList[-1]):
        randXCoord = random.triangular(0, radius, radius)
        randYCoord = random.uniform(0, randXCoord * math.tan(math.pi / angleNum))
        if radius ** 2 < randXCoord ** 2 + randYCoord ** 2:
            print("Failure:", i, "번째 바늘은 원 안에 들어가지 못했습니다.")
        else:
            print("Success:", i, "번째 바늘은 원 안에 들어갔습니다.")
            touchedTimes += 1

        if (i + 1) in simulTimeList:
            tmpResultList.append((touchedTimes * angleNum * math.tan(math.pi / angleNum)) / (i + 1))
    return simulTimeList, tmpResultList
