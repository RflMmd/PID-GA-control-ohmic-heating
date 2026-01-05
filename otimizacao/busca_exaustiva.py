import numpy as np
from controlador import ft_PID
from modelo import aquecimento_ohmico
from simulacao import simulacao_do_sistema
from simulacao import overshoot, settling_time

def busca_exaustiva(pontos, acomodacao, LimKp, LimKi, LimKd, N, limPWMaceitavel, setpoint, tfim, tempo):
    Kpmin, Kpmax = LimKp
    Kimin, Kimax = LimKi
    Kdmin, Kdmax = LimKd
    PMWmin, PMWmax = limPWMaceitavel

    Overshoot_B = []
    Sett_Time_B = []
    umax_B = []
    Kp_list, Ki_list, Kd_list = [], [], []
    
    for i in range(pontos):
        Kp_val = np.random.uniform(Kpmin, Kpmax)
        Ki_val = np.random.uniform(Kimin, Kimax)
        Kd_val = np.random.uniform(Kdmin, Kdmax)

        C = ft_PID(Kp_val, Ki_val, Kd_val, N)
        G = aquecimento_ohmico()
        _, y, u = simulacao_do_sistema(G, C, tempo, setpoint)

        # Métricas
        if np.max(y) > setpoint:
            OS = overshoot(y, setpoint) 
        else:
            OS = 0.0  # sem overshoot
        Settling = settling_time(y, tempo, setpoint, acomodacao) 
        erro = np.abs(y - setpoint)
        tolerancia = acomodacao * setpoint
        abaixo = np.where(erro < tolerancia)[0]

        if len(abaixo) > 0:
            Settling = tempo[abaixo[-1]]

        # Armazenar
        Kp_list.append(Kp_val)
        Ki_list.append(Ki_val)
        Kd_list.append(Kd_val)
        Overshoot_B.append(OS)
        Sett_Time_B.append(Settling)
        umax_B.append(np.max(u))

    # Melhor da busca aleatória
    OSmin = np.inf
    ind = -1
    for i in range(pontos):
        if umax_B[i] <= PMWmax and umax_B[i] > PMWmin:
            if Overshoot_B[i] < OSmin:
                OSmin = Overshoot_B[i]
                ind = i

    melhor_forca_bruta = [Kp_list[ind], Ki_list[ind], Kd_list[ind]]
    OS = float(Overshoot_B[ind])
    ST = float(Sett_Time_B[ind])
    max_u = float(umax_B[ind])
    melhor_FB_info = {
        "constantes [Kp, Ki, Kd]": melhor_forca_bruta,
        "overshoot [%]": OS,
        "SettTime [s]": ST,
        "umax [PWM]": max_u
    }


    return melhor_forca_bruta, melhor_FB_info
