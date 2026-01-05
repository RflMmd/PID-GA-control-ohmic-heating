import numpy as np

def overshoot(y, sp):
    return max(0, (np.max(y) - sp) / sp * 100)

def settling_time(y, t, sp, tol):
    erro = np.abs(y - sp)
    idx = np.where(erro < tol * sp)[0]
    return t[idx[-1]] if len(idx) > 0 else t[-1]
