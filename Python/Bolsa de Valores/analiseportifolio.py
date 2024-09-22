import pandas as pd
import numpy as np
import yfinance as yf
# Nome dos ativos
ativos = ['ABEV3.SA', 'PETR4.SA', 'VALE3.SA', 'BRFS3.SA', 'ALUP4.SA']

# Início e Fim da Análise
data_inicio = pd.to_datetime('2021-01-01')
data_fim = pd.to_datetime('2022-01-01')

# Pesos atribuídos a cada ativo 
pesos = np.array([0.20,0.20,0.20,0.20,0.20])

# Coleta dos dados de fechamento ajustado no yfinance ['Adj Close']
carteira = yf.download(ativos, start=data_inicio, end=data_fim)['Adj Close']

# Retorno da carteira = Soma dos Pesos x Retornos diários
retornos = carteira.pct_change().dropna()
retornos = (retornos*pesos).sum(axis=1)

# Retorno médio anualizado = retorno da carteira X 252 (dias úteis)
dias_uteis = 252
retorno_medio_anualizado = (retornos.mean()*dias_uteis)
retorno_medio_anualizado

# Primeiro calcular a volatilidade da carteira e atualizar
cov = carteira.pct_change().cov()
vol_diaria = np.sqrt(np.dot(pesos.T, np.dot(cov, pesos)))
vol_ano = vol_diaria*np.sqrt(dias_uteis)

# Agora calcular o shape ratio
rf = 0.1375
shape_ratio = ((retornos.mean()*dias_uteis)-rf)/(vol_ano)
print(shape_ratio)

# Cálculo do máximo drawdown

# Cálculo dos retornos
retornos = carteira.pct_change()
retornos.fillna(0, inplace=True)

# Retorno acumulado
retorno_acumulado = (1+retornos).cumprod()
retorno_acumulado_carteira = pd.Series((retorno_acumulado*pesos).sum(axis=1), name='Carteira')

# Calcula o ponto máximo do portifólio
pico = retorno_acumulado_carteira.expanding(min_periods=1).max()

# E agora a razão entre seu ponto mínimo de queda
dd = (retorno_acumulado_carteira/pico)-1
drawdown = dd.min()
print(drawdown)