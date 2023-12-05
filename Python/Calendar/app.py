import holidays
import pandas_market_calendars as mcal

# ======= Holidays =======
feriados_nacionais = holidays.country_holidays("BR")
feriados_estaduais = holidays.country_holidays("BR", subdiv="RJ")
feriados_nacionais_2024 = feriados_nacionais["2024-01-01":"2024-12-31"]
feriados_estaduais_2024 = feriados_estaduais["2024-01-01":"2024-12-31"]

for feriado in feriados_nacionais_2024:
    print("Feriado Nacional:", feriado.strftime("%d/%m/%Y"))

for feriado in feriados_estaduais_2024:
    if feriado not in feriados_nacionais_2024:
        print("Feriado Estadual:", feriado.strftime("%d/%m/%Y"))

# ======= Holidays =======

# ======= Pandas Market Calendars =======
calendario = mcal.get_calendar("BMF")
dias_negociacao_2024 = calendario.schedule(start_date="2024-01-01", end_date="2024-12-31")
print(dias_negociacao_2024)
#for dias in dias_negociacao_2024:
#    print(dias)
# ======= Pandas Market Calendars =======