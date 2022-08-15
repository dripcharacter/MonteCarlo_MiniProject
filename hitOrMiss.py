import random
import math
from regularPolygon import RegularPolygon

# 정n각형의 각 꼭짓점 좌표를 찍는 함수(현재는 hit-or-miss를 바꾸면서 사용하지 않게 됨)
def makeRegularPolygon(angleNum, radius):
    regPolygon = RegularPolygon()
    distFromCenter = radius / abs(math.cos(math.pi / angleNum))

    for i in range(angleNum):
        angle = (math.pi / 2) - (2 * i) * (2 * math.pi) / (2 * angleNum)
        xCoord = distFromCenter * math.cos(angle)
        yCoord = distFromCenter * math.sin(angle)
        regPolygon.append_coord(xCoord, yCoord)

    return regPolygon.get_xList_yList()


# hit-or-miss 테스트를 하는 함수
# 정n각형은 2n개의 직각삼각형으로 이루어져 있다.
# 중심각이 180/n 도이며 이 직각삼각형과 180/n 도의 부채꼴로 테스트를 한다
def HitOrMissSampling(angleNum, radius, simulTimeList):
    touchedTimes = 0  # 바늘이 몇 번 선에 닿았는지 저장하는 변수
    tmpResultList = []

    for i in range(simulTimeList[-1]):  # simulTimes[-1]만큼 시뮬레이션을 한다
        randXCoord = random.triangular(0, radius, radius)  # 직각삼각형이니 radius로 갈수록 더 자주 나오도록 random.trianagular을 사용한다
        randYCoord = random.uniform(0, randXCoord * math.tan(math.pi / angleNum))
        if radius ** 2 < randXCoord ** 2 + randYCoord ** 2:
            print("Failure:", i, "번째 바늘은 원 안에 들어가지 못했습니다.")
        else:
            print("Success:", i, "번째 바늘은 원 안에 들어갔습니다.")
            touchedTimes += 1

        # simulTimeList에 있는 순간마다 중간 결과를 기록한다
        if (i + 1) in simulTimeList:
            tmpResultList.append((touchedTimes * angleNum * math.tan(math.pi / angleNum)) / (i + 1))
    # 언제 기록했는지와 기록한 결과를 리턴한다
    return simulTimeList, tmpResultList
