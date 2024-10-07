# Import the dependencies.

import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect = True)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
   session = Session(engine)
   previous_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= previous_year).all()
   session.close()
   precip = {date: prcp for date, prcp in data}
   return jsonify(precipitation=precip)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    data_s = session.query(Station.station).all()
    session.close()
    stations = list(np.ravel(data_s))
    return jsonify(stations=stations)


@app.route("/api/v1.0/tobs")
def tobs():
   session = Session(engine)
   previous_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   data_t = session.query(Measurement.tobs).\
   filter(Measurement.station == 'USC00519281').\
   filter(Measurement.date >= previous_year).all()
   temperature = list(np.ravel(data_t))
   return jsonify(temperature=temperature)
   

#Used Xpert Learning Assistant

@app.route("/api/v1.0/<start>")
def start(start=None):
   session = Session(engine)
   data_st = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
   filter(Measurement.date <= start).all()
   temperatures = list(np.ravel(data_st))
   session.close()
   return jsonify(temperatures=temperatures)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None, end=None):
   session = Session(engine)
   data_se = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
   filter(Measurement.date >= start).\
   filter(Measurement.date <= end).all()
   temperatures = list(np.ravel(data_se))
   session.close()
   return jsonify(temperatures=temperatures)


if __name__ == '__main__':
    app.run(debug=True)