from ClosedSystemElement import ClosedSystemElement
from ClosedSystem import ClosedSystem
import math
import sys
import os
import random
import time
import matplotlib.pyplot as plt
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


def print_current_system(system, current_energy, current_mag, current_total_energy_para):
    system_size_func = system.system_size
    state_one_num = 0
    state_minus_one_num = 0
    for y_idx in range(system_size_func):
        for x_idx in range(system_size_func):
            print(system.system_element_list[y_idx][x_idx].current_state, end=" ")
            if system.system_element_list[y_idx][x_idx].current_state == 1:
                state_one_num += 1
            else:
                state_minus_one_num += 1
        print(end='\n')
    print("current energy: ", current_energy)
    print("current mag: ", current_mag)
    print("current total energy: ", current_total_energy_para)
    print("1's percentage: ", state_one_num / (system_size_func ** 2))
    print("-1's percentage: ", state_minus_one_num / (system_size_func ** 2))


def thermodynamic_func(factor_list, factor_range_list, factor_name):
    var_list = list()
    for idx, factor in enumerate(factor_list):
        tmp_var_list = list()
        small_h=0
        if factor_name == "temperature":
            closed_system = ClosedSystem(coup_const, factor, external_mag, system_size, system_type)
            small_h = external_mag / (-coup_const)
        elif factor_name == "external_mag":
            closed_system = ClosedSystem(coup_const, temperature, factor, system_size, system_type)
            small_h = factor / (-coup_const)

        monte_energy_list = list()
        monte_mag_list = list()
        monte_total_energy_list = list()

        monte_energy_list.append(closed_system.calculate_energy())
        monte_mag_list.append(closed_system.calculate_magnetization())
        monte_total_energy_list.append(-coup_const * monte_energy_list[-1] - small_h * monte_mag_list[-1])
        print_current_system(closed_system, monte_energy_list[-1], monte_mag_list[-1], monte_total_energy_list[-1])

        for i in range(monte_time):
            rand_x_idx = random.randint(0, system_size - 1)
            rand_y_idx = random.randint(0, system_size - 1)

            current_total_energy = monte_total_energy_list[-1]
            closed_system.change_element_state(rand_x_idx, rand_y_idx)
            new_energy = closed_system.calculate_energy()
            new_mag = closed_system.calculate_magnetization()
            new_total_energy = -coup_const * new_energy - small_h * new_mag

            if new_total_energy - current_total_energy < 0:
                monte_total_energy_list.append(new_total_energy)
                monte_energy_list.append(new_energy)
                monte_mag_list.append(new_mag)
                if i + 1 >= factor_range_list[idx]:
                    if factor_name == "temperature":
                        tmp_var_list.append(monte_energy_list[-1])
                    elif factor_name == "external_mag":
                        tmp_var_list.append(monte_mag_list[-1])
                print(i + 1, "번째에는 상태가 바뀌었습니다.")
                print_current_system(closed_system, monte_energy_list[-1], monte_mag_list[-1],
                                     monte_total_energy_list[-1])
            else:
                rand_prob = random.uniform(0, 1)
                transition_bound = math.exp(-(new_total_energy - current_total_energy) / temperature)
                if rand_prob > transition_bound:
                    closed_system.change_element_state(rand_x_idx, rand_y_idx)
                    print(i + 1, "번째에는 상태가 바뀌지 않았습니다.")
                else:
                    monte_total_energy_list.append(new_total_energy)
                    monte_energy_list.append(new_energy)
                    monte_mag_list.append(new_mag)
                    if i + 1 >= factor_range_list[idx]:
                        if factor_name == "temperature":
                            tmp_var_list.append(monte_energy_list[-1])
                        elif factor_name == "external_mag":
                            tmp_var_list.append(monte_mag_list[-1])
                    print(i + 1, "번째에는 상태가 바뀌었습니다.")
                    print_current_system(closed_system, monte_energy_list[-1], monte_mag_list[-1],
                                         monte_total_energy_list[-1])
        var_list.append(np.var(tmp_var_list))

    return var_list


coup_const = float(sys.argv[1])
temperature = float(sys.argv[2])
external_mag = float(sys.argv[3])
system_size = int(sys.argv[4])
system_type = sys.argv[5]
monte_time = int(sys.argv[6])

temperature_list = [i for i in range(2, 100)]
ext_mag_list = [i for i in range(0, 25)]
temperature_range_list = [2000 for i in range(len(temperature_list))]
ext_mag_range_list = [2000 for i in range(len(ext_mag_list))]

var_temperature_list = thermodynamic_func(temperature_list, temperature_range_list, "temperature")
var_ext_mag_list = thermodynamic_func(ext_mag_list, ext_mag_range_list, "external_mag")

now = time.localtime()
current_time = str(now.tm_year) + "-" + str(now.tm_mon) + "-" + str(now.tm_mday) + "_" + str(now.tm_hour) + "-" + str(
    now.tm_min) + "-" + str(now.tm_sec)
os.mkdir(current_time + "_thermodynamic_func")
specific_heat_dir = "./" + current_time + "_thermodynamic_func/" + current_time + "_thermodynamic_func_specific_heat.png"
susceptibility_dir = "./" + current_time + "_thermodynamic_func/" + current_time + "_thermodynamic_func_susceptibility.png"
make_plot_file(temperature_list, var_temperature_list, "specific_heat result", "temperature", "specific_heat", specific_heat_dir)
make_plot_file(ext_mag_list, var_ext_mag_list, "susceptibility result", "external_mag", "susceptibility", susceptibility_dir)
