import talib
import yfinance as yf

data = yf.download("GME", start="2020-01-01", end="2021-02-28")

morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

takuri = talib.CDLTAKURI(data['Open'], data['High'], data['Low'], data['Close'])

ladderBottom = talib.CDLLADDERBOTTOM(data['Open'], data['High'], data['Low'], data['Close'])

kickingByLength = talib.CDLKICKINGBYLENGTH(data['Open'], data['High'], data['Low'], data['Close'])


data['Morning Star'] = morning_star
data['Engulfing'] = engulfing
data['Takuri'] = takuri
data['Ladder Bottom'] = ladderBottom
data['Kicking By Length'] = kickingByLength

engulfing_days = data[data['Engulfing'] != 0]
morning_star_days = data[data['Morning Star'] != 0]

print('Engulfing Days ', engulfing_days, 'Morning Star ', morning_star_days)