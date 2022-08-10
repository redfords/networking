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

    filas = soup.find_all('td')
    use_filas = [filas for filas in filas[4:]]

    return use_filas

def get_month(date, delta):
    m = (date.month + delta) % 12
    y = date.year + ((date.month) + delta - 1) // 12
    if not m: m = 12
    d = min(date.day, [31,
                       29 if y % 4])
