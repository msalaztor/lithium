import yfinance as yf
import streamlit as st

st.write("""
# MS
Aqui se muestra el precio **De cierre** De LIT Global X Lithium & Battery Tech ETF
""")

#definir el ticker
tickerSymbol = 'LIT'
#obtener datos
tickerData = yf.Ticker(tickerSymbol)
#obtener precios historicos
tickerDf = tickerData.history(period='1d', start='2019-12-30', end='2023-6-30')


st.write("""
## Precio de cierre
""")
st.line_chart(tickerDf.Close)
