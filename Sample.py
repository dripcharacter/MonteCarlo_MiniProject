import ghalton
import time
import matplotlib.pyplot as plt
import hitOrMiss
import math
import htmForMultiDim
sequencer = ghalton.GeneralizedHalton(2, 68)
points = sequencer.get(1000)
now = time.localtime()
currentTime = str(now.tm_year) + "-" + str(now.tm_mon) + "-" + str(now.tm_mday) + "_" + str(now.tm_hour) + "-" + str(now.tm_min) + "-" + str(now.tm_sec)
print(currentTime)

# plt.plot([1, 2, 3, 4], [2, 3, 5, 10], [1, 2, 3, 4], [3, 5, 9, 7])
# plt.legend(labels=list(["a", "b"]))
# plt.show()
# xCoordList, yCoordList = hitOrMiss.makeRegularPolygon(5, 10)
# print(xCoordList)
# print(yCoordList)
#
# for i in range(len(xCoordList)):
#     print((xCoordList[i]**2+yCoordList[i]**2)**(1/2))
# print(math.cos(math.pi/2))
# hitOrMiss.HitOrMissSampling(4, 10, [1000000])
# htmForMultiDim.htm_for_multi_dim_sampling(2, 10, [1000000])

# def func(num, *xargs):
#     print(num)
#     for i in range(len(xargs)//3):
#         print(xargs[3*i])
#         print(xargs[3*i+1])
#         print(xargs[3*i+2])
#
# func(3, ["x1"], ["y1"], ["title1"], ["x2"], ["y2"], ["title2"], ["x3"], ["y3"], ["title3"])
#
# def make_multi_plot_file(title, x_label, y_label, *x_y_label_args):
#     plt.clf()
#     for index in range(len(x_y_label_args) //3):
#         plt.plot(x_y_label_args[3 * index], x_y_label_args[3 * index + 1], label = str(x_y_label_args[3 * index + 2]))
#     plt.title(str(title))
#     plt.xlabel(str(x_label))
#     plt.ylabel(str(y_label))
#     plt.legend()
#     plt.show()
#
# make_multi_plot_file("title", "num", "pi", [1, 2, 3, 4], [2, 3, 5, 10], "graph1", [1, 2, 3, 4], [3, 5, 9, 7], "graph2")
print(list(range(1, 1000000))[0])