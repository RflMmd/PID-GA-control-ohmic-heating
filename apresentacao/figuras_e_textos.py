import matplotlib.pyplot as plt

def apresentacao_resultados(setpoint, melhor_individuo_be, informacoes_melhor_individuo_be, melhor_individuo_ga,informacoes_melhor_individuo_ga, outras_GA):
    print("\n======================================================")
    print(f"Considerando um SetPoint de {setpoint:.2f} C:")
    print("Os valores das constantes do controlador sao:\n")

    print("Brute Force:")
    print(f"Kp = {melhor_individuo_be[0]:.4f} | Ki = {melhor_individuo_be[1]:.4f} | Kd = {melhor_individuo_be[2]:.4f}")
    print(f"Overshoot = {informacoes_melhor_individuo_be['overshoot [%]']:.3f}")
    print(f"Settling Time = {informacoes_melhor_individuo_be['SettTime [s]']:.3f}")
    print(f"PWM Max = {informacoes_melhor_individuo_be['umax [PWM]']:.3f}")

    print("----------------------------------------------------")
    print("Genetic Algorithm:")
    print(f"Kp = {melhor_individuo_ga[0]:.4f} | Ki = {melhor_individuo_ga[1]:.4f} | Kd = {melhor_individuo_ga[2]:.4f}")
    print(f"Overshoot = {informacoes_melhor_individuo_ga['overshoot [%]']:.3f}")
    print(f"Settling Time (s) = {informacoes_melhor_individuo_ga['SettTime [s]']:.3f}")
    print(f"PWM Max = {informacoes_melhor_individuo_ga['umax [PWM]']:.3f}")



    
    
    # Figuras
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))  # 3 linhas, 1 coluna

    # Evolucao das Geracoes
    geracoes = [r[0] for r in outras_GA["custo_geracao"]]
    custos = [r[1] for r in outras_GA["custo_geracao"]]
    axs[0].plot(geracoes, custos, '-*r')
    axs[0].grid(True)
    axs[0].set_ylabel("Custo")
    axs[0].set_title("Melhor resultado - GA")

    # Resposta do Sistema
    axs[1].plot(outras_GA["tempo"], outras_GA["resultado"])
    axs[1].grid(True)
    axs[1].set_ylabel("Saída")
    axs[1].set_xlabel("Tempo")

    # Sinal do Controlador
    axs[2].plot(outras_GA["tempo"], outras_GA["controle"])
    axs[2].grid(True)
    axs[2].set_ylabel("Controle")
    axs[2].set_xlabel("Tempo")
    # Ajusta o layout
    plt.tight_layout()
    plt.show()
