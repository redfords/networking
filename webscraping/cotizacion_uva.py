from turtle import reset
import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import os
import sys

def scrap(fecha_desde, fecha_hasta):
    url = 'http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables_datos.asp'
    try:
        data = {'fecha_desde': fecha_desde, 'fecha_hasta': fecha_hasta, 'B1': 'Enviar', 'primeravez': 1, 'serie': 7913}
        resp = requests.post(url=url, data=data)
        soup = BeautifulSoup(resp.text, "html.parser")

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    filas = soup.find_all('td')
    return filas

def parsear(filas):
    mensual = pd.DataFrame()
    for i in range(0, int(len(list(filas)) / 2)):
        dic = dict()
        dic['fecha'] = filas[2 * i].text.strip()
        dic['valor'] = filas[2 * i + 1].text.strip()

        rueda = pd.DataFrame.from_dict(dic, orient='index').transpose().set_index('fecha')
        rueda.index = pd.to_datetime(rueda.index, format='%d/%m/%Y')
        mensual = pd.concat([mensual, rueda], axis=0)
    return mensual

def monthdelta(date, delta):
    m, y = (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12
    if not m: m = 12
    d = min(date.day, [31,
                       29 if y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0) else 28,
                       31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date.replace(day=d, month=m, year=y)

def periodo_descarga(fecha_desde, fecha_hasta, path, year, month, day):
    tabla_anual = pd.DataFrame()
    filas = scrap(fecha_desde, fecha_hasta)
    tabla = parsear(filas)
    tabla_anual = pd.concat([tabla_anual, tabla], axis=0)

    fullPath = path + '/' + str(year) + '/' + str(month)
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)

    archivo = 'bcra_cotizacion_uva_' + str(year) + str(month) + str(day) + '.txt.gz'
    tabla_anual.to_csv(fullPath + '/' + archivo, sep='|')

FechaDesde = monthdelta(datetime.datetime.now(), -6)
FechaHasta = datetime.datetime.now()
path = str(sys.argv[1])
fecha = datetime.date.today()
year = fecha.year
month = '{:02d}'.format(fecha.month)
day = '{:02d}'.format(fecha.day)

periodo_descarga(FechaDesde.strftime('%Y-%m-%d'), FechaHasta.strftime('%Y-%m-%d'), path, year, month, day)