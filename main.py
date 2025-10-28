from flask import Flask, render_template # Import Flask class and render_template function from flask import Flask, render_template

app = Flask("Website") # Instantiate the Flask application to the variable app

@app.route("/home") # Define the route for the home URL
def home(): # Define the home function
    return render_template("tutorial.html") # Use render_template to render the HTML file

@app.route("/about/") # Define the route for the about URL
def about(): # Define the about function
    return render_template("about.html") # Use render_template to render the HTML file


app.run(debug=True) # Run the Flask application in debug mode