import requests
from datetime import date

def coletar_dados_inmet(municipio, estado):
    """
    Consome a API do INMET para buscar temperatura e umidade de um município.
    
    :param municipio: Nome da cidade (ex: 'Belo Horizonte').
    :param estado: Sigla do estado (ex: 'MG').
    :return: Dicionário formatado como {'HH:MM': (temperatura, umidade)}.
    """
    url_estacoes = "https://apitempo.inmet.gov.br/estacoes/T"
    res_estacoes = requests.get(url_estacoes)
    
    if res_estacoes.status_code != 200:
        return "Erro ao acessar API de estações"

    estacoes = res_estacoes.json()
    codigo = None
    for e in estacoes:
        if municipio.upper() in e["DC_NOME"].upper() and estado.upper() == e["SG_ESTADO"]:
            codigo = e["CD_ESTACAO"]
            break
            
    if not codigo:
        return "Município não encontrado."

    hoje = date.today().strftime("%Y-%m-%d")
    url_medicoes = f"https://apitempo.inmet.gov.br/estacao/{hoje}/{hoje}/{codigo}"
    res_med = requests.get(url_medicoes)

    resultado = {}
    if res_med.status_code == 200 and res_med.text:
        medicoes = res_med.json()
        for m in medicoes:
            hora = f"{m['HR_MEDICAO'][:2]}:{m['HR_MEDICAO'][2:]}"
            t = m.get("TEM_INS")
            u = m.get("UMD_INS")
            
            if t is not None and u is not None:
                resultado[hora] = (float(t), float(u))
    
    return resultado