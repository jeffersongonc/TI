import pandas as pd
import plotly.express as px

def read_data(pFile):
    tabela = pd.read_csv(pFile)
    return tabela

def remove_column(pDF, pColumn, pAxis):
    tabela = pDF.drop(pColumn, axis=pAxis)
    return tabela

def remove_data_null(pDF):
    tabela = pDF.dropna()
    return tabela

def query_data(pDF, pQuery):
    tabela = pDF.query(pQuery)
    return tabela

def display_histogram(pDF, pColumn):
    grafico = px.histogram(pDF, x=pColumn, color=pColumn)
    return grafico

# Lendo dados
data = read_data('cancelamentos.csv')
print(data)

# Removendo Coluna 'CustomerID'
data = remove_column(data, 'CustomerID', 1)
print(data)

# Removendo dados Nulos
data = remove_data_null(data)
print(data)

# Quentidade de pessoas que 'cancelou'
print(query_data(data, 'cancelou == 1.0')['cancelou'].value_counts())

# Quentidade de pessoas que 'Nao cancelou'
print(query_data(data, 'cancelou != 1.0')['cancelou'].value_counts())

# Duração de contratos em %
print(data['duracao_contrato'].value_counts(normalize=True))

# Duração de contratos
print(data['duracao_contrato'].value_counts())

# Análise de contratos
print(data.groupby('duracao_contrato').mean(numeric_only=True))

# Análise de 'assinatura' em %
print(data['assinatura'].value_counts(normalize=True))

# Análise de 'assinatura'
print(data['assinatura'].value_counts())

# Gráfico
grafico = display_histogram(data, 'cancelou')
grafico.show()