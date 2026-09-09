class LIFNeuron:
    """Leaky Integrate-and-Fire (LIF) biological neuron dynamics simulator."""
    def __init__(self, tau_m: float = 10.0, v_rest: float = -70.0, v_thresh: float = -50.0,
                 v_reset: float = -75.0, r_m: float = 1.0, refractory_steps: int = 2):
        self.tau_m = tau_m
        self.v_rest = v_rest
        self.v_thresh = v_thresh
        self.v_reset = v_reset
        self.r_m = r_m
        self.refractory_steps = refractory_steps

        self.v = v_rest
        self.refractory_counter = 0

    def step(self, current_injection: float, dt: float = 1.0) -> tuple[int, float]:
        if self.refractory_counter > 0:
            self.refractory_counter -= 1
            self.v = self.v_reset
            return 0, self.v

        # dv/dt = (-(v - v_rest) + R*I) / tau_m
        dv = (-(self.v - self.v_rest) + self.r_m * current_injection) * (dt / self.tau_m)
        self.v += dv

        if self.v >= self.v_thresh:
            self.v = self.v_reset
            self.refractory_counter = self.refractory_steps
            return 1, self.v_thresh # Emits spike
        return 0, self.v

    def simulate_trace(self, current_trace: list[float], dt: float = 1.0) -> dict:
        spikes = []
        voltage_trace = []
        for i_e in current_trace:
            spk, v = self.step(i_e, dt=dt)
            spikes.append(spk)
            voltage_trace.append(round(v, 2))
        return {
            "total_steps": len(current_trace),
            "spike_count": sum(spikes),
            "firing_rate_hz": (sum(spikes) / (len(current_trace) * dt * 0.001)) if current_trace else 0.0,
            "spikes": spikes,
            "membrane_potential_trace": voltage_trace[:10]
        }
