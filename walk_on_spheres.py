import math
import random
import os
import sys
import time
import matplotlib.pyplot as plt


# 두 지점 사이의 거리를 재는 함수
def distance_to(pos_1st, pos_2nd):
    return math.sqrt((pos_1st[0] - pos_2nd[0]) ** 2 + (pos_1st[1] - pos_2nd[1]) ** 2)


# 시뮬레이션 결과를 bar형태로 만드는 함수
def make_plot_file(x_axis_data, y_axis_data, title, x_label, y_label, save_dir):
    plt.clf()
    plt.plot(x_axis_data, y_axis_data)
    plt.title(str(title))
    plt.xlabel(str(x_label))
    plt.ylabel(str(y_label))
    plt.savefig(str(save_dir))


# 실행 command로 받아올 parameter들
radius = float(sys.argv[1])  # big circle의 반지름
step_radius = float(sys.argv[2])  # 각 step마다 만들 sphere의 기본 반지름
epsilon = float(sys.argv[3])  # step의 결과가 big circle에 가까운지 판정할 척도
start_pos_factor = int(sys.argv[4])  # 몇 개의 starting position에 대해서 시뮬레이션 할지
start_pos_theta = float(sys.argv[5]) * math.pi  # starting position을 어느 방향으로 움직일지
monte_time = int(sys.argv[6])  # 한 starting position에 대해서 몇 번의 diffusion process를 할지
# 원점부터 start_pos_theta 방향으로 start_pos_factor 갯수 만큼의 starting position을 실험한다
start_pos_list = [((radius * i / start_pos_factor) * math.cos(start_pos_theta),
                   (radius * i / start_pos_factor) * math.sin(start_pos_theta)) for i in range(start_pos_factor)]
# 시뮬레이션 결과 저장할 디렉터리 생성
now = time.localtime()
current_time = str(now.tm_year) + "-" + str(now.tm_mon) + "-" + str(now.tm_mday) + "_" + str(now.tm_hour) + "-" + str(
    now.tm_min) + "-" + str(now.tm_sec)
os.mkdir(current_time + "_walk_on_spheres")

for idx, start_pos in enumerate(start_pos_list):  # 각 starting position에 대해
    angle_list = [0 for i in range(360)]  # diffusion process의 결과가 어디에 닿았는지 저장하는 리스트
    for simul_time in range(monte_time):  # 각 diffusion process에 대해
        # starting position으로 초기화
        cur_x_pos = start_pos[0]
        cur_y_pos = start_pos[1]
        while True:
            # 매 step마다 생성되는 원에서 어느 방향으로 갈지 random하게 뽑음
            rand_theta = random.uniform(0, 2 * math.pi)
            # 만약 step_radius보다 현재 위치에서 boundary까지 거리가 더 짧으면 그 거리를 sphere의 radius로 하고 아니면 step_radius를 radius로 한다
            if radius - distance_to((0, 0), (cur_x_pos, cur_y_pos)) < step_radius:
                real_radius = radius - distance_to((0, 0), (cur_x_pos, cur_y_pos))
            else:
                real_radius = step_radius
            # step 이후의 position으로 update
            new_x_pos = cur_x_pos + real_radius * math.cos(rand_theta)
            new_y_pos = cur_y_pos + real_radius * math.sin(rand_theta)
            # update한 position이 epsilon보다 boundary에 가까우면 simulation을 종료하고 결과를 정리하고 새 simulation을 시작한다
            if radius - distance_to((0, 0), (new_x_pos, new_y_pos)) <= epsilon:
                final_angle = math.atan2(new_y_pos, new_x_pos)
                if final_angle >= 0:
                    pass
                else:
                    final_angle = 2 * math.pi + final_angle
                sample_idx = int(final_angle // (math.pi / 180))
                print(simul_time, "번째 시도는", sample_idx, "~", (sample_idx + 1), "사이의 각도에 도달했다.")
                angle_list[sample_idx] += 1
                break
            else:
                cur_x_pos = new_x_pos
                cur_y_pos = new_y_pos
    walk_on_spheres_dir = "./" + current_time + "_walk_on_spheres/" + current_time + "_walk_on_spheres_" + str(
        start_pos[0]) + "_" + str(start_pos[1]) + ".png"
    tmp_x_axis_list = [1 * i for i in range(360)]
    for angle_idx in range(len(angle_list)):
        angle_list[angle_idx] = angle_list[angle_idx] / monte_time
    title = "walk on spheres on (" + str(start_pos[0]) + ", " + str(start_pos[1]) + ")"
    make_plot_file(tmp_x_axis_list, angle_list, title, "angle(degree)", "times(percent)", walk_on_spheres_dir)

    # cdf plotting을 하기 위한 list 만들기
    angle_list_cdf = list()
    for angle_idx in range(len(angle_list)):
        if angle_idx > 0:
            angle_list_cdf.append(angle_list_cdf[angle_idx - 1] + angle_list[angle_idx])
        else:
            angle_list_cdf.append(angle_list[angle_idx])
    # cdf plotting
    title = "walk on spheres cdf on (" + str(start_pos[0]) + ", " + str(start_pos[1]) + ")"
    walk_on_spheres_dir = "./" + current_time + "_walk_on_spheres/" + current_time + "_walk_on_spheres_cdf_" + str(
        start_pos[0]) + "_" + str(start_pos[1]) + ".png"
    make_plot_file(tmp_x_axis_list, angle_list_cdf, title, "angle(degree)", "times(percent)", walk_on_spheres_dir)
