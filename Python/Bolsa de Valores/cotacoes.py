from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

def validate_date(vDate):
    vRet = False
    try:
        if isinstance(vDate, dt.date):
            vRet = True

        if isinstance(vDate, str):
            data_objeto = dt.datetime.strptime(vDate, "%Y-%m-%d").date()
            if isinstance(data_objeto, dt.date):
                vRet = True
    except Exception as error:
        print(f"Ocorreu o erro: {error}")

    return vRet

def convert_date_to_str(vDate, vFormat):
    vDataStr = ''
    try:
        if isinstance(vDate, str):
            vDate = dt.datetime.strptime(vDate, "%Y-%m-%d").date()
        vDataStr = vDate.strftime(vFormat)
    except Exception as error:
        print(f"Ocorreu o erro: {error}")

    return vDataStr

def get_stock_price(ticket, dt_begin, dt_end, source='yahoo'):
    price = []
    try:
        if validate_date(dt_begin) and validate_date(dt_end):
            price = yf.download(ticket, period='1d', 
                                start=convert_date_to_str(dt_begin,"%Y-%m-%d"), 
                                end=convert_date_to_str(dt_end, "%Y-%m-%d"))            
        else:
            print('Data informada inválida.')
    except Exception as error:
        print(f"Ocorreu o erro: {error}")

    return price[['Adj Close']]

def get_stock_balance(vTicket):
    try:
        vBalanco = yf.Ticker(vTicket).balance_sheet
    except Exception as error:
        print(f"Ocorreu o erro: {error}")
    return vBalanco

def get_stock_dre(vTicket):
    try:
        vDRE = yf.Ticker(vTicket).financials
    except Exception as error:
        print(f"Ocorreu o erro: {error}")
    return vDRE

def fundamentos(vTicket):
    vDF_dre = get_stock_dre(vTicket).T
    vDF_balance = get_stock_balance(vTicket).T
    vDF_price = get_stock_price(vTicket, '2019-01-01', '2023-12-31')
    vDF = pd.merge(vDF_dre, vDF_balance, right_index=True, left_index=True)
    return vDF

#df = get_stock_price('ABEV3.SA', '2019-01-01', '2023-12-31')
#df = get_stock_dre('ABEV3.SA').T
#df = get_stock_balance('ABEV3.SA').T
df = fundamentos('ABEV3.SA')
#df.info()
print(df)