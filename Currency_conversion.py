import requests, json, locale

def currency_conversion():
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    currency_quotes = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    currency_quotes = currency_quotes.json()
    dolar = locale.currency(float(currency_quotes['USD']['bid']), grouping=True)
    euro = locale.currency(float(currency_quotes['EUR']['bid']), grouping=True)
    bitcoin = float(currency_quotes['BTC']['bid'])

    return f'Dolar: {dolar} - Euro: {euro} - Bitcoin: R$ {bitcoin}'
    