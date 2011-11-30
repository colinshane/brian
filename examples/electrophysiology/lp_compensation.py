"""
Lp electrode compensation example.
"""
from brian import *
from brian.library.electrophysiology import Lp_compensate
import numpy

# load the injected current and the raw voltage trace of a neuron
# in response to this current. The two variables are 1D vectors of 
# equal length.
I = numpy.load("current.npy")
Vraw = numpy.load("trace.npy")

# launch the compensation procedure. The sampling period must be specified
# (here, 10 kHz). This function returns the compensated trace, and the
# corresponding neuron+electrode parameters: R, tau, Vr, Re, taue.
Vcomp, params = Lp_compensate(I, Vraw, .1*ms)

print "Compensation terminated, Re=%.1f MOhm, taue=%.2f ms" % \
    (params[3,0]/Mohm, params[4,0]/ms)

subplot(211)
plot(I, 'k')

subplot(212)
plot(Vraw, 'k')
plot(Vcomp, 'r')

show()
