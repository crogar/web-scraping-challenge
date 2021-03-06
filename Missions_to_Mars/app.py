from re import template
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_mars")  # Creating a db named mission_mars if it doesn't exist already


# Set route to render index.html
@app.route('/')
def index():
    # Find one record of data from the mongo database
    mars_data = mongo.db.mars_data.find_one()   # since we are only using one Document in the MongoDb, well use find_one() method
    # Return template and data
    return render_template("index.html", mars_mission=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    mongo.db.mars_data.update({}, mars_data, upsert=True)
    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)