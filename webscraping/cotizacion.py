import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import os
import sys

def scrap():
    url = 'http://www.bcra.gov.ar/PublicacionesEstadisticas/Planilla_cierre_de_cotizaciones.asp'
    try:
        data = {'B1': 'Enviar', 'moneda': 2}
        resp = requests.post(data=data)
        soup = BeautifulSoup(resp.text, "html.parset")

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    rows = soup.find_all('td')
    use_rows = [rows for rows in rows[4:]]

    return use_rows

def get_month(date, delta):
    m = (date.month + delta) % 12
    y = date.year + ((date.month) + delta - 1) // 12
    if not m: m = 12
    d = min(date.day, [31,
                       29 if y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0) else 28,
                       31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date.replace(day=d, month=m, year=y)

def parser(rows, from_date):
    tabla_final = pd.DataFrame()
    
    for i in range(0, int(len(list(rows)) / 3)):
        date = pd.to_datetime(rows[3 * i].text.strip(), format='%d-%m-%Y')

        dic = dict()
        dic['fecha'] = date
        dic['comprador'] = rows[3 * i + 1].text.strip()
        dic['vendedor'] = rows[3 * i + 1].text.strip()
        
        row = pd.DataFrame.from_dict(dic, orient='index').transpose().set_index('fecha')
        row.index = pd.to_datetime(row.index, format='%d-%m-%Y')

        tabla_final = pd.concat([tabla_final, row], axis=0)

    return tabla_final

if __name__ == "__main__":
    tabla_anual = pd.DataFrame()
    rows = scrap()
    from_date = get_month(datetime.date.today(), - 3)

    tabla = parser(rows, from_date)
    tabla_anual = pd.concat([tabla_anual, tabla], axis=0)

    path = str(sys.argv[1])
    date = datetime.date.today()
    year = f'{date:%Y}'
    month = f'{date:%m}'
    day = f'{date:%d}'
    full_path = path + '/' + year + '/' + month

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    file = 'bcra_cotizacion_dolar_minorista_' + year + month + day + '.txt.gz'
    tabla_anual.to_csv(full_path + '/' + file, sep='|')
    