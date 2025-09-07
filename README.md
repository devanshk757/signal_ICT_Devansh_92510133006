# signal_ict_devansh_92510133006

A custom Python package demonstrating fundamental concepts of **Signals and Systems**.  
This package contains unitary signals, trigonometric signals, and signal operations.

## 📦 Modules

- **unitary_signals.py**
  - `unit_step(n)` – Generates a unit step signal.
  - `unit_impulse(n)` – Generates a unit impulse signal.
  - `ramp_signal(n)` – Generates a ramp signal.

- **trigonometric_signals.py**
  - `sine_wave(A, f, phi, t)` – Generates a sine wave.
  - `cosine_wave(A, f, phi, t)` – Generates a cosine wave.
  - `exponential_signal(A, alpha, t)` – Generates an exponential signal.

- **operations.py**
  - `time_shift(signal, k)` – Shifts a signal in time.
  - `time_scale(signal, k)` – Scales a signal in time.
  - `signal_addition(x, y)` – Adds two signals.
  - `signal_multiplication(x, y)` – Multiplies two signals element-wise.

## ⚙️ Installation

### From TestPyPI:
```bash
pip install --index-url https://test.pypi.org/simple/ signal_ict_devansh_92510133006