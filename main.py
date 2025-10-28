from flask import Flask, render_template # Import Flask class and render_template function from flask import Flask, render_template

app = Flask("Website") # Instantiate the Flask application to the variable app

@app.route("/") # Define the route for the home URL
def home(): # Define the home function
    return render_template("home.html") # Use render_template to render the HTML file

@app.route("/api/v1/<station>/<date>") # Define the route for the API with dynamic parameters station and date
def about(station, date): # define the about function with parameters station and date
    temperature = 23    # Example temperature value
    return {"station": station,
            "date": date,
            "temperature": temperature}  # return a JSON response with station, date, and temperature


app.run(debug=True) # Run the Flask application in debug mode