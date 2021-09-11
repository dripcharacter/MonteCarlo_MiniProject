import random
import math
import sys
import matplotlib.pyplot as plt

# 실행 command line에서 parameter을 받아온다
needleLen = float(sys.argv[1])  # 바늘 크기
lineInterval = float(sys.argv[2])  # 선들의 간격
planeWid = float(sys.argv[3])  # 바닥의 너비
buffonTimes = int(sys.argv[4])  # BuffonTest의 parameter인 simulTimes를 몇 번할지


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


tmpList = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 40000, 90000, 160000, 250000, 360000, 490000,
           640000, 810000, 1000000, 4000000, 9000000, 16000000, 25000000]  # BuffonTest에 simulTimes에 들어갈 것들의 list
tmpLogList = []  # tmpList의 값을 log를 씌운 값들을 저장하는 list(visualization을 위한 log)
finalResultList = []  # tmpList속 entry로 나온 pi값들을 저장한 list
finalErrorList = []  # tmpList속 entry로 나온 pi값에 대한 error rate들을 저장한 list
# 각 entry라는 횟수만큼 바늘을 떨어뜨리는 BuffonTest를 buffonTimes만큼 반복하겠다는 반복문
for entry in tmpList:
    tmpLogList.append(math.log(entry))
    buffonResultList = []
    for i in range(buffonTimes):
        buffonResultList.append(BuffonTest(needleLen, lineInterval, planeWid, entry))
        print(i, "th simulation Result:", buffonResultList[i])

    simulResult = 0
    for result in buffonResultList:
        simulResult += result
    simulResult /= buffonTimes
    finalResultList.append(simulResult)
    finalErrorList.append(abs(math.pi - simulResult) / math.pi)
    print("simulation Result for", entry, "times throwing:", simulResult)
    print("error rate: ", abs(math.pi - simulResult) / math.pi)

# pi 결과 visualization
plt.plot(tmpList, finalResultList)  # x-axis: simulation times y-axis: pi value
plt.title("pi cal result")
plt.xlabel("n(times)")
plt.ylabel("pi")
plt.text(tmpList[-1], finalResultList[-1], str(finalResultList[-1]), fontsize=9, color="blue",
         horizontalalignment="center",
         verticalalignment="bottom")
plt.show()
plt.plot(tmpLogList, finalResultList)  # x-axis: log(simulation) times y-axis: pi value
plt.title("pi cal result")
plt.xlabel("log(n)(times)")
plt.ylabel("pi")
plt.text(tmpLogList[-1], finalResultList[-1], str(finalResultList[-1]), fontsize=9, color="blue",
         horizontalalignment="center",
         verticalalignment="bottom")
plt.show()
# pi Error rate 결과 visualization
plt.plot(tmpList, finalErrorList)  # x-axis: simulation times y-axis: error rate
plt.title("pi cal error result")
plt.xlabel("n(times)")
plt.ylabel("error")
plt.text(tmpList[-1], finalErrorList[-1], str(finalErrorList[-1]), fontsize=9, color="blue",
         horizontalalignment="center",
         verticalalignment="bottom")
plt.show()
# Error rate의 더 효과적인 visualization을 위해 log((error rate)^(-2))로 가공한다
finalErrorManufList = []
for error in finalErrorList:
    finalErrorManufList.append(math.log(1 / (error ** 2)))
plt.plot(tmpLogList, finalErrorManufList)  # x-axis: log(simulation) times y-axis: log((error rate)^(-2))
plt.title("pi cal error result")
plt.xlabel("log(n)(times)")
plt.ylabel("log(1/error^2)")
plt.text(tmpLogList[-1], finalErrorManufList[-1], str(finalErrorManufList[-1]), fontsize=9, color="blue",
         horizontalalignment="center",
         verticalalignment="bottom")
plt.show()
