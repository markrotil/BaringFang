from flask import Flask, render_template, jsonify, request, redirect, url_for
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine(
    'postgres://qzewnmvp:KLrEMMwqNGoGYgkvTiI5pNANap7CuFbP@ziggy.db.elephantsql.com:5432/qzewnmvp', echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)

stocks = Base.classes.stocks
employees = Base.classes.employees
offices = Base.classes.offices


session = Session(engine)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("./index.html")


@app.route("/api/stocks")
def stockage():

    amazon_data = session.query(stocks.Date, stocks.Adj_Close, stocks.Ticker).filter(
        stocks.Ticker == 'AMZN').all()

    amazon_Date = []
    for item in amazon_data:
        amazon_Date.append(item[0])

    amazon_Close = []
    for item in amazon_data:
        amazon_Close.append(item[1])

    amazon_Ticker = []
    for item in amazon_data:
        amazon_Ticker.append(item[2])

    amazon_output = {"amazon_Date": amazon_Date,
                     "amazon_Close": amazon_Close,
                     "amazon_Volume": amazon_Ticker
                     }

    netflix_data = session.query(stocks.Date, stocks.Adj_Close, stocks.Ticker).filter(
        stocks.Ticker == 'NFLX').all()

    netflix_Date = []
    for item in netflix_data:
        netflix_Date.append(item[0])

    netflix_Close = []
    for item in netflix_data:
        netflix_Close.append(item[1])

    netflix_Ticker = []
    for item in netflix_data:
        netflix_Ticker.append(item[2])

    netflix_output = {"netflix_Date": netflix_Date,
                      "netflix_Close": netflix_Close,
                      "netflix_Volume": netflix_Ticker
                      }

    apple_data = session.query(stocks.Date, stocks.Adj_Close, stocks.Ticker).filter(
        stocks.Ticker == 'AAPL').all()

    apple_Date = []
    for item in apple_data:
        apple_Date.append(item[0])

    apple_Close = []
    for item in apple_data:
        apple_Close.append(item[1])

    apple_Ticker = []
    for item in apple_data:
        apple_Ticker.append(item[2])

    apple_output = {"apple_Date": apple_Date,
                    "apple_Close": apple_Close,
                    "apple_Volume": apple_Ticker
                    }

    facebook_data = session.query(stocks.Date, stocks.Adj_Close, stocks.Ticker).filter(
        stocks.Ticker == 'FB').all()

    facebook_Date = []
    for item in facebook_data:
        facebook_Date.append(item[0])

    facebook_Close = []
    for item in facebook_data:
        facebook_Close.append(item[1])

    facebook_Ticker = []
    for item in facebook_data:
        facebook_Ticker.append(item[2])

    facebook_output = {"facebook_Date": facebook_Date,
                       "facebook_Close": facebook_Close,
                       "facebook_Volume": facebook_Ticker
                       }

    google_data = session.query(stocks.Date, stocks.Adj_Close, stocks.Ticker).filter(
        stocks.Ticker == 'GOOG').all()

    google_Date = []
    for item in google_data:
        google_Date.append(item[0])

    google_Close = []
    for item in google_data:
        google_Close.append(item[1])

    google_Ticker = []
    for item in google_data:
        google_Ticker.append(item[2])

    google_output = {"google_Date": google_Date,
                     "google_Close": google_Close,
                     "google_Volume": google_Ticker
                     }

    microsoft_data = session.query(stocks.Date, stocks.Adj_Close, stocks.Ticker).filter(
        stocks.Ticker == 'MSFT').all()

    microsoft_Date = []
    for item in microsoft_data:
        microsoft_Date.append(item[0])

    microsoft_Close = []
    for item in microsoft_data:
        microsoft_Close.append(item[1])

    microsoft_Ticker = []
    for item in microsoft_data:
        microsoft_Ticker.append(item[2])

    microsoft_output = {"microsoft_Date": microsoft_Date,
                        "microsoft_Close": microsoft_Close,
                        "microsoft_Volume": microsoft_Ticker
                        }

    stocks_list = []
    stocks_list.extend((amazon_output, netflix_output,
                        apple_output, facebook_output, google_output, microsoft_output))
    return jsonify(stocks_list)


@app.route("/employees")
def employee_():

    employee = session.query(
        employees.Company, employees.Number_of_Employees, employees.Year).all()

    emp_list = []
    for row in employee:
        emp_dict = {"Company": row[0],
                    "Number_of_Employees": row[1],  "Year": row[2]}
        emp_list.append(emp_dict)
    session.close()
    return jsonify(emp_list)


@app.route("/office")
def location():

    offices_ = session.query(
        offices.Company, offices.Country, offices.Office,
        offices.Latitude, offices.Longitude).all()

    off_list = []
    for row in offices_:
        off_dict = {"Company": row[0], "Country": row[1], "Office": row[2], "Latitude": row[3],
                    "Longitude": row[4]}
        off_list.append(off_dict)
    session.close()
    return jsonify(off_list)


if __name__ == "__main__":
    app.run()
