"""
Ana calistirma dosyasi.
Bang-Bang ve PID kontrolcuyu ayni sistem uzerinde kosturup karsilastirir.
"""

import matplotlib.pyplot as plt
from system_model import ThermalSystem
from controllers.bang_bang import BangBangController
from controllers.pid import PIDController
from simulator import run_simulation

SETPOINT = 80.0
DURATION = 30.0
DT = 0.1

# --- Bang-Bang simulasyonu ---
system_bb = ThermalSystem(K=100.0, tau=5.0, initial_temp=20.0)
bb_controller = BangBangController(setpoint=SETPOINT)
t_bb, v_bb, u_bb, e_bb = run_simulation(
    system_bb, bb_controller, DURATION, DT, is_pid=False
)

# --- PID simulasyonu ---
system_pid = ThermalSystem(K=100.0, tau=5.0, initial_temp=20.0)
pid_controller = PIDController(
    Kp=0.5, Ki=0.1, Kd=0.05, setpoint=SETPOINT
)
t_pid, v_pid, u_pid, e_pid = run_simulation(
    system_pid, pid_controller, DURATION, DT, is_pid=True
)

# --- Gorsellistirme ---
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Ust grafik: Sistem tepkisi
axes[0].plot(t_bb, v_bb, label="Bang-Bang", color="red")
axes[0].plot(t_pid, v_pid, label="PID", color="blue")
axes[0].axhline(SETPOINT, color="green", linestyle="--", label="Setpoint")
axes[0].set_xlabel("Zaman (s)")
axes[0].set_ylabel("Sicaklik (C)")
axes[0].set_title("Sistem Tepkisi Karsilastirmasi")
axes[0].legend()
axes[0].grid(True)

# Alt grafik: Kontrol sinyali
axes[1].plot(t_bb, u_bb, label="Bang-Bang u(t)", color="red")
axes[1].plot(t_pid, u_pid, label="PID u(t)", color="blue")
axes[1].set_xlabel("Zaman (s)")
axes[1].set_ylabel("Kontrol Sinyali")
axes[1].set_title("Kontrol Sinyali Karsilastirmasi")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig("docs/comparison.png", dpi=120)
plt.show()

print("Grafik docs/comparison.png olarak kaydedildi.")