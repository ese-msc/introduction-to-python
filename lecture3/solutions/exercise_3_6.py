import math


def calc_material_velocity(mu, k, rho):
    mu *= 1e9  # GPa
    k *= 1e9  # GPa

    if mu < 0 or k < 0 or rho < 0:
        raise ValueError

    vp = math.sqrt((k + 4*mu/3) / rho)
    vs = math.sqrt(mu/rho)

    return vp, vs
