import numpy as np
import matplotlib.pyplot as plt
from signal_ict_devansh_92510133006.unitary_signals import unit_step, unit_impulse, ramp_signal
from signal_ict_devansh_92510133006.trigonometric_signals import sine_wave, cosine_wave
from signal_ict_devansh_92510133006.operations import time_shift, signal_addition, signal_multiplication

def main():
    print("Starting Signal Processing Demonstrations...")
    
    # 1. Generate and plot unit step & unit impulse (length 20)
    print("1. Generating Unit Step and Unit Impulse signals...")
    n = np.arange(-10, 10, 1)  # Length 20: -10 to 9
    step = unit_step(n)
    impulse = unit_impulse(n)
    
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.stem(n, step)  # Removed use_line_collection=True
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.stem(n, impulse)  # Removed use_line_collection=True
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Generate sine wave (A=2, f=5Hz, phi=0, t=0..1 sec)
    print("2. Generating Sine Wave...")
    t = np.linspace(0, 1, 500)
    sine = sine_wave(2, 5, 0, t)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, sine)
    plt.title("Sine Wave (A=2, f=5Hz, φ=0)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    # 3. Perform time shifting on sine wave by +5 units
    print("3. Time Shifting Sine Wave...")
    shifted_sine = time_shift(sine, 5)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, sine, label="Original Sine", alpha=0.7)
    plt.plot(t, shifted_sine, label="Shifted Sine (+5)", alpha=0.7)
    plt.legend()
    plt.title("Time Shifting Example")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    # 4. Add unit step and ramp signal
    print("4. Adding Unit Step and Ramp signals...")
    ramp = ramp_signal(n)
    added = signal_addition(step, ramp)
    
    plt.figure(figsize=(10, 6))
    plt.stem(n, added)  # Removed use_line_collection=True
    plt.title("Addition: Unit Step + Ramp")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    # 5. Multiply sine and cosine of same frequency
    print("5. Multiplying Sine and Cosine waves...")
    cosine = cosine_wave(2, 5, 0, t)
    multiplied = signal_multiplication(sine, cosine)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, multiplied)
    plt.title("Multiplication: Sine × Cosine")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    print("All 5 demonstrations completed successfully!")

if __name__ == "__main__":
    main()