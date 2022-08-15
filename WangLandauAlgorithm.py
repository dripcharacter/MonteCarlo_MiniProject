from ClosedSystemElement import ClosedSystemElement
from ClosedSystem import ClosedSystem
from DensityOfStates import DensityOfStates
import sys
import math
import random
import matplotlib.pyplot as plt
import numpy as np

# parameter로 받아오는 coupling constant, system의 size와 종류, 시뮬레이션 횟수, wang_landau update에 쓰이는 factor 2개
coup_const = float(sys.argv[1])
system_size = int(sys.argv[2])
system_type = sys.argv[3]
monte_time = int(sys.argv[4])
power_factor = float(sys.argv[5])
update_factor = int(sys.argv[6])
# 닫힌계와 microstate에 대한 degeneracy에 대한 object생성
closed_system = ClosedSystem(coup_const, math.inf, 0, system_size, system_type)
state_density = DensityOfStates(system_size, system_type, power_factor)

# simulation에서 현재 microstate에서 가지고 있는 energy, magnetization, degeneracy를 저장하는 변수
current_energy = closed_system.calculate_energy()
current_mag = closed_system.calculate_magnetization()
current_density = state_density.get_density(current_mag, current_energy)

for i in range(monte_time):
    # 매스탭 flip할 site를 정하고 저장하는 랜덤 변수
    x_idx = random.randint(0, system_size - 1)
    y_idx = random.randint(0, system_size - 1)
    # 바뀐 microstate에 대한 energy, magnetization, degeneracy를 저장하고 multiply_factor을 업데이트 한다
    closed_system.change_element_state(x_idx, y_idx)
    new_energy = closed_system.calculate_energy()
    new_mag = closed_system.calculate_magnetization()
    new_density = state_density.get_density(new_mag, new_energy)
    state_density.update_multiply_factor(monte_time + 1, monte_time // update_factor)
    # 새 microstate가 현재 microstate보다 degeneracy가 낮을때(무조건 상태 전이)
    if new_density - current_density <= 0:
        # 상태 전이를 반영하는 과정
        current_energy = new_energy
        current_mag = new_mag
        # 바뀐 상태의 degeneracy를 업데이트하고 업데이트한 degeneracy를 변수에 저장하는 과정
        state_density.set_density(current_mag, current_energy)
        current_density = state_density.get_density(current_mag, current_energy)
        print(i, "번쨰에는 바뀌었습니다.")
    else:
        rand_prob = random.uniform(0, 1)  # 상태전이를 할 확률 변수
        if rand_prob < current_density / new_density:  # 상태전이가 성공한 경우
            # 상태 전이를 반영
            current_energy = new_energy
            current_mag = new_mag
            # degeneracy를 업데이트하고 반영하는 과정
            state_density.set_density(current_mag, current_energy)
            current_density = state_density.get_density(current_mag, current_energy)
            print(i, "번쨰에는 바뀌었습니다.")
        else:
            # 닫힌계 object의 spin flip을 되돌리고 바뀌지 않은 상태의 degeneracy를 업데이트 및 반영
            closed_system.change_element_state(x_idx, y_idx)
            state_density.set_density(current_mag, current_energy)
            current_density = state_density.get_density(current_mag, current_energy)
            print(i, "번쨰에는 바뀌지 않았습니다.")

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
# degeneracy에 log를 씌워 entropy로 해석되게 만든다
state_density.density_array = list(map(lambda x: list(map(math.log, x)), state_density.density_array))
# plotting할 점들을 뽑아내 저장할 list
energy_list = list()
mag_list = list()
density_list = list()
# plotting할 점들의 좌표만 뽑아내는 과정(simulation과정동안 한 번도 방문하지 않은(M, E)는 나올 수 없는 microstate로 인식하고 plotting에서 제외한다)
# 제외 기준(ln(degeneracy)==0인 (M, E))
E_idx = state_density.min_E
for same_energy in state_density.density_array:
    M_idx = state_density.min_M
    for degeneracy in same_energy:
        if degeneracy != 0:
            energy_list.append(E_idx)
            mag_list.append(M_idx)
            if degeneracy == math.inf:
                density_list.append(-1)
            else:
                density_list.append(degeneracy)
        M_idx += 1
    E_idx += 1
# Wang_Landau과정동안 이상하게 refine된 값들 정리하는 과정
tmp_max = max(density_list)
tmp_idx = 0
for entry in density_list:
    if entry < 0:
        density_list[tmp_idx] = tmp_max
    tmp_idx += 1
# 뽑아낸 점들을 plotting한다
min_degeneracy = min(density_list)
max_degeneracy = max(density_list)
color_list = np.array([density_list[i] / (max_degeneracy - min_degeneracy) + 1 for i in range(len(density_list))])
ax1.scatter(mag_list, energy_list, density_list, c=color_list, marker='3', s=1, cmap="cool")
ax1.set_xlabel("magnetization")
ax1.set_ylabel("energy")
ax1.set_zlabel("ln[g(M,E)]")
ax1.set_title("degeneracy")
plt.show()
