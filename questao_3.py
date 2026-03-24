import pandas as pd
"""
Objetivo: Limpeza e padronização de dados jurídicos.
Tratamentos: Remoção de IDs nulos, padronização de texto e conversão monetária.
"""
dados_extraidos = {
    'id_processo': [101, 102, None, 104, 105],
    'valor_causa': ['R$ 1.500,00', '2000', 'R$ 350,50', '5000.00', None],
    'status': ['Ativo', 'encerrado', 'ATIVO', 'Arquivado', 'Ativo'],
    'estado': ['SP', 'RJ', 'sp', 'MG', 'SP']
}

df = pd.DataFrame(dados_extraidos)

df = df.dropna(subset=['id_processo'])

df['status'] = df['status'].str.title()

df['valor_causa'] = (
    df['valor_causa']
    .str.replace('R$', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.')
    .astype(float)
)

print(df)