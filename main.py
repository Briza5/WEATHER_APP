# Import Flask class and render_template function from flask import Flask, render_template
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)  # Instantiate the Flask application to the variable app

# Read the stations data into a DataFrame
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")  # Define the route for the home URL
def home():  # Define the home function
    # Use render_template to render the HTML file
    return render_template("home.html", data=stations.to_html())


# Define the route for the API with dynamic parameters station and date
@app.route("/api/v1/<station>/<date>")
def about(station, date):  # define the about function with parameters station and date
    # Construct the filename based on station parameter
    filename = "data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # Extract temperature for the given date
    temperature_extract = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    if not temperature_extract.empty:
        temperature = float(temperature_extract)
    else:
        temperature = None
    return {"station": station,
            "date": date,
            # return a JSON response with station, date, and temperature
            "temperature": temperature}


if __name__ == "__main__":  # Check if the script is run directly and not imported as a module
    app.run(debug=True)  # Run the Flask application in debug mode
