# PT-BR #

# Otimização de Controlador PID com Busca Exaustiva e Algoritmo Genético

Projeto para sintonia de controladores PID utilizando Busca Exaustiva e Algoritmo Genético, aplicado à simulação de um processo térmico com restrições de PWM.
---


## Objetivo do Projeto

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
- Garantia de ótimo local dentro dos limites e critérios definidos  

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


### Nota: 
Este projeto foi desenvolvido para ajudar a identificar melhores parâmetros para um controlador PID experimental utilizado para controlar a temperatura de uma célula de aquecimento ôhmico.
---


**Autor:**
**Rafael Mamedio**  
Engenheiro Químico  
Área de atuação: Modelagem, Simulação e Controle de Processos


#   EN   #

# PID Controller Optimization Using Exhaustive Search and Genetic Algorithm

Project for tuning PID controllers using Exhaustive Search and a Genetic Algorithm, applied to the simulation of a thermal process with PWM constraints.
---


## Project Objective

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
- Guarantee of a local optimum within the defined limits and criteria 

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


### Note: 
This project was developed to help identify improved parameters for an experimental PID controller used to regulate the temperature of an ohmic heating cell.
---

**Author:**
**Rafael Mamedio**  
Chemical Engineer 
Field of expertise: Process Modeling, Simulation, and Control
