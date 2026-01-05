import numpy as np

def funObj(y, u, setpoint, peso, fator):
    funcao = np.sum(np.abs(setpoint - y)) + peso * np.sum(u) + fator
    return funcao
