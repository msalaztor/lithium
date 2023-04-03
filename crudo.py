import yfinance as yf
import streamlit as st

st.write("""
# Edukatiba
Aqui se muestra el precio **De cierre** Del Barril de Crudo!
""")

#definir el ticker
tickerSymbol = 'CL=F'
#obtener datos
tickerData = yf.Ticker(tickerSymbol)
#obtener precios historicos
tickerDf = tickerData.history(period='1d', start='2019-1-1', end='2023-4-3')


st.write("""
## Precio de cierre
""")
st.line_chart(tickerDf.Close)
