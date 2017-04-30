import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import pandas as pd


plotly.tools.set_credentials_file(username='hoslack', api_key='eCkxdXMEJWIchIA2HmQq')


df = pd.read_csv('timeseries1.csv')
df.head()

trace1 = go.Scatter(
                    x=df['time_read'], y=df['temperature'],
                    mode='lines', name='logx'
                   )
fig = go.Figure(data=[trace1])

py.plot(fig, filename='simple-plot-from-csv')
