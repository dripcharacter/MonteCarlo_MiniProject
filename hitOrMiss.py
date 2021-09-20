import random
import math
from regularPolygon import RegularPolygon


def makeRegularPolygon(angleNum, radius):
    regPolygon = RegularPolygon()
    distFromCenter = radius / abs(math.cos(math.pi / angleNum))
    for i in range(angleNum):
        angle = (math.pi / 2) - (2 * i) * (2 * math.pi) / (2 * angleNum)
        xCoord = distFromCenter * math.cos(angle)
        yCoord = distFromCenter * math.sin(angle)
        regPolygon.append_coord(xCoord, yCoord)

    return regPolygon.get_xList_yList()


def HitOrMissSampling(angleNum, radius, xCoordList, yCoordList, simulTimes):
    highestYCoord = 0
    lowestYCoord = 0
    for yCoord in yCoordList:
        if highestYCoord < yCoord:
            highestYCoord = yCoord
        if lowestYCoord > yCoord:
            lowestYCoord = yCoord

    touchedTimes = 0
    for i in range(simulTimes):
        touchedBool = False
        randYCoord = random.uniform(lowestYCoord, highestYCoord)

        posIdx = 0
        for yCoord in yCoordList:
            if randYCoord >= yCoord:
                posIdx = yCoordList.index(yCoord)

        ratio = 0
        if posIdx - 1 > 0:
            ratio = (randYCoord - yCoordList[posIdx - 1]) / (yCoordList[posIdx] - yCoordList[posIdx - 1])
        else:
            touchedBool = True

        if touchedBool:
            print("Failure:", i, "번째 바늘은 원 안에 들어가지 못했습니다.")
            continue

        xPosBound = (ratio * xCoordList[posIdx]) + ((1 - ratio) * xCoordList[posIdx - 1])
        randXCoord = random.uniform(-xPosBound, xPosBound)

        if radius ** 2 < randXCoord ** 2 + randYCoord ** 2:
            print("Failure:", i, "번째 바늘은 원 안에 들어가지 못했습니다.")
        else:
            print("Success:", i, "번째 바늘은 원 안에 들어갔습니다.")
            touchedTimes += 1

    print("확률:", touchedTimes / simulTimes)
    return (touchedTimes * angleNum * math.tan(math.pi / angleNum)) / simulTimes
