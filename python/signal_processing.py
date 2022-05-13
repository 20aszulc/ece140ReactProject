import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

sample_rate = 50
data = np.genfromtxt('accel_raw_test2.txt', delimiter=',')
ax = data[:, 0]
ay = data[:, 1]
az = data[:, 2]
t = np.arange(len(ay))/sample_rate


def moving_average(x, win):
    ma = np.zeros(x.size)
    for i in np.arange(0, len(x)):
        if i < win:  # use mean until filter is "on"
            ma[i] = np.mean(x[:i + 1])
        else:
            ma[i] = ma[i - 1] + (x[i] - x[i - win]) / win
    return ma


# Detrend the Signal
def detrend(x, win=50):
    return x - moving_average(x, win)


plt.subplot(311)
plt.title('raw data')
plt.plot(t, ax, 'r')
plt.ylabel('ax')
plt.xlabel('time/s')
plt.subplot(312)
plt.plot(t, ay, 'b')
plt.ylabel('ay')
plt.xlabel('time/s')
plt.subplot(313)
plt.plot(t, az, 'g')
plt.ylabel('az')
plt.xlabel('time/s')
plt.show()


# Power Spectral Density
freqs, power = sig.welch(ax, nfft=len(ax), fs=sample_rate)
plt.subplot(211)
plt.title('Power Spectral Density of ax')
plt.plot(ax)
plt.subplot(212)
plt.plot(freqs, power)
plt.show()


x_ma = moving_average(ax, 20)
plt.plot(t, x_ma)
plt.title('Moving average of ax')
plt.show()


bl, al = sig.butter(5, 2, btype="lowpass", output='ba', fs=sample_rate)
lpx = sig.lfilter(bl, al, ax)
lpy = sig.lfilter(bl, al, ay)
lpz = sig.lfilter(bl, al, az)
plt.subplot(311)
plt.title('lowpass signals')
plt.plot(t, lpx, 'r')
plt.ylabel('ax')
plt.xlabel('time/s')
plt.subplot(312)
plt.plot(t, lpy, 'b')
plt.ylabel('ay')
plt.xlabel('time/s')
plt.subplot(313)
plt.plot(t, lpz, 'g')
plt.ylabel('az')
plt.xlabel('time/s')
plt.show()

lpx = np.round(lpx, 2)
lpy = np.round(lpy, 2)
lpz = np.round(lpz, 2)

with open('test2_processed.txt', 'w') as f:
    for idx, number in enumerate(ax):
        f.write('{}, {}, {}\n'.format(lpx[idx], lpy[idx], lpz[idx]))


