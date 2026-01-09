PT-BR: _A função de transferência empregada neste projeto foi derivada de um modelo dinâmico, baseado em princípios físicos, do processo de aquecimento ôhmico. O modelo baseia-se em balanços de energia acoplados para o material processado e a parede da célula ôhmica, considerando convecção natural e condutividade elétrica dependente da temperatura. As equações governantes foram discretizadas utilizando o método das diferenças finitas, linearizadas em torno de um ponto de operação e transformadas para o domínio de Laplace. Os parâmetros do modelo foram obtidos experimentalmente, e os controladores otimizados foram implementados e validados em um sistema térmico real._

EN: _The transfer function employed in this project was derived from a dynamic, physics-based model of the ohmic heating process. The model is based on coupled energy balances for the processed material and the ohmic cell wall, considering natural convection and temperature-dependent electrical conductivity. The governing equations were discretized using the finite difference method, linearized around an operating point, and transformed into the Laplace domain. Model parameters were obtained experimentally, and the optimized controllers were implemented and validated in a real thermal system._
##

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


### Nota
#### Este projeto foi desenvolvido para ajudar a identificar melhores parâmetros para um controlador PID experimental utilizado para controlar a temperatura de uma célula de aquecimento ôhmico.
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


### Note
#### This project was developed to help identify improved parameters for an experimental PID controller used to regulate the temperature of an ohmic heating cell.
---


**Author:**
**Rafael Mamedio**  
Chemical Engineer   
Field of expertise: Process Modeling, Simulation, and Control
