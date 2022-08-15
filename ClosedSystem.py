from ClosedSystemElement import ClosedSystemElement
import random


def _make_system_element_list(system_size, system_type):
    tmp_list = list()
    for y_idx in range(system_size):
        tmp_row_list = list()
        for x_idx in range(system_size):
            random_state=random.choice([-1, 1])
            tmp_row_list.append(ClosedSystemElement(x_idx, y_idx, random_state, system_size, system_type))
        tmp_list.append(tmp_row_list)

    return tmp_list


class ClosedSystem:

    def __init__(self, coup_const, temperature, external_mag, system_size, system_type):
        self.coup_const = coup_const
        self.temperature = temperature
        self.external_mag = external_mag  # 아직 안쓰지만 혹시나 해서 넣어두는 변수
        self.system_size = system_size
        self.system_type = system_type
        self.system_element_list = _make_system_element_list(self.system_size, self.system_type)

    def change_element_state(self, x_idx, y_idx):
        if self.system_element_list[y_idx][x_idx].current_state == 1:
            self.system_element_list[y_idx][x_idx].current_state = -1
        else:
            self.system_element_list[y_idx][x_idx].current_state = 1

    def calculate_magnetization(self):
        magnetization_sum = 0
        for element_list in self.system_element_list:
            for element in element_list:
                magnetization_sum += element.current_state

        return magnetization_sum

    def calculate_energy(self):
        energy_sum = 0
        for element_list in self.system_element_list:
            for element in element_list:
                for adjacent_idx in element.adjacency_list:
                    adjacent_element = self.system_element_list[adjacent_idx[1]][adjacent_idx[0]]
                    energy_sum += element.current_state * adjacent_element.current_state

        return energy_sum
