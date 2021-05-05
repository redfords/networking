from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

""" Request for a JSON expressed as a dictionary of nested lists with price, market cap and total
volumes, which contain the unix timestamp and price at that time
"""

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'usd', days = 30)
bitcoin_price_data = bitcoin_data['prices']

data = pd.DataFrame(bitcoin_price_data, columns = ['TimeStamp', 'Price'])
data['Date'] = pd.to_datetime(data['TimeStamp'], unit = 'ms')
print(data)

candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})
print(candlestick_data)

fig = go.Figure(data = [go.Candlestick(x = candlestick_data.index,
open = candlestick_data['Price']['first'],
high = candlestick_data['Price']['max'],
low = candlestick_data['Price']['min'],
close = candlestick_data['Price']['last'])
])

fig.update_layout(xaxis_rangeslider_visible = False, xaxis_title = 'Date',
yaxis_title = 'Price (USD $)', title = 'Bitcoin Candlestick Chart Over Past 30 Days')

# plot(fig, filename = 'bitcoin_candlestick_graph.html')