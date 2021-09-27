import time
import random
import math
import sys
import os
import matplotlib.pyplot as plt
import buffonTest
import hitOrMiss
import htmForMultiDim
import numpy as np


def make_plot_file(x_axis_data, y_axis_data, title, x_label, y_label, save_dir):
    plt.clf()
    plt.plot(x_axis_data, y_axis_data)
    plt.title(str(title))
    plt.xlabel(str(x_label))
    plt.ylabel(str(y_label))
    plt.text(x_axis_data[-1], y_axis_data[-1], str(y_axis_data[-1]), fontsize=9, color="blue",
             horizontalalignment="center",
             verticalalignment="bottom")
    plt.savefig(str(save_dir))


def make_error_list(resultList):
    errorList = []
    for result in resultList:
        errorList.append(abs(math.pi - result) / math.pi)
    return errorList


def make_multi_plot_file(title, x_label, y_label, save_dir, *x_y_label_args):
    plt.clf()
    for index in range(len(x_y_label_args) // 3):
        plt.plot(x_y_label_args[3 * index], x_y_label_args[3 * index + 1], label = str(x_y_label_args[3 * index + 2]))
    plt.title(str(title))
    plt.xlabel(str(x_label))
    plt.ylabel(str(y_label))
    plt.legend()
    for index in range(len(x_y_label_args) // 3):
        plt.text(x_y_label_args[3 * index][-1], x_y_label_args[3 * index + 1][-1], str(x_y_label_args[3 * index + 1][-1]), fontsize=9, color="blue",
                 horizontalalignment="center",
                 verticalalignment="bottom")
    plt.savefig(str(save_dir))


# 실행 command line에서 parameter을 받아온다
needleLen = float(sys.argv[1])  # 바늘 크기
lineInterval = float(sys.argv[2])  # 선들의 간격
planeWid = float(sys.argv[3])  # 바닥의 너비
angleNum = int(sys.argv[4])
radius = float(sys.argv[5])
dimension = int(sys.argv[6])

now = time.localtime()
currentTime = str(now.tm_year) + "-" + str(now.tm_mon) + "-" + str(now.tm_mday) + "_" + str(now.tm_hour) + "-" + str(
    now.tm_min) + "-" + str(now.tm_sec)

simulTimeList = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 40000,
                 90000, 160000, 250000, 360000, 490000, 640000, 810000, 1000000]  # BuffonTest에 simulTimes에 들어갈 것들의 list

buffonTimeList, buffonResultList = buffonTest.BuffonTest(needleLen, lineInterval, planeWid, simulTimeList)
homTimeList, homResultList = hitOrMiss.HitOrMissSampling(angleNum, radius, simulTimeList)
homNDimTimeList, homNDimResultList = htmForMultiDim.htm_for_multi_dim_sampling(dimension, radius, simulTimeList)

buffonErrorList = make_error_list(buffonResultList)
homErrorList = make_error_list(homResultList)
homNDimErrorList = make_error_list(homNDimResultList)

os.mkdir(currentTime)

buffon_result_dir = "./" + currentTime + "/" + currentTime + "_buffon_result.png"
buffon_result_log_dir = "./" + currentTime + "/" + currentTime + "_buffon_result_log.png"
buffon_error_dir = "./" + currentTime + "/" + currentTime + "_buffon_error.png"
buffon_error_manuf_dir = "./" + currentTime + "/" + currentTime + "_buffon_error_manuf.png"

make_plot_file(buffonTimeList, buffonResultList, "pi cal result", "n(times)", "pi", buffon_result_dir)
buffonTimeLogList = []
for entry in buffonTimeList:
    buffonTimeLogList.append(math.log2(entry))
make_plot_file(buffonTimeLogList, buffonResultList, "pi cal result", "log(n)(times)", "pi", buffon_result_log_dir)
make_plot_file(buffonTimeList, buffonErrorList, "pi cal error result", "n(times)", "error", buffon_error_dir)
buffonErrorManufList = []
for error in buffonErrorList:
    buffonErrorManufList.append(math.log2(1 / (error ** 2)))
make_plot_file(buffonTimeLogList, buffonErrorManufList, "pi cal error result", "log(n)(times)", "log(1/error^2)", buffon_error_manuf_dir)


hom_result_dir = "./" + currentTime + "/" + currentTime + "_hom_result.png"
hom_result_log_dir = "./" + currentTime + "/" + currentTime + "_hom_result_log.png"
hom_error_dir = "./" + currentTime + "/" + currentTime + "_hom_error.png"
hom_error_manuf_dir = "./" + currentTime + "/" + currentTime + "_hom_error_manuf.png"

make_plot_file(homTimeList, homResultList, "pi cal with " + str(angleNum) + "-regular polygon result", "n(times)", "pi", hom_result_dir)
homTimeLogList = []
for entry in homTimeList:
    homTimeLogList.append(math.log2(entry))
make_plot_file(homTimeLogList, homResultList, "pi cal with " + str(angleNum) + "-regular polygon result", "log(n)(times)", "pi", hom_result_log_dir)
make_plot_file(homTimeList, homErrorList, "pi cal error with " + str(angleNum) + "-regular polygon result", "n(times)", "error", hom_error_dir)
homErrorManufList = []
for error in homErrorList:
    homErrorManufList.append(math.log2(1 / (error ** 2)))
make_plot_file(homTimeLogList, homErrorManufList, "pi cal error with " + str(angleNum) + "-regular polygon result", "log(n)(times)", "log(1/error^2)", hom_error_manuf_dir)


homNDim_result_dir = "./" + currentTime + "/" + currentTime + "_homNDim_result.png"
homNDim_result_log_dir = "./" + currentTime + "/" + currentTime + "_homNDim_result_log.png"
homNDim_error_dir = "./" + currentTime + "/" + currentTime + "_homNDim_error.png"
homNDim_error_manuf_dir = "./" + currentTime + "/" + currentTime + "_homNDim_error_manuf.png"

make_plot_file(homNDimTimeList, homNDimResultList, "pi cal with " + str(dimension) + "-dim result", "n(times)", "pi", homNDim_result_dir)
homNDimTimeLogList = []
for entry in homNDimTimeList:
    homNDimTimeLogList.append(math.log2(entry))
make_plot_file(homNDimTimeLogList, homNDimResultList, "pi cal with " + str(dimension) + "-dim result", "log(n)(times)", "pi", homNDim_result_log_dir)
make_plot_file(homNDimTimeList, homNDimErrorList, "pi cal error with " + str(dimension) + "-dim result", "n(times)", "error", homNDim_error_dir)
homNDimErrorManufList = []
for error in homNDimErrorList:
    homNDimErrorManufList.append(math.log2(1 / (error ** 2)))
make_plot_file(homNDimTimeLogList, homNDimErrorManufList, "pi cal error with " + str(dimension) + "-dim result", "log(n)(times)", "log(1/error^2)", homNDim_error_manuf_dir)


cmp_result_dir = "./" + currentTime + "/" + currentTime + "_cmp_result.png"
cmp_result_log_dir = "./" + currentTime + "/" + currentTime + "_cmp_result_log.png"
cmp_error_dir = "./" + currentTime + "/" + currentTime + "_cmp_error.png"
cmp_error_manuf_dir = "./" + currentTime + "/" + currentTime + "_cmp_error_manuf.png"

cmp_hom_label = str(angleNum) + "-regular polygon hom"
cmp_homNDim_label = str(dimension) + "-dim hom"

make_multi_plot_file("pi cal result", "n(times)", "pi", cmp_result_dir, buffonTimeList, buffonResultList, "buffonNeedle", homTimeList, homResultList, cmp_hom_label, homNDimTimeList, homNDimResultList, cmp_homNDim_label)
make_multi_plot_file("pi cal result", "log(n)(times)", "pi", cmp_result_log_dir, buffonTimeLogList, buffonResultList, "buffonNeedle", homTimeLogList, homResultList, cmp_hom_label, homNDimTimeLogList, homNDimResultList, cmp_homNDim_label)
make_multi_plot_file("pi cal error result", "n(times)", "error", cmp_error_dir, buffonTimeList, buffonErrorList, "buffonNeedle", homTimeList, homErrorList, cmp_hom_label, homNDimTimeList, homNDimErrorList, cmp_homNDim_label)
make_multi_plot_file("pi cal error result", "log(n)(times)", "log(1/error^2)", cmp_error_manuf_dir, buffonTimeLogList, buffonErrorManufList, "buffonNeedle", homTimeLogList, homErrorManufList, cmp_hom_label, homNDimTimeLogList, homNDimErrorManufList, cmp_homNDim_label)
