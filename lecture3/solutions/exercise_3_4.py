def displacement(t, v0, g=9.81):
    if t < 0 or v0 < 0:
        raise ValueError('t and v0 cannot be negative.')
    return v0*t - 0.5*g*t**2
