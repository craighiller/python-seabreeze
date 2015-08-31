import seabreeze
seabreeze.use('pyseabreeze')
import seabreeze.spectrometers as sb
import matplotlib.pyplot as plt
import time
import sys

devices = sb.list_devices()
print devices
spec = sb.Spectrometer(devices[0])
spec.integration_time_micros(10000)

while(1):
    try:
        plt.clf()
        plt.scatter(spec.wavelengths(), spec.intensities())
        plt.draw()
        print "draw"
        plt.pause(0.001)
    except KeyboardInterrupt:
        print "should go down"
        spec.close()
        sys.exit()