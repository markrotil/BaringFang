from flask import Flask, render_template, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine(
    'postgres://qzewnmvp:KLrEMMwqNGoGYgkvTiI5pNANap7CuFbP@ziggy.db.elephantsql.com:5432/qzewnmvp', echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index1.html')


@app.route("/entertainment")
def entertainment():

    stocks = Base.classes.fang_stocks_2018_2020
    session = Session(engine)

    AMZN = session.query(stocks.Ticker, stocks.Adj_Close, stocks.Date).filter(
        stocks.Ticker == 'AMZN').order_by(stocks.Date).all()
    NFLX = session.query(stocks.Ticker, stocks.Adj_Close, stocks.Date).filter(
        stocks.Ticker == 'NFLX').order_by(stocks.Date).all()
    MSFT = session.query(stocks.Ticker, stocks.Adj_Close, stocks.Date).filter(
        stocks.Ticker == 'MSFT').order_by(stocks.Date).all()

    entertainment_stocks = {"entertainment_stocks": [
        {
            'Ticker': 'AMZN',
            'Date': [row[2] for row in AMZN],
            'Adj_Close': [row[1] for row in AMZN]
        },
        {
            'Ticker': 'NFLX',
            'Date': [row[2] for row in NFLX],
            'Adj_Close': [row[1] for row in NFLX]
        },
        {
            'Ticker': 'MSFT',
            'Date': [row[2] for row in MSFT],
            'Adj_Close': [row[1] for row in MSFT]
        }
    ]}
    session.close()
    return jsonify(entertainment_stocks)


if __name__ == "__main__":
    app.run()
