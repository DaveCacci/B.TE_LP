# SAMPLE BMP CURVE
# Declare functions to create the BMP time-curve for later sampling (two-pool first order kinetics model)
from scipy.integrate import odeint
import numpy as np

# Define the differential equation system (ODE)
def model(state, t, k1, k2):
    '''Two-pool first order kinetics model ODEs.
    state: list of current state variables [x, y, z] 
    t: time
    k1: rate constant for rapidly biodegradable substrate
    k2: rate constant for slowly biodegradable substrate
    Returns the derivatives [dx/dt, dy/dt, dz/dt]'''
    x, y, z = state # x: rapidly biodegradable substrate, y: slowly biodegradable substrate, z: cumulative BMP produced
    dxdt = -k1 * x
    dydt = -k2 * y
    dzdt = k1 * x + k2 * y
    return [dxdt, dydt, dzdt]

def evaluate_model(x0, y0, k1, k2, horizon, steps):
    '''Evaluate the two-pool first order kinetics model.
    x0: initial rapidly biodegradable substrate (BMPinf_r)
    y0: initial slowly biodegradable substrate (BMPinf_s)
    k1: rate constant for rapidly biodegradable substrate
    k2: rate constant for slowly biodegradable substrate
    Returns time points and corresponding BMP production values.'''
    # Initial conditions
    x0 = x0
    y0 = y0
    z0 = 0.0

    # Time points to solve the equations
    t = np.linspace(0, horizon, steps)

    # Rate constants
    k1 = k1
    k2 = k2

    # Solve the differential equations
    state = odeint(model, [x0, y0, z0], t, args=(k1, k2))
    x_response = state[:, 0]
    y_response = state[:, 1]
    z_response = state[:, 2]

    return t,z_response