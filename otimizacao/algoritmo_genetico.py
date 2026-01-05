import numpy as np
from controlador import ft_PID
from modelo import aquecimento_ohmico
from simulacao import simulacao_do_sistema
from otimizacao import funObj
from simulacao import overshoot, settling_time

def GA(N_individuos, MaxGeracao, mutacao, cruzamento, acomodacao, LimKp, LimKi, LimKd, N, limPWMaceitavel, setpoint, tempo, tfim, peso, melhor_BE):
    Kpmin, Kpmax = LimKp
    Kimin, Kimax = LimKi
    Kdmin, Kdmax = LimKd
    PMWmin, PMWmax = limPWMaceitavel

    # Limites para o GA
    LimSup = np.array([Kpmax, Kimax, Kdmax])
    LimInf = np.array([Kpmin, Kimin, Kdmin])

    # Inicializar população
    pop = LimInf + (LimSup - LimInf) * np.random.rand(N_individuos, 3)
    results = []

    # Rodar o GA
    for Geracao in range(MaxGeracao):
        pop[0, :] = melhor_BE  # Elitismo

        Ajuste = []
        umax_GA = []

        for i in range(N_individuos):
            Kp_i, Ki_i, Kd_i = pop[i]
            C = ft_PID(Kp_i, Ki_i, Kd_i, N)

            G = aquecimento_ohmico()
            _, ymodel, u = simulacao_do_sistema(G, C, tempo, setpoint)

            # Penalizações:
            if np.max(u) > PMWmax:
                fator = 100000
            else:
                fator = 0
            
            if ymodel[-1] < 0.975 * setpoint:
                fator += 100000
            elif ymodel[-1] > 1.025 * setpoint:
                fator +=  100000

            Ajuste.append(funObj(ymodel, u, setpoint, peso, fator))
            umax_GA.append(np.max(u))

        # Torneio binário
        Nova_pop = np.zeros_like(pop)
        for i in range(N_individuos):
            I1, I2 = np.random.randint(0, N_individuos, size=2)
            vencedor = I1 if Ajuste[I1] < Ajuste[I2] else I2
            Nova_pop[i, :] = pop[vencedor, :]

        # Crossover
        for i in range(0, N_individuos - 1, 2):
            if np.random.rand() < cruzamento:
                cte = np.random.rand()
                p1, p2 = Nova_pop[i], Nova_pop[i+1]
                Nova_pop[i] = cte * p1 + (1 - cte) * p2
                Nova_pop[i+1] = cte * p2 + (1 - cte) * p1

        # Mutação
        for i in range(N_individuos):
            if np.random.rand() < mutacao:
                Nova_pop[i, :] = LimInf + (LimSup - LimInf) * np.random.rand(3)

        pop = Nova_pop.copy()

        # Avaliação final da geração
        minimos = []
        umax = []
        for i in range(N_individuos):
            Kp_i, Ki_i, Kd_i = pop[i]
            C = ft_PID(Kp_i, Ki_i, Kd_i, N)

            _, ymodel, u = simulacao_do_sistema(G, C, tempo, setpoint)

            # Penalizações:
            if np.max(u) > PMWmax:
                fator = 100000
            else:
                fator = 0

            if ymodel[-1] < 0.975 * setpoint:
                fator += 100000
            elif ymodel[-1] > 1.025 * setpoint:
                fator +=  100000

            umax.append(np.max(u))
            minimos.append(funObj(ymodel, u, setpoint, peso, fator))

        results.append([Geracao + 1, min(minimos)])
        individuos_min = np.where(minimos == min(minimos))[0]
        individuo_maior = np.where(minimos == max(minimos))[0]
        pop[individuo_maior[0], :] = pop[individuos_min[0], :]  # Elitismo
    
    # Melhor indivíduo do GA
    melhor_idx = individuos_min[0]
    melhor_GA = pop[melhor_idx]
    C = ft_PID(*melhor_GA, N)
    tmodel, resultado, sinal = simulacao_do_sistema(G, C, tempo, setpoint)

    if np.max(ymodel) > setpoint:
        Overshoot_final = overshoot(resultado, setpoint) 
    else:
        Overshoot_final= 0.0  # sem overshoot
    Settling_final = settling_time(resultado, tempo, setpoint, acomodacao) 
    umax_final = np.max(sinal)

    propriedades_melhor_GA = {
        "constantes [Kp, Ki, Kd]": melhor_GA,
        "overshoot [%]": Overshoot_final,
        "SettTime [s]": Settling_final,
        "umax [PWM]": umax_final
    }
    GA_outras_infos = {
        "resultado": resultado,
        "tempo": tmodel,
        "controle": sinal,
        "custo_geracao": results}

    return melhor_GA, propriedades_melhor_GA, GA_outras_infos
