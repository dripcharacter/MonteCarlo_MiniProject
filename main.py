import random
import math
import sys
import matplotlib.pyplot as plt
import pandas as pd

needleLen = float(sys.argv[1])
lineInterval = float(sys.argv[2])
planeWid = float(sys.argv[3])
simulTimes = int(sys.argv[4])
buffonTimes = int(sys.argv[5])


def BuffonTest(needleLen, lineInterval, planeWid, simulTimes):
    touchedTimes = 0
    for i in range(simulTimes):
        needlePos = random.uniform(0, planeWid)
        needleTheta = random.uniform(0, math.pi)

        if needleTheta < math.pi / 2:
            needlePos += abs(needleLen / 2 * math.cos(needleTheta))
        else:
            needlePos -= abs(needleLen / 2 * math.cos(needleTheta))

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

        if (needleLen / 2) * abs(math.cos(needleTheta)) >= abs(closestLine - needlePos):
            touchedTimes += 1
            print("Success:", i, "번째 바늘은 선에 닿았습니다.")
        else:
            print("Failure:", i, "번째 바늘은 선에 닿지 못했습니다.")

    print("확률:", touchedTimes / simulTimes)
    return (2 * simulTimes * needleLen) / (touchedTimes * lineInterval)


tmpList = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 40000, 90000, 160000, 250000, 360000, 490000, 640000, 810000, 1000000, 4000000]
tmpLogList = []
finalResultList = []
finalErrorList = []
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
    print("simulation Result for", simulTimes, "times throwing:", simulResult)
    print("error rate: ", abs(math.pi - simulResult) / math.pi)

plt.plot(tmpList, finalResultList)
plt.title("pi cal result")
plt.xlabel("n(times)")
plt.ylabel("pi")
# for i, v in enumerate(tmpList):
#     plt.text(v, finalResultList[i], str(finalResultList[i]), fontsize=9, color="blue", horizontalalignment="center",
#              verticalalignment="bottom")
plt.show()
plt.plot(tmpLogList, finalResultList)
plt.title("pi cal result")
plt.xlabel("log(n)(times)")
plt.ylabel("pi")
# for i, v in enumerate(tmpLogList):
#     plt.text(v, finalResultList[i], str(finalResultList[i]), fontsize=9, color="blue", horizontalalignment="center",
#              verticalalignment="bottom")
plt.show()

plt.plot(tmpList, finalErrorList)
plt.title("pi cal error result")
plt.xlabel("n(times)")
plt.ylabel("error")
# for i, v in enumerate(tmpList):
#     plt.text(v, finalErrorList[i], str(finalErrorList[i]), fontsize=9, color="blue", horizontalalignment="center",
#              verticalalignment="bottom")
plt.show()

finalErrorManufList = []
for error in finalErrorList:
    finalErrorManufList.append(math.log(1 / (error ** 2)))
plt.plot(tmpLogList, finalErrorManufList)
plt.title("pi cal error result")
plt.xlabel("log(n)(times)")
plt.ylabel("log(1/error^2)")
# for i, v in enumerate(tmpLogList):
#     plt.text(v, finalErrorManufList[i], str(finalErrorManufList[i]), fontsize=9, color="blue", horizontalalignment="center",
#              verticalalignment="bottom")
plt.show()
