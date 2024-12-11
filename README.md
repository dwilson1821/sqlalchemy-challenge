# SQLAlchemy Challenge: Climate Analysis and Exploration  

## Background  

You've decided to plan a long holiday in **Honolulu, Hawaii**, and part of your preparation includes conducting a climate analysis of the area. Using Python, SQLAlchemy, Flask, Pandas, and Matplotlib, you'll analyze historical weather data from a SQLite database and build a Flask API to make the results accessible.

---

## Repository Structure  

The repository is organized as follows:  

```  
sqlalchemy-challenge/  
│  
├── SurfsUp/  
│   ├── Resources/                 # Folder containing data files  
│   │   └── hawaii.sqlite          # SQLite database with climate data  
│   │  
│   ├── climate_starter.ipynb      # Jupyter Notebook for climate analysis and exploration  
│   ├── app.py                     # Flask application to serve API endpoints  
│   ├── README.md                  # This README file  
│   ├── requirements.txt           # Python dependencies  
│  
└── .gitignore                     # File to exclude unnecessary files  
```  

---

## Objectives  

This project is divided into two main parts:  

### Part 1: Analyze and Explore the Climate Data  

1. **Connect to the Database**  
   - Use SQLAlchemy's `create_engine()` to connect to the `hawaii.sqlite` database.  
   - Reflect the database tables using `automap_base()` to access the `station` and `measurement` tables.  
   - Establish a SQLAlchemy session and remember to close it at the end.  

2. **Precipitation Analysis**  
   - Query the most recent date in the dataset.  
   - Retrieve the last 12 months of precipitation data (`date` and `prcp`) based on the most recent date.  
   - Load the query results into a Pandas DataFrame and sort them by date.  
   - Plot the results as a time series chart.  
   - Generate summary statistics for the precipitation data using Pandas.  

3. **Station Analysis**  
   - Design a query to calculate the total number of stations in the dataset.  
   - Identify the most-active stations by querying station activity counts in descending order.  
   - For the most-active station:  
     - Calculate the minimum, maximum, and average temperature.  
     - Retrieve the last 12 months of temperature observation data (`TOBS`) and plot a histogram with 12 bins.  

4. **Close Your Session**  
   - Ensure you close your SQLAlchemy session after completing all analysis.  

---

### Part 2: Design Your Climate App  

Use Flask to create a RESTful API based on the results from Part 1. Your application should provide the following routes:  

| Route | Description |  
|-------|-------------|  
| `/` | Homepage that lists all available routes. |  
| `/api/v1.0/precipitation` | Returns a JSON dictionary of precipitation data for the last 12 months, where the date is the key and `prcp` is the value. |  
| `/api/v1.0/stations` | Returns a JSON list of all stations in the dataset. |  
| `/api/v1.0/tobs` | Returns a JSON list of temperature observations (TOBS) for the last 12 months from the most-active station. |  
| `/api/v1.0/<start>` | Returns the minimum, average, and maximum temperatures for all dates from the given start date onward (inclusive). |  
| `/api/v1.0/<start>/<end>` | Returns the minimum, average, and maximum temperatures for the date range between the start and end dates (inclusive). |  

---

## Setup Instructions  

### Prerequisites  

1. **Install Python 3.x**  
2. Install required Python packages using the `requirements.txt` file:  
   ```bash  
   pip install -r requirements.txt  
   ```  

### Step 1: Clone the Repository  
```bash  
git clone https://github.com/your-username/sqlalchemy-challenge.git  
cd sqlalchemy-challenge/SurfsUp  
```  

### Step 2: Run the Climate Analysis  
1. Open the Jupyter Notebook `climate_starter.ipynb` to analyze and explore the climate data.  
2. Follow the steps outlined in the notebook to generate plots and summary statistics.  

### Step 3: Launch the Flask Application  
1. Navigate to the directory containing `app.py`.  
2. Run the Flask application:  
   ```bash  
   python app.py  
   ```  
3. Open a browser and navigate to `http://127.0.0.1:5000/` to access the API.  

---

## Example Output  

### 1. Precipitation Plot  
A time series plot of precipitation for the last 12 months:  

![Precipitation Plot](path/to/precipitation_plot.png)  

### 2. Temperature Histogram  
A histogram of temperature observations for the most-active station:  

![Temperature Histogram](path/to/temperature_histogram.png)  

### 3. Flask API Output  
Example JSON response from `/api/v1.0/precipitation`:  
```json  
{  
  "2016-08-23": 0.0,  
  "2016-08-24": 0.08,  
  "2016-08-25": 0.15,  
  "2016-08-26": 0.0,  
  "2016-08-27": 0.05  
}  
```  

---

## Key Findings  

- **Most-Active Station**: The station with ID `XXXXXX` recorded the highest number of observations.  
- **Precipitation Trends**: Rainfall was most prominent in [specific months], with an average precipitation of X inches.  
- **Temperature Analysis**: The average temperature for the most-active station during the last 12 months was X°F.  
