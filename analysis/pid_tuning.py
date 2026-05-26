import matplotlib.pyplot as plt
from system_model import ThermalSystem
from controllers.pid import PIDController
from simulator import run_simulation

SETPOINT = 80.0

configs = [
    {"Kp": 0.2, "Ki": 0.0, "Kd": 0.0, "label": "Sadece P (zayif)"},
    {"Kp": 1.0, "Ki": 0.0, "Kd": 0.0, "label": "Sadece P (guclu)"},
    {"Kp": 0.5, "Ki": 0.1, "Kd": 0.0, "label": "PI (kalici hata yok)"},
    {"Kp": 0.5, "Ki": 0.1, "Kd": 0.05, "label": "PID (dengeli)"},
]

plt.figure(figsize=(10, 6))
for cfg in configs:
    system = ThermalSystem(K=100.0, tau=5.0)
    pid = PIDController(
        Kp=cfg["Kp"], Ki=cfg["Ki"], Kd=cfg["Kd"],
        setpoint=SETPOINT
    )
    t, v, _, _ = run_simulation(system, pid, duration=30.0, dt=0.1, is_pid=True)
    plt.plot(t, v, label=cfg["label"])

plt.axhline(SETPOINT, color="black", linestyle="--", label="Setpoint")
plt.xlabel("Zaman (s)")
plt.ylabel("Sicaklik (C)")
plt.title("PID Katsayilarinin Sistem Tepkisine Etkisi")
plt.legend()
plt.grid(True)
plt.savefig("docs/pid_tuning.png", dpi=120)
plt.show()
print("Grafik docs/pid_tuning.png olarak kaydedildi.")