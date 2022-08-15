from scipy import integrate
import math
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import random
import time

simul_time = int(sys.argv[1])   # 몇 번 (X, Y)를 샘플링할지
sample_range = int(sys.argv[2]) # sample domain

x_coord = 0
y_coord = 0
# 현재 시각을 기반으로 저장하기 위해 미리 만드는 과정
now = time.localtime()
currentTime = str(now.tm_year) + "-" + str(now.tm_mon) + "-" + str(now.tm_mday) + "_" + str(now.tm_hour) + "-" + str(
    now.tm_min) + "-" + str(now.tm_sec)

# 알아보고 싶은 함수 정의
def f(rad, the):
    return 1 / (1 + ((x_coord - rad * math.cos(the)) ** 2 + (y_coord - rad * math.sin(the)) ** 2) / (1 - rad ** 2)) ** (1 / 2)

# 결과 plot할 객체
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
# plot할때 각각 x, y, z 좌표로 쓸 list
x_coord_list = list()
y_coord_list = list()
result_list = list()

for i in range(simul_time):
    # x, y좌표를 샘플링
    rand_rad = random.uniform(0, int(sample_range))
    rand_the = random.uniform(0, 2 * math.pi)

    x_coord_list.append(rand_rad * math.cos(rand_the))
    y_coord_list.append(rand_rad * math.sin(rand_the))

    x_coord = x_coord_list[i]
    y_coord = y_coord_list[i]

    # 이중 적분으로 f(X, Y)값을 구함
    result_list.append(integrate.dblquad(f, 0, 2 * math.pi, lambda the: 0, lambda the: 1)[0])
    print(i + 1, "번째 샘플링: (x_coord:", x_coord_list[i], ", y_coord:", y_coord_list[i], ", result:", result_list[i], ")")

os.mkdir(currentTime+"_integrating")  # plot 파일들을 저장할 디렉터리 생성

min_result = min(result_list)
max_result = max(result_list)
color_list = np.array([result_list[i]/(max_result-min_result) + 10 for i in range(simul_time)]) # 결과의 가시성을 위하여 만드는 color list
ax1.scatter(x_coord_list, y_coord_list, result_list, c=color_list, s=1, cmap="cool")
ax1.set_xlabel("x_coord")
ax1.set_ylabel("y_coord")
ax1.set_zlabel("result")
ax1.set_title("integration")

# standard normal distribution과 비교하기 위해 snd를 plot하는 과정
# mu = [0, 0]
# cov = [[1, 0], [0, 1]]
# rv = stats.multivariate_normal(mu, cov)
# xx = np.linspace(-int(sample_range), int(sample_range), 150)
# yy = np.linspace(-int(sample_range), int(sample_range), 150)
# XX, YY = np.meshgrid(xx, yy)
# ax1.plot_surface(XX, YY, 30 * rv.pdf(np.dstack((XX, YY))))

# 다양한 각도로 결과값을 저장하기 위한 부분
xy_plane_angle_list = range(0, 181, 30)
z_axis_angle_list = range(0, 181, 30)
for xy_entry in xy_plane_angle_list:
    for z_entry in z_axis_angle_list:
        ax1.view_init(z_entry, xy_entry)
        plt.savefig(str("./" + currentTime + "_integrating/" + currentTime + "_integrating_" + str(z_entry) + "_" + str(xy_entry)))

plt.show()
