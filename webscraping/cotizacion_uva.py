from turtle import reset
import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import os
import sys

def scrap(from_date, to_date):
    url = 'http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables_datos.asp'
    try:
        data = {'fecha_desde': from_date, 'fecha_hasta': to_date, 'B1': 'Enviar', 'primeravez': 1, 'serie': 7913}
        resp = requests.post(url=url, data=data)
        soup = BeautifulSoup(resp.text, "html.parser")

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    rows = soup.find_all('td')
    return rows

def parsear(rows):
    mensual = pd.DataFrame()
    for i in range(0, int(len(list(rows)) / 2)):
        dic = dict()
        dic['fecha'] = rows[2 * i].text.strip()
        dic['valor'] = rows[2 * i + 1].text.strip()

        rueda = pd.DataFrame.from_dict(dic, orient='index').transpose().set_index('fecha')
        rueda.index = pd.to_datetime(rueda.index, format='%d/%m/%Y')
        mensual = pd.concat([mensual, rueda], axis=0)
    return mensual

def get_month(date, delta):
    m, y = (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12
    if not m: m = 12
    d = min(date.day, [31,
                       29 if y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0) else 28,
                       31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date.replace(day=d, month=m, year=y)

def periodo_descarga(from_date, to_date, path, date):
    tabla_anual = pd.DataFrame()
    rows = scrap(from_date, to_date)
    tabla = parsear(rows)
    tabla_anual = pd.concat([tabla_anual, tabla], axis=0)

    year = f'{date:%Y}'
    month = f'{date:%m}'
    day = f'{date:%d}'

    full_path = path + '/' + year + '/' + month
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    file = 'bcra_cotizacion_uva_' + year + month + day + '.txt.gz'
    tabla_anual.to_csv(full_path + '/' + file, sep='|')

from_date = get_month(datetime.datetime.now(), -6)
to_date = datetime.datetime.now()
path = str(sys.argv[1])
date = datetime.date.today()

periodo_descarga(from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'), path, date)