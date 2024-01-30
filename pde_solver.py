from scipy.fft import fft, ifft
from odeintz import odeintz
import numpy as np

def solve(t, y_0, k=1):
    # Get fourier transform
    F_0 = fft(y_0)
    f = np.arange(len(y_0)) # list of frequencies
    dF_dt_0 = np.zeros_like(F_0)

    # Apply differential equation to fourier transform
    F = np.split(
        odeintz(vibration_frequency_equation, np.concatenate([F_0, dF_dt_0]), t, args=(f, k)), 2, axis=1
    )[0]


    # Apply inverse fourier fourier transform to solved frequency domains for solution
    y = ifft(F).real.astype('float')

    return y

def vibration_frequency_equation(u, t, f, k):
    F, dF_dt = np.split(u, 2)
    du = np.concatenate([dF_dt, -((2*np.pi*k*f)**2)*F])
    return du