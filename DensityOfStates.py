import math


def _make_density_array(max_M, max_E):
    tmp_list = list()
    for y_idx in range(-max_E, max_E + 1, 1):
        tmp_row_list = list()
        for x_idx in range(-max_M, max_M + 1, 1):
            tmp_row_list.append(1)
        tmp_list.append(tmp_row_list)

    return tmp_list


def _calculate_max_E(system_size, system_type):
    if system_type == "SL":
        return 4 * system_size ** 2
    else:
        pass


class DensityOfStates:
    def __init__(self, system_size, system_type, power_factor):
        self.system_size = system_size
        self.system_type = system_type
        self.max_M = system_size ** 2
        self.min_M = -system_size ** 2
        self.max_E = _calculate_max_E(self.system_size, self.system_type)
        self.min_E = -self.max_E
        self.density_array = _make_density_array(self.max_M, self.max_E)
        self.power_factor = power_factor
        self.multiply_factor = math.exp(self.power_factor)

    def set_density(self, M_idx, E_idx):
        self.density_array[E_idx + self.max_E][M_idx + self.max_M] *= self.multiply_factor

    def get_density(self, M_idx, E_idx):
        return self.density_array[E_idx + self.max_E][M_idx + self.max_M]

    def update_multiply_factor(self, current_times, update_factor):
        self.multiply_factor = math.exp(self.power_factor / (current_times//update_factor + 1))
