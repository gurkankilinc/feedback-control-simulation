"""
Birinci dereceden isal sistem modeli.
dT/dt = (K * u - (T - T_ambient)) / tau

T       : anlik sicaklik (derece)
u       : kontrol girisi (0.0 - 1.0 arasi, isitici gucu)
K       : sistem kazanci
tau     : zaman sabiti (sistem ne kadar yavas tepki veriyor)
ambient : ortam sicakligi
"""


class ThermalSystem:
    def __init__(self, K=100.0, tau=5.0, initial_temp=20.0, ambient=20.0):
        self.K = K
        self.tau = tau
        self.T = initial_temp
        self.ambient = ambient

    def update(self, u, dt):
        """
        Bir dt zaman adimi kadar sistemi ilerletir.
        Euler integrasyonu kullanir.
        """
        dT = (self.K * u - (self.T - self.ambient)) / self.tau
        self.T += dT * dt
        return self.T