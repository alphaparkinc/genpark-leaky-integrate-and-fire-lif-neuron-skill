import sys
import json
from client import LIFNeuron

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "simulate":
        neuron = LIFNeuron()
        return neuron.simulate_trace(params.get("current_trace", [20.0] * 50))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
