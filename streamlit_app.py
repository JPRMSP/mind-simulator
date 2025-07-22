import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.set_page_config(page_title="Mind Simulator", page_icon="🧠")
st.title("🧠 Mind Simulator: Simulated BCI Mental State Detector")
st.markdown("Simulate brain signals based on mental state and visualize how EEG patterns vary.")

# Sidebar: Choose mental state
st.sidebar.header("🧠 Select Mental State")
state = st.sidebar.selectbox("Choose your mental state:", ["Relaxed", "Focused", "Stressed"])

# Function to simulate EEG signals
def generate_signal(state):
    t = np.linspace(0, 1, 256)
    if state == "Relaxed":
        signal = np.sin(2 * np.pi * 8 * t) + 0.1 * np.random.randn(len(t))  # Alpha wave (8 Hz)
    elif state == "Focused":
        signal = np.sin(2 * np.pi * 13 * t) + 0.2 * np.random.randn(len(t))  # Beta wave (13 Hz)
    elif state == "Stressed":
        signal = np.sin(2 * np.pi * 20 * t) + 0.4 * np.random.randn(len(t))  # Gamma wave (20 Hz)
    return t, signal

# Generate signal
t, signal = generate_signal(state)

# Plot EEG Signal
st.subheader("📈 Simulated EEG Signal")
fig, ax = plt.subplots()
ax.plot(t, signal, color="purple")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude (µV)")
ax.set_title(f"Simulated EEG Signal for: {state}")
st.pyplot(fig)

# Show simplified spectral components
st.subheader("🔬 Spectral Component (Frequency Domain)")
fft = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(fft), d=1/256)  # Assuming sampling rate = 256 Hz

fig2, ax2 = plt.subplots()
ax2.plot(frequencies[:128], np.abs(fft)[:128], color="teal")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")
ax2.set_title("FFT Spectrum")
st.pyplot(fig2)

# Result Section
st.subheader("🔍 Detected Mental State")
if state == "Relaxed":
    st.success("System detected a calm and relaxed brain state. 🧘‍♂️")
elif state == "Focused":
    st.info("Brain appears to be focused and attentive. 🎯")
elif state == "Stressed":
    st.warning("Increased stress levels detected. 😥 Try relaxing.")

# Footer
st.markdown("---")
st.markdown("🧠 Developed for Brain-Computer Interface simulation | No real EEG used | Ideal for learning")
