import numpy as np
import sounddevice as sd
import time

def play_gentle_notification():
    # Parameters for a gentle notification sound
    sample_rate = 44100  # Sample rate in Hz
    duration = 0.5  # Duration in seconds
    frequency = 440  # A4 note (440 Hz)
    
    # Generate a sine wave with a smooth envelope
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    envelope = np.sin(np.pi * t / duration)  # Smooth envelope to avoid clicks
    tone = 0.3 * envelope * np.sin(2 * np.pi * frequency * t)
    
    # Play the sound
    sd.play(tone, sample_rate)
    sd.wait()  # Wait until the sound is done playing

if __name__ == "__main__":
    # Install if needed: pip install numpy sounddevice
    play_gentle_notification()