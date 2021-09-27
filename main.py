import time
import math
import sys
import os
import matplotlib.pyplot as plt
import buffonTest
import hitOrMiss
import htmForMultiDim


# 한 테스트에 대한 plot을 저장하는 함수
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


# 한 테스트 결과에 대한 에러율 리스트를 만드는 함수
def make_error_list(resultList):
    errorList = []
    for result in resultList:
        errorList.append(abs(math.pi - result) / math.pi)
    return errorList


# 여러 테스트들의 결과를 비교한 plot 파일을 저장하는 함수
def make_multi_plot_file(title, x_label, y_label, save_dir, *x_y_label_args):
    plt.clf()
    for index in range(len(x_y_label_args) // 3):
        plt.plot(x_y_label_args[3 * index], x_y_label_args[3 * index + 1], label=str(x_y_label_args[3 * index + 2]))
    plt.title(str(title))
    plt.xlabel(str(x_label))
    plt.ylabel(str(y_label))
    plt.legend()
    for index in range(len(x_y_label_args) // 3):
        plt.text(x_y_label_args[3 * index][-1], x_y_label_args[3 * index + 1][-1],
                 str(x_y_label_args[3 * index + 1][-1]), fontsize=9, color="blue",
                 horizontalalignment="center",
                 verticalalignment="bottom")
    plt.savefig(str(save_dir))


# 실행 command line에서 parameter을 받아온다
needleLen = float(sys.argv[1])  # 바늘 크기
lineInterval = float(sys.argv[2])  # 선들의 간격
planeWid = float(sys.argv[3])  # 바닥의 너비
angleNum = int(sys.argv[4])  # 정n각형의 꼭짓점 개수
radius = float(sys.argv[5])  # 정n각형에 내접하는 원의 반지름
dimension = int(sys.argv[6])  # n차원의 초구와 초입방체에 대해 하는 테스트의 차원

# 테스트 결과를 저장한 plot 파일들을 저장할 dir
now = time.localtime()
currentTime = str(now.tm_year) + "-" + str(now.tm_mon) + "-" + str(now.tm_mday) + "_" + str(now.tm_hour) + "-" + str(
    now.tm_min) + "-" + str(now.tm_sec)

simulTimeList = [100, 400, 900, 1600, 2500, 3600, 4900, 6400, 8100, 10000, 40000,
                 90000, 160000, 250000, 360000, 490000, 640000, 810000, 1000000]  # 시뮬레이션을 하면서 언제 중간 결과를 기록할지의 리스트

# 순서대로 buffon-needle 테스트, 정n각형에 대한 hit-or-miss 테스트, n차원 속 초구와 초 입방체에 대한 hit-or-miss 테스트 및 리스트에 저장
buffonTimeList, buffonResultList = buffonTest.BuffonTest(needleLen, lineInterval, planeWid, simulTimeList)
homTimeList, homResultList = hitOrMiss.HitOrMissSampling(angleNum, radius, simulTimeList)
homNDimTimeList, homNDimResultList = htmForMultiDim.htm_for_multi_dim_sampling(dimension, radius, simulTimeList)

# 위의 테스트들 결과의 에러율을 리스트로 만들어 저장
buffonErrorList = make_error_list(buffonResultList)
homErrorList = make_error_list(homResultList)
homNDimErrorList = make_error_list(homNDimResultList)

os.mkdir(currentTime)  # plot 파일들을 저장할 디렉터리 생성

# buffon 테스트의 다양한 결과들을 저장할 디렉터리
buffon_result_dir = "./" + currentTime + "/" + currentTime + "_buffon_result.png"
buffon_result_log_dir = "./" + currentTime + "/" + currentTime + "_buffon_result_log.png"
buffon_error_dir = "./" + currentTime + "/" + currentTime + "_buffon_error.png"
buffon_error_manuf_dir = "./" + currentTime + "/" + currentTime + "_buffon_error_manuf.png"

# buffon 테스트의 결과들을 plot으로 만들어서 저장
make_plot_file(buffonTimeList, buffonResultList, "pi cal result", "n(times)", "pi", buffon_result_dir)
buffonTimeLogList = []
for entry in buffonTimeList:
    buffonTimeLogList.append(math.log2(entry))
make_plot_file(buffonTimeLogList, buffonResultList, "pi cal result", "log(n)(times)", "pi", buffon_result_log_dir)
make_plot_file(buffonTimeList, buffonErrorList, "pi cal error result", "n(times)", "error", buffon_error_dir)
buffonErrorManufList = []
for error in buffonErrorList:
    buffonErrorManufList.append(math.log2(1 / (error ** 2)))
make_plot_file(buffonTimeLogList, buffonErrorManufList, "pi cal error result", "log(n)(times)", "log(1/error^2)",
               buffon_error_manuf_dir)

# 정n각형에 대한 hit-or-miss 테스트의 다양한 결과들을 저장할 디렉터리
hom_result_dir = "./" + currentTime + "/" + currentTime + "_hom_result.png"
hom_result_log_dir = "./" + currentTime + "/" + currentTime + "_hom_result_log.png"
hom_error_dir = "./" + currentTime + "/" + currentTime + "_hom_error.png"
hom_error_manuf_dir = "./" + currentTime + "/" + currentTime + "_hom_error_manuf.png"

# 정n각형에 대한 hit-or-miss 테스트의 결과들을 plot으로 만들어서 저장
make_plot_file(homTimeList, homResultList, "pi cal with " + str(angleNum) + "-regular polygon result", "n(times)", "pi",
               hom_result_dir)
homTimeLogList = []
for entry in homTimeList:
    homTimeLogList.append(math.log2(entry))
make_plot_file(homTimeLogList, homResultList, "pi cal with " + str(angleNum) + "-regular polygon result",
               "log(n)(times)", "pi", hom_result_log_dir)
make_plot_file(homTimeList, homErrorList, "pi cal error with " + str(angleNum) + "-regular polygon result", "n(times)",
               "error", hom_error_dir)
homErrorManufList = []
for error in homErrorList:
    homErrorManufList.append(math.log2(1 / (error ** 2)))
make_plot_file(homTimeLogList, homErrorManufList, "pi cal error with " + str(angleNum) + "-regular polygon result",
               "log(n)(times)", "log(1/error^2)", hom_error_manuf_dir)

# n차원에서의 hit-or-miss 테스트의 다양한 결과들을 저장할 디렉터리
homNDim_result_dir = "./" + currentTime + "/" + currentTime + "_homNDim_result.png"
homNDim_result_log_dir = "./" + currentTime + "/" + currentTime + "_homNDim_result_log.png"
homNDim_error_dir = "./" + currentTime + "/" + currentTime + "_homNDim_error.png"
homNDim_error_manuf_dir = "./" + currentTime + "/" + currentTime + "_homNDim_error_manuf.png"

# n차원에서의 hit-or-miss 테스트 결과들을 plot으로 만들어서 저장
make_plot_file(homNDimTimeList, homNDimResultList, "pi cal with " + str(dimension) + "-dim result", "n(times)", "pi",
               homNDim_result_dir)
homNDimTimeLogList = []
for entry in homNDimTimeList:
    homNDimTimeLogList.append(math.log2(entry))
make_plot_file(homNDimTimeLogList, homNDimResultList, "pi cal with " + str(dimension) + "-dim result", "log(n)(times)",
               "pi", homNDim_result_log_dir)
make_plot_file(homNDimTimeList, homNDimErrorList, "pi cal error with " + str(dimension) + "-dim result", "n(times)",
               "error", homNDim_error_dir)
homNDimErrorManufList = []
for error in homNDimErrorList:
    homNDimErrorManufList.append(math.log2(1 / (error ** 2)))
make_plot_file(homNDimTimeLogList, homNDimErrorManufList, "pi cal error with " + str(dimension) + "-dim result",
               "log(n)(times)", "log(1/error^2)", homNDim_error_manuf_dir)


# 다양한 테스트들의 결과들을 비교하는 plot 파일들을 저장하는 디렉터리
cmp_result_dir = "./" + currentTime + "/" + currentTime + "_cmp_result.png"
cmp_result_log_dir = "./" + currentTime + "/" + currentTime + "_cmp_result_log.png"
cmp_error_dir = "./" + currentTime + "/" + currentTime + "_cmp_error.png"
cmp_error_manuf_dir = "./" + currentTime + "/" + currentTime + "_cmp_error_manuf.png"

# 정n각형, n차원에 대한 라벨 생성
cmp_hom_label = str(angleNum) + "-regular polygon hom"
cmp_homNDim_label = str(dimension) + "-dim hom"

# 다양한 테스트들의 결과들을 비교하는 plot 파일들을 만들어서 저장
make_multi_plot_file("pi cal result", "n(times)", "pi", cmp_result_dir, buffonTimeList, buffonResultList,
                     "buffonNeedle", homTimeList, homResultList, cmp_hom_label, homNDimTimeList, homNDimResultList,
                     cmp_homNDim_label)
make_multi_plot_file("pi cal result", "log(n)(times)", "pi", cmp_result_log_dir, buffonTimeLogList, buffonResultList,
                     "buffonNeedle", homTimeLogList, homResultList, cmp_hom_label, homNDimTimeLogList,
                     homNDimResultList, cmp_homNDim_label)
make_multi_plot_file("pi cal error result", "n(times)", "error", cmp_error_dir, buffonTimeList, buffonErrorList,
                     "buffonNeedle", homTimeList, homErrorList, cmp_hom_label, homNDimTimeList, homNDimErrorList,
                     cmp_homNDim_label)
make_multi_plot_file("pi cal error result", "log(n)(times)", "log(1/error^2)", cmp_error_manuf_dir, buffonTimeLogList,
                     buffonErrorManufList, "buffonNeedle", homTimeLogList, homErrorManufList, cmp_hom_label,
                     homNDimTimeLogList, homNDimErrorManufList, cmp_homNDim_label)
