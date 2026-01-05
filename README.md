#########
# PT-BR #
#########

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


## Estrutura
├── main.py
├── config.json
├── otimizacao/
│ ├── busca_exaustiva.py
│ ├── algoritmo_genetico.py
│ └── funcao_objetivo.py
├── modelo/
│ └── modelo_do_processo.py
├── simulacao/
│ ├── avaliacao.py
│ └── simulacao.py
├── controlador/
│ └── controlador_PID.py
├── apresentacao/
│ └── figuras_e_textos.py
├── data/
│ ├── historico/
│ │ └── [...]
│ ├── dados_ultima_execucao.json
│ └── salvar.py
└── README.md
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


##  Execução

```
python main.py
```
---


## O programa irá
- Ler os parâmetros definidos em config.json
- Executar a Busca Exaustiva
- Executar o Algoritmo Genético
- Apresentar os resultados
- Salvar os dados automaticamente (quando habilitado)
---


**Autor:**
Rafael Felipe Neves Mamedio
_Engenheiro Químico_
Área: _Modelagem, Simulação e Controle de Processos_


##########
#   EN   #
##########
