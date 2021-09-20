import random
import math
import sys
import matplotlib.pyplot as plt
import buffonTest
import hitOrMiss

# 실행 command line에서 parameter을 받아온다
needleLen = float(sys.argv[1])  # 바늘 크기
lineInterval = float(sys.argv[2])  # 선들의 간격
planeWid = float(sys.argv[3])  # 바닥의 너비
buffonTimes = int(sys.argv[4])  # BuffonTest의 parameter인 simulTimes를 몇 번할지

tmpList = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 40000, 90000]  # BuffonTest에 simulTimes에 들어갈 것들의 list
tmpLogList = []  # tmpList의 값을 log를 씌운 값들을 저장하는 list(visualization을 위한 log)
finalResultList = []  # tmpList속 entry로 나온 pi값들을 저장한 list
finalErrorList = []  # tmpList속 entry로 나온 pi값에 대한 error rate들을 저장한 list
# 각 entry라는 횟수만큼 바늘을 떨어뜨리는 BuffonTest를 buffonTimes만큼 반복하겠다는 반복문
for entry in tmpList:
    tmpLogList.append(math.log(entry))
    buffonResultList = []
    for i in range(buffonTimes):
        buffonResultList.append(buffonTest.BuffonTest(needleLen, lineInterval, planeWid, entry))
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
