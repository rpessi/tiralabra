'''A module for getting familiar with different libraries and datatypes,
heavily based on tutorial examples with some modifications'''

import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft
import soundfile as sf
import sounddevice as sd

birds_file = "soundfiles/birds.mp3"

y, sample_rate = librosa.load(birds_file, duration=10)
print("Sample rate: ", sample_rate)
print("y: ", y[:20])
print("Y:n arvoja yhteensä: ", len(y))
sf.write('testplay.wav', y, sample_rate)
sd.play(y, sample_rate)
sd.wait()

plt.style.use('seaborn-v0_8-pastel')

ts = 1.0/sample_rate
t = np.arange(0,10,ts)

windows = [] #divide in 10 windows
for i in range(0, sample_rate*10, sample_rate):
    windows.append(y[i:i+sample_rate])

time = 0
for window in windows[:5]:
    y = window
    t = np.arange(time,time+1,ts)

    X = fft(y)
    print("fft: ", X[:5])
    N = len(X)
    print("Arvoja yhteensä: ", N)
    n = np.arange(N)
    T = N/sample_rate
    freq = n/T 

    plt.figure(figsize = (12, 6))
    plt.subplot(121)

    plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude |X(freq)|')
    plt.xlim(0, 8000)

    plt.subplot(122)
    plt.plot(t, ifft(X), 'r')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()
    time = time+1
