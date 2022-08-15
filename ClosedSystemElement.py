class ClosedSystemElement:
    def __init__(self, x_idx, y_idx, initial_state, system_size, system_type):
        self.x_idx = x_idx
        self.y_idx = y_idx
        self.current_state = initial_state
        self.system_size = system_size
        self.system_type = system_type
        self.adjacency_list = self._make_adjacency_list(self.system_type)

    def _make_adjacency_list(self, system_type):
        tmp_list = list()
        if system_type == "SL":
            if self.x_idx == 0:
                tmp_list.append((self.system_size - 1, self.y_idx))
            else:
                tmp_list.append((self.x_idx - 1, self.y_idx))
            if self.y_idx == 0:
                tmp_list.append((self.x_idx, self.system_size - 1))
            else:
                tmp_list.append((self.x_idx, self.y_idx - 1))
            if self.x_idx == self.system_size - 1:
                tmp_list.append((0, self.y_idx))
            else:
                tmp_list.append((self.x_idx + 1, self.y_idx))
            if self.y_idx == self.system_size - 1:
                tmp_list.append((self.x_idx, 0))
            else:
                tmp_list.append((self.x_idx, self.y_idx + 1))
        elif system_type == "TL":
            pass

        return tmp_list
