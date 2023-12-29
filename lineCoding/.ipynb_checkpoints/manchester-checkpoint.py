import numpy as np
import matplotlib.pyplot as plt

def encode(bitstream, amplitude, t, sampling_rate):
    # Create time axis for signal
    time_axis = np.arange(len(bitstream) * int(t*sampling_rate))

    # Create signal using Manchester line coding
    signal = np.zeros(len(time_axis))
    for i in range(len(bitstream)):
        start_index = i * int(t * sampling_rate)
        midpoint_index = start_index + int((t/2) * sampling_rate)
        end_index = (i + 1) * int(t * sampling_rate)
        if bitstream[i] == 0:
            signal[start_index:midpoint_index] = amplitude
            signal[midpoint_index:end_index] = -amplitude
        else:
            signal[start_index:midpoint_index] = -amplitude
            signal[midpoint_index:end_index] = amplitude

    return signal

def draw_signal(signal, amplitude, t, sampling_rate):
    
    time_axis = np.arange(len(signal)) / sampling_rate
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(time_axis, signal, drawstyle='steps-post', linewidth=1.5)
    #ax.scatter(time_axis, signal, s=30, c='black')
    ax.set_xlabel('Time')
    ax.set_ylabel('Signal Amplitude')
    ax.set_title('Unipolar NRZ Signal')
    plt.xlim(0, 10)
    plt.grid(True)
    plt.show()


def decode(signal, amplitude, n_sample):
    pass
