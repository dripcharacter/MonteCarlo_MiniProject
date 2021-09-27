import random
import math
import ghalton


# n-차원의 초구와 초입방체로 hit-or-miss 테스트를 하는 함수
def htm_for_multi_dim_sampling(dim, radius, simulTimeList):
    touchedTimes = 0  # 바늘이 몇 번 선에 닿았는지 저장하는 변수
    tmpResultList = []
    for i in range(simulTimeList[-1]):  # simulTimes[-1]만큼 시뮬레이션을 한다
        randCoordList = []
        for _ in range(dim):  # n개의 랜덤 변수로 n차원 좌표를 생성한다
            randCoordList.append(random.uniform(-radius, radius))

        tmpDistance = 0
        for coord in randCoordList:
            tmpDistance += coord ** 2

        if tmpDistance <= radius ** 2:
            print("Success:", i, "번째 좌표는", dim, "차원 초구의 안에 들어갔습니다.")
            touchedTimes += 1
        else:
            print("Failure:", i, "번째 좌표는", dim, "차원 초구의 안에 들어가지 못했습니다.")

        # simulTimeList에 있는 순간마다 중간 결과를 기록한다
        if (i + 1) in simulTimeList:
            quotient = 0
            simulatedPi = 0
            if dim % 2 == 0:  # 초구의 초부피 계산은 감마함수가 있기 때문에 홀수일때와 짝수일때 계산 결과가 달라진다
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

    # 언제 기록했는지와 기록한 결과를 리턴한다
    return simulTimeList, tmpResultList
