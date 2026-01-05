import numpy as np
import json
from pathlib import Path
from otimizacao import busca_exaustiva
from otimizacao import GA
from apresentacao import apresentacao_resultados
from data import salvar

def main():
    diretorio = Path(__file__).parent
    config_caminho = diretorio / "config.json"
    with open(config_caminho, "r", encoding="utf-8") as file:
        config = json.load(file)
    # ---------------------
    # Salvamento Automático
    auto_save = config["auto_save"]
    # ---------------------

    setpoint = config["setpoint"]  # Setpoint [ºC]
    tfim = config["tempo_simulado"]  # Tempo simulado [s]

    dt = config["passo_de_tempo"]    # Passo de tempo [s]
    tempo = np.arange(0, tfim + 1, dt)
    acomodacao = config["acomodacao_offset"] # % do offset considerado

    LimKp  = config["Limites_Kp"] # Limites do Kp
    LimKi = config["Limites_Ki"] # Limites do Ki
    LimKd = config["Limites_Kd"] # Limites do Kd
    N = config["Filtro_derivativo"] # Filtro do termo derivativo

    limPWMaceitavel  =  config["Faixa_Aceitavel_PWM_max"] # Limites do PWM máximo aceitáve;

    # Config Funcao Objetivo
    peso = config["peso_controle_funObj"] # peso da soma do sinal de controle (Incentiva a consumir menos)

    # Config Busca Exaustiva
    pontos_busca = config["Pontos_Busca_Exaustiva"] # Número de pontos de busca

    # Config Algoritmo Genético
    Nindividuos = config["Individuos_GA"] # Número de indivíduos em cada geração
    MaxGeracao = config["Geracoes_GA"]  # Número de gerações
    mutacao = config["Chance_mutacao"]  # Chance de mutação
    cruzamento = config["Chance_cruzamento"]  # Chance de cruzamento

    ## Resolucao
    melhor_individuo_be, informacoes_melhor_individuo_be = busca_exaustiva(pontos_busca, acomodacao, LimKp, LimKi, LimKd, N, limPWMaceitavel, setpoint, tfim, tempo)
    melhor_individuo_ga, informacoes_melhor_individuo_ga, outras_GA = GA(Nindividuos, MaxGeracao, mutacao, cruzamento, acomodacao, LimKp, LimKi, LimKd, N, limPWMaceitavel, setpoint, tempo, tfim, peso, melhor_individuo_be)

    apresentacao_resultados(setpoint, melhor_individuo_be, informacoes_melhor_individuo_be, melhor_individuo_ga, informacoes_melhor_individuo_ga, outras_GA)

    configs = {"Setpoint [ºC]": setpoint,
            "tempo simulado [s]":tfim, 
            "Offset considerado [%]": acomodacao,
            "Pontos de Busca Exaustiva": pontos_busca,
            "Indivíduos GA": Nindividuos,
            "Gerações GA": MaxGeracao,
            "Chance de Mutação [%]": mutacao,
            "Chance do Cruzamento [%]": cruzamento}

    Dados = {"Configurações": configs,
            "Constantes melhor controlador - Busca Exaustiva [Kp, Ki, Kd]": melhor_individuo_be, 
            "Dados Busca Exaustiva": informacoes_melhor_individuo_be, 
            "Constantes melhor controlador - Algoritmo Genético [Kp, Ki, Kd]": melhor_individuo_ga, 
            "Dados GA": informacoes_melhor_individuo_ga}
    print(Dados)

    if auto_save:
        print("\nSalvamento Automático está ativado. Os dados estão sendo armazenados a cada execução!!")
        salvar(Dados)
    else:
        while True:
            try:
                # Salvar Resultados
                salvamento = int(input("\nSalvamento Automático está desativado\nDeseja salvar o resultado?\n1 - Salvar\n0 - Não\n\n"))
                if salvamento == 1:
                    salvar(Dados)
                    break
                elif salvamento == 0:
                    print("\nDados não salvos!\n")
                    break
                else:
                    print("Entrada inválida. Digite apenas números.")

            except ValueError:
                print("Entrada inválida. Digite apenas números.")

if __name__ == "__main__":
    main()
