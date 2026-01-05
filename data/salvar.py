import json
import types
import numpy as np
from datetime import datetime

def salvar(Dados):

    def serializavel(Dados):
   
        # Caso seja NamedSignal
        if type(Dados).__name__ == "NamedSignal":
            try:
                return float(Dados.array)  # Pega o valor numérico
            except:
                return str(Dados)  # fallback: salva como string

        # NumPy array
        if isinstance(Dados, np.ndarray):
            return Dados.tolist()

        # NumPy float/int
        if isinstance(Dados, (np.float64, np.float32, np.int64, np.int32)):
            return float(Dados)

        # Dicionário → processa recursivamente
        if isinstance(Dados, dict):
            return {k: serializavel(v) for k, v in Dados.items()}

        # Lista ou tupla → processa recursivamente
        if isinstance(Dados, (list, tuple)):
            return [serializavel(x) for x in Dados]

        # Outros tipos serializáveis
        if isinstance(Dados, (int, float, str, bool, type(None))):
            return Dados

        # Fallback → string
        return str(Dados)

    # Converte todo o dicionário Dados
    Dados_serializavel = serializavel(Dados)
    
    agora  = datetime.now().strftime("%d-%m-%Y_%H-%M")

    with open(".\data\dados-ultima_exec.json", "w", encoding="utf-8") as arquivo:
        json.dump(Dados_serializavel, arquivo, ensure_ascii=False, indent=4)
    with open(f".\data\historico\dados_{agora}.json", "w", encoding="utf-8") as arquivo:
        json.dump(Dados_serializavel, arquivo, ensure_ascii=False, indent=4)

    print("Os dados foram armazenados com sucesso!")
