import random
import math

# Buffon needle 시뮬레이션 함수
def BuffonTest(needleLen, lineInterval, planeWid, simulTimes):
    touchedTimes = 0  # 바늘이 몇 번 선에 닿았는지 저장하는 변수
    for i in range(simulTimes):  # simulTimes만큼 바늘을 떨어뜨린다
        needlePos = random.uniform(0, planeWid)  # 바늘이 처음 바닥에 닿는 위치
        needleTheta = random.uniform(0, math.pi)  # 바늘이 어느 방향으로 넘어지는지 각도(x축 1사분면을 기준으로)

        # needleTheta가 90도를 넘느냐 아니냐를 기준으로 needle middle point의 위치를 어떻게 설정하는지
        if needleTheta < math.pi / 2:
            needlePos += abs(needleLen / 2 * math.cos(needleTheta))
        else:
            needlePos -= abs(needleLen / 2 * math.cos(needleTheta))

        # 가장 가까운 선이 어디인지를 설정한다
        closestLine = 0
        if needlePos < 0:
            closestLine = 0
        elif needlePos % lineInterval < lineInterval / 2:
            closestLine = needlePos // lineInterval * lineInterval
        else:
            if needlePos // lineInterval * lineInterval + lineInterval <= planeWid:
                closestLine = needlePos // lineInterval * lineInterval + lineInterval
            else:
                closestLine = needlePos // lineInterval * lineInterval

        # closestLine과 needle이 만나지 않았으면 다른 line과도 만나지 않을것이기 때문에 closestLine으로 needle의 crossing 여부를 판단
        if (needleLen / 2) * abs(math.cos(needleTheta)) >= abs(closestLine - needlePos):
            touchedTimes += 1
            print("Success:", i, "번째 바늘은 선에 닿았습니다.")
        else:
            print("Failure:", i, "번째 바늘은 선에 닿지 못했습니다.")

    print("확률:", touchedTimes / simulTimes)
    return (2 * simulTimes * needleLen) / (touchedTimes * lineInterval)