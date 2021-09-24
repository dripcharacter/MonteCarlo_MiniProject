import random
import math
import ghalton


def htm_for_multi_dim_sampling(dim, radius, simulTimes):
    touchedTimes = 0
    for i in range(simulTimes):
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

    quotient = 0
    simulatedPi = 0
    if dim % 2 ==0:
        quotient = dim // 2
        tmpProduct = 1
        for i in range(1, quotient + 1):
            tmpProduct *= i
        simulatedPi = ((touchedTimes * tmpProduct * (4 ** quotient)) / touchedTimes) ** (1 / quotient)
    else:
        quotient = dim //2
        tmpProduct = 1
        for i in range(quotient):
            tmpProduct *= (2 * i + 1)
        simulatedPi = ((touchedTimes * tmpProduct * (2 ** (quotient - 1))) / simulTimes) ** (1 / (quotient - 1))

    print("확률:", touchedTimes / simulTimes)
    return simulatedPi
