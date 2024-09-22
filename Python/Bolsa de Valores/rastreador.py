import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
import cotacoes

def rastrear_carteira(tickers, pesos, inicio, fim):
    dados = cotacoes.get_stock_price(tickers, inicio, fim)
    retorno = dados.pct_change()
    retorno_ponderado = (retorno * pesos).sum(axis=1)
    carteira_acumulada = (1 + retorno_ponderado).cumprod()

    return carteira_acumulada

def baixar_benchmark(ticker, inicio, fim):
    benchmark = cotacoes.get_stock_price(ticker, inicio, fim)#yf.download(ticker, start=inicio, end=fim, progress=False)['Adj Close']
    benchmark = benchmark/benchmark.iloc[0]
    return benchmark

def comparar_com_benchmark(carteira_acumulada, benchmark,
                           nome_carteira='Carteira', nome_benchmark='Benchmark'):
    df = pd.DataFrame({nome_carteira: carteira_acumulada, nome_benchmark: benchmark})
    df
    #df.plot(figsize=(10, 6))
    #plt.title('Comparação com Benchmark')
    #plt.xlabel('Data')
    #plt.ylabel('Retorno Acumulado')
    #plt.show()

tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
pesos = [0.25, 0.25, 0.25, 0.25]

# Defina o período desejado para análise
inicio = datetime(2020, 1, 1)
fim = datetime(2023, 1, 1)

# Rastreie a carteira
carteira_acumulada = rastrear_carteira(tickers, pesos, inicio, fim)

# Baixe o benchmark (S&P 500)
sp500 = baixar_benchmark('^GSPC', inicio, fim)

# Compare com o benchmark e plote o desempenho
comparar_com_benchmark(carteira_acumulada, sp500,
                       nome_carteira='Minha Carteira', nome_benchmark='S&P 500')