class BangBangController:
    def __init__(self, setpoint, u_max=1.0, u_min=0.0):
        self.setpoint = setpoint
        self.u_max = u_max
        self.u_min = u_min

    def compute(self, current_value):
        error = self.setpoint - current_value
        if error > 0:
            return self.u_max
        else:
            return self.u_min