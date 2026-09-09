from client import LIFNeuron

def main():
    print("=== LIF Biological Spiking Neuron Simulator ===")
    neuron = LIFNeuron(tau_m=10.0, v_rest=-70.0, v_thresh=-50.0, v_reset=-75.0)

    # Sustained input current of 25.0 mA for 100 timesteps
    trace = [25.0] * 100
    res = neuron.simulate_trace(trace)
    print("Simulation summary:", res["total_steps"], "steps,", res["spike_count"], "spikes.")
    print("Firing rate:", res["firing_rate_hz"], "Hz")
    assert res["spike_count"] > 0
    print("LIF Neuron Simulator verified successfully!")

if __name__ == "__main__":
    main()
