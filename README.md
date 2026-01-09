# PT-BR #

# Otimização de Controlador PID com Busca Exaustiva e Algoritmo Genético

Projeto para sintonia de controladores PID utilizando Busca Exaustiva e Algoritmo Genético, aplicado à simulação de um processo térmico com restrições de PWM.
---

## Contexto Científico:
_Este repositório implementa um modelo dinâmico derivado fisicamente do processo de aquecimento ôhmico, baseado em balanços de energia e condutividade elétrica dependente da temperatura. Os parâmetros do modelo foram identificados experimentalmente e os controladores otimizados foram validados em um sistema térmico real._



## Objetivo do Projeto
Este repositório implementa uma estratégia para a otimização de um controlador PID aplicado em sistema de aquecimento ôhmico baseada em uma função de transferência derivada de um modelo dinâmico fundamentado em princípios físicos.

Este projeto tem como objetivo:
- Ajustar automaticamente os parâmetros **Kp, Ki e Kd** de um controlador PID  
- Minimizar o erro de regime permanente e o esforço de controle  
- Permitir a simulação de diferentes sistemas por meio de **funções de transferência**  
- Facilitar a configuração e reprodutibilidade dos experimentos via arquivo `config.json`
---


## Metodologias

### 1) Busca Exaustiva
- Varredura discreta do espaço de busca dos parâmetros PID  
- Avaliação da função objetivo para cada combinação  
- Garantia do melhor desempenho dentro do espaço discretizado e critérios definidos

### 2) Algoritmo Genético
- População inicial baseada na melhor solução da Busca Exaustiva  
- Operadores utilizados:
  - Seleção por torneio  
  - Cruzamento  
  - Mutação  
  - Elitismo 

### 3) Função Objetivo
A função objetivo penaliza:
- Soma do erro ao longo do tempo  
- Elevada ação de controle  
- Offset fora da faixa aceitável definida 
---


## Requisitos

- Python ≥ 3.9  
- Bibliotecas:
  - numpy
  - pathlib
  - json
  - control
  - datetime
  - matplotlib.pyplot
---


## Execução

```
python main.py
```
---


## O programa irá
- Ler os parâmetros definidos em `config.json`
- Executar a Busca Exaustiva
- Executar o Algoritmo Genético
- Apresentar os resultados
- Salvar os dados automaticamente (quando habilitado)
---


### Nota
#### Este projeto foi desenvolvido para ajudar a identificar melhores parâmetros para um controlador PID experimental utilizado para controlar a temperatura de uma célula de aquecimento ôhmico.
---


*Publications*:
- R. F. N. Mamedio & G. R. Ströher, “Implementação de lógica de controle para o tratamento térmico por meio da tecnologia de aquecimento ôhmico”, Anais do XXX Seminário de Iniciação Científica e Tecnológica da UTFPR, Curitiba, PR, 2025 (link: https://www.even3.com.br/anais/sei-sicite-2025-593680/1256543-implementacao-de-logica-de-controle-para-o-tratamento-termico-por-meio-da-tecnologia-de-aquecimento-ohmico_
---


**Autor:**
**Rafael Mamedio**  
Engenheiro Químico  
Área de atuação: Modelagem, Simulação e Controle de Processos


#   EN   #

# PID Controller Optimization Using Exhaustive Search and Genetic Algorithm

Project for tuning PID controllers using Exhaustive Search and a Genetic Algorithm, applied to the simulation of a thermal process with PWM constraints.
---

## Scientific Context
_This repository implements a physically derived dynamic model of the ohmic heating process, based on energy balances and temperature-dependent electrical conductivity. Model parameters were experimentally identified, and the optimized controllers were validated on a real thermal system._


## Project Objective
This repository implements a strategy for optimizing a PID controller applied to an ohmic heating system based on a transfer function derived from a dynamic model grounded in physical principles.

This project aims to:
- Automatically tune the **Kp, Ki, and Kd** parameters of a PID controller
- Minimize steady-state error and control effort
- Allow the simulation of different systems through **transfer functions**  
- Facilitate configuration and experiment reproducibility via a `config.json` file
---


## Methodologies

### 1) Exhaustive Search
- Discrete scanning of the PID parameter search space
- Evaluation of the objective function for each combination
- Guaranteeing optimal performance within the discretized space and defined criteria

### 2) Genetic Algorithm
- Initial population based on the best solution from the Exhaustive Search
- Operators used:
  - Tournament selection
  - Crossover
  - Mutation
  - Elitism 

### 3) Objective Function
The objective function penalizes:
- Cumulative error over time
- Excessive control action
- Offset outside the defined acceptable range
---


## Requirements

- Python ≥ 3.9  
- Libraries:
  - numpy
  - pathlib
  - json
  - control
  - datetime
  - matplotlib.pyplot
---


## Execution

```
python main.py
```
---


## The program will
- Read the parameters defined in `config.json`
- Run the Exhaustive Search
- Run the Genetic Algorithm
- Display the results
- Automatically save data (when enabled)
---


### Note
#### This project was developed to help identify improved parameters for an experimental PID controller used to regulate the temperature of an ohmic heating cell.
---


*Publications*:
- R. F. N. Mamedio & G. R. Ströher, “Implementação de lógica de controle para o tratamento térmico por meio da tecnologia de aquecimento ôhmico”, Anais do XXX Seminário de Iniciação Científica e Tecnológica da UTFPR, Curitiba, PR, 2025 (link: https://www.even3.com.br/anais/sei-sicite-2025-593680/1256543-implementacao-de-logica-de-controle-para-o-tratamento-termico-por-meio-da-tecnologia-de-aquecimento-ohmico_
---


**Author:**
**Rafael Mamedio**  
Chemical Engineer   
Field of expertise: Process Modeling, Simulation, and Control
