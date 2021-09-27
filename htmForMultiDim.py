import random
import math
import ghalton


def htm_for_multi_dim_sampling(dim, radius, simulTimeList):
    touchedTimes = 0
    tmpResultList = []
    for i in range(simulTimeList[-1]):
        randCoordList = []
        for _ in range(dim):
            randCoordList.append(random.uniform(-radius, radius))

        tmpDistance = 0
        for coord in randCoordList:
            tmpDistance += coord ** 2

        if tmpDistance <= radius ** 2:
            print("Success:", i, "번째 좌표는", dim, "차원 초구의 안에 들어갔습니다.")
            touchedTimes += 1
        else:
            print("Failure:", i, "번째 좌표는", dim, "차원 초구의 안에 들어가지 못했습니다.")

        if (i + 1) in simulTimeList:
            quotient = 0
            simulatedPi = 0
            if dim % 2 == 0:
                quotient = dim // 2
                tmpProduct = 1
                for tmpNum in range(1, quotient + 1):
                    tmpProduct *= tmpNum
                simulatedPi = ((touchedTimes * tmpProduct * (4 ** quotient)) / (i + 1)) ** (1 / quotient)
            else:
                quotient = dim // 2 + 1
                tmpProduct = 1
                for tmpNum in range(quotient):
                    tmpProduct *= (2 * tmpNum + 1)
                simulatedPi = ((touchedTimes * tmpProduct * (2 ** (quotient - 1))) / (i + 1)) ** (1 / (quotient - 1))
            tmpResultList.append(simulatedPi)

    print("quotient:", dim // 2)

    print(touchedTimes/simulTimeList[-1])
    print(tmpResultList[-1])
    return simulTimeList, tmpResultList
