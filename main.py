import random
import math
import sys
import matplotlib.pyplot as plt

needleLen = float(sys.argv[1])
lineInterval = float(sys.argv[2])
planeWid = float(sys.argv[3])
simulTimes = int(sys.argv[4])
buffonTimes = int(sys.argv[5])


def BuffonTest(needleLen, lineInterval, planeWid, simulTimes):
    touchedTimes = 0
    # resultList = []
    # rangeList = list(range(simulTimes//100, simulTimes, simulTimes//100))
    for i in range(simulTimes):
        needlePos = random.uniform(0, planeWid)
        print("planeWid:", needlePos)
        needleTheta = random.uniform(0, math.pi)
        print("Theta:", needleTheta)

        closestLine = 0
        if needlePos % lineInterval < lineInterval / 2:
            closestLine = needlePos // lineInterval * lineInterval
        else:
            if needlePos // lineInterval * lineInterval + lineInterval <= planeWid:
                closestLine = needlePos // lineInterval * lineInterval + lineInterval
            else:
                closestLine = needlePos // lineInterval * lineInterval

        if (needleLen / 2) * math.sin(needleTheta) >= abs(closestLine - needlePos):
            touchedTimes += 1
            print("Success:", i, "번째 바늘은 선에 닿았습니다.")
        else:
            print("Failure:", i, "번째 바늘은 선에 닿지 못했습니다.")

        # if i in rangeList:
        #     resultList.append(touchedTimes / i)

    # plt.plot(rangeList, resultList)
    # plt.show()

    print("확률:", touchedTimes / simulTimes)
    return (2 * simulTimes * needleLen) / (touchedTimes * lineInterval)

tmpList = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 40000, 90000, 160000, 250000, 360000, 490000, 640000, 810000, 1000000]
finalResultList = []
for entry in tmpList:
    buffonResultList = []
    for i in range(buffonTimes):
        buffonResultList.append(BuffonTest(needleLen, lineInterval, planeWid, entry))
        print(i, "th simulation Result:", buffonResultList[i])

    simulResult = 0
    for result in buffonResultList:
        simulResult += result
    simulResult /= buffonTimes
    finalResultList.append(simulResult)
    print("simulation Result for", simulTimes, "times throwing:", simulResult)
    print("error rate: ", abs(math.pi - simulResult) / math.pi)
    print(math.pi)

plt.plot(tmpList, finalResultList)
plt.show()
