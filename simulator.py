"""
Simulasyon motoru.
Kontrolcu ile sistemi belirli sure boyunca calistirir,
zaman / sicaklik / kontrol sinyali / hata verilerini toplar.
"""

import numpy as np


def run_simulation(system, controller, duration=30.0, dt=0.1, is_pid=False):
    steps = int(duration / dt)
    time_data = np.zeros(steps)
    value_data = np.zeros(steps)
    control_data = np.zeros(steps)
    error_data = np.zeros(steps)

    for i in range(steps):
        t = i * dt
        current = system.T

        # Kontrolcu turune gore cagri
        if is_pid:
            u = controller.compute(current, dt)
        else:
            u = controller.compute(current)

        # Sistemi guncelle
        system.update(u, dt)

        # Verileri kaydet
        time_data[i] = t
        value_data[i] = current
        control_data[i] = u
        error_data[i] = controller.setpoint - current

    return time_data, value_data, control_data, error_data