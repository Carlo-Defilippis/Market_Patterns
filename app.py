import os, csv
import talib
import yfinance as yf
import pandas
from flask import Flask, escape, request, render_template, send_from_directory, jsonify
from patterns import candlestick_patterns

app = Flask(__name__, static_url_path='/')


# @app.route('/data')
# def get_data():
#     df = pandas.read_csv('datasets/daily/{}'.format(filename))
#     pattern  = request.args.get('pattern', False)
#     pattern_function = getattr(talib, pattern)
#     results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
#     if pattern:
#         for filename in os.listdir('datasets/daily'):
#             df = pandas.read_csv('datasets/daily/{}'.format(filename))
#             pattern_function = getattr(talib, pattern)
#             results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
#             if results:
#                 return jsonify(results)
#     return jsonify(pattern_function)

@app.route('/snapshot')
def snapshot():
    with open('datasets/symbols.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            data = yf.download(symbol, start="2020-01-01", end="2020-08-01")
            data.to_csv('datasets/daily/{}.csv'.format(symbol))

    return {
        "code": "success"
    }

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    pattern  = request.args.get('pattern', False)
    stocks = {}
    foundStocks = 0

    with open('datasets/symbols.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}

    if pattern:
        for filename in os.listdir('datasets/daily'):
            df = pandas.read_csv('datasets/daily/{}'.format(filename))
            pattern_function = getattr(talib, pattern)
            symbol = filename.split('.')[0]

            try:
                results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                last = results.tail(1).values[0]

                if last > 0:
                    stocks[symbol][pattern] = 'bullish'
                elif last < 0:
                    stocks[symbol][pattern] = 'bearish'
                else:
                    stocks[symbol][pattern] = None
                    foundStocks += 1
            except Exception as e:
                print('failed on filename: ', filename)

    return render_template('index.html', candlestick_patterns=candlestick_patterns, stocks=stocks, pattern=pattern, foundStocks=foundStocks)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)
