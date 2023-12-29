import numpy as np
import matplotlib.pyplot as plt

def encode(bitstream, amplitude, n_sample):
    '''
        n_sample = t * sampling_rate
    '''
    # Create time axis for signal
    time_axis = np.arange(len(bitstream) * int(n_sample))

    # Create signal by setting the amplitude of each bit for the duration of that bit
    signal = np.zeros(len(time_axis))
    for i in range(len(bitstream)):
        start_index = i * int(n_sample)
        end_index = (i + 1) * int(n_sample)
        signal[start_index:end_index] = bitstream[i] * amplitude

    return signal

def draw_signal(signal, amplitude, t, sampling_rate):
    
    time_axis = np.arange(len(signal)) / sampling_rate
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(time_axis, signal, drawstyle='steps-post', linewidth=1.5)
    ax.scatter(time_axis, signal, s=30, c='black')
    ax.set_xlabel('Time')
    ax.set_ylabel('Signal Amplitude')
    ax.set_title('Unipolar NRZ Signal')
    plt.xlim(0, 10)
    plt.grid(True)
    plt.show()

def decode(signal, n_sample):
    decoded_bits = []
    for i in range(0,len(signal),int(n_sample)):
        if signal[i] > 0:
            decoded_bits.append(1)
        else:
            decoded_bits.append(0)
    return np.array(decoded_bits)
