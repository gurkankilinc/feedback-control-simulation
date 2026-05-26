"""
PID Kontrolcu.
u(t) = Kp * e(t) + Ki * integral(e) + Kd * de/dt

Kp (Oransal) : Hata buyukse cikis buyuk. Tek basina kalici hata birakir.
Ki (Integral) : Gecmisteki hatalari toplar, kalici hatayi sifirlar.
Kd (Turevsel) : Hatanin degisim hizina bakar, asimi (overshoot) azaltir.
"""


class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint, u_max=1.0, u_min=0.0):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.u_max = u_max
        self.u_min = u_min

        self._integral = 0.0
        self._prev_error = 0.0

    def compute(self, current_value, dt):
        error = self.setpoint - current_value

        # Oransal terim
        P = self.Kp * error

        # Integral terim (birikmis hata)
        self._integral += error * dt
        I = self.Ki * self._integral

        # Turevsel terim (hatanin degisim hizi)
        derivative = (error - self._prev_error) / dt if dt > 0 else 0.0
        D = self.Kd * derivative

        # Toplam cikis
        u = P + I + D

        # Doyma - cikisi sinirla
        u = max(self.u_min, min(self.u_max, u))

        self._prev_error = error
        return u