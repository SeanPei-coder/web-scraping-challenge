from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    news_title=mongo.db.collection.find_one({},{ "news_title":1, "_id":0})['news_title']
    
    news_p = mongo.db.collection.find_one({},{ "news_p":1, "_id":0})['news_p']

    news_date = mongo.db.collection.find_one({},{"news_date":1,"_id":0})['news_date']

    news_img_complete_url = mongo.db.collection.find_one({},{ "news_img_complete_url":1, "_id":0})['news_img_complete_url']

    featured_image_url = mongo.db.collection.find_one({},{ "featured_image_url":1, "_id":0})['featured_image_url']

    return render_template("index.html" , news_title = news_title, 
                                          news_p = news_p,
                                          news_date=news_date,
                                          news_img_complete_url=news_img_complete_url,
                                          featured_image_url=featured_image_url,
                                        )


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():


    scrape_data = scrape_mars.scrape()

    mongo.db.collection.update({},scrape_data, upsert=True)
    # Redirect back to home page
    return redirect("/")

#Route to render image_and_table.html
@app.route("/image_and_table")
def page():
    featured_image_url = mongo.db.collection.find_one({},{ "featured_image_url":1, "_id":0})['featured_image_url']

    return render_template("image_and_table.html" , featured_image_url=featured_image_url)


@app.route("/mars_hemispheres")
def web():
    hemisphere_image_url_1 = mongo.db.collection.find_one({},{ "hemisphere_image_urls":1, "_id":0})['hemisphere_image_urls'][0]['img_url']
    hemisphere_image_title_1 = mongo.db.collection.find_one({},{ "hemisphere_image_urls":1, "_id":0})['hemisphere_image_urls'][0]['title']

    hemisphere_image_url_2 = mongo.db.collection.find_one({},{ "hemisphere_image_urls":1, "_id":0})['hemisphere_image_urls'][1]['img_url']
    hemisphere_image_title_2 = mongo.db.collection.find_one({},{ "hemisphere_image_urls":1, "_id":0})['hemisphere_image_urls'][1]['title']

    hemisphere_image_url_3 = mongo.db.collection.find_one({},{ "hemisphere_image_urls":1, "_id":0})['hemisphere_image_urls'][2]['img_url']
    hemisphere_image_title_3 = mongo.db.collection.find_one({},{ "hemisphere_image_urls":1, "_id":0})['hemisphere_image_urls'][2]['title']

    hemisphere_image_url_4 = mongo.db.collection.find_one({},{ "hemisphere_image_urls":1, "_id":0})['hemisphere_image_urls'][3]['img_url']
    hemisphere_image_title_4 = mongo.db.collection.find_one({},{ "hemisphere_image_urls":1, "_id":0})['hemisphere_image_urls'][3]['title']


    return render_template("mars_hemispheres.html" ,hemisphere_image_url_1=hemisphere_image_url_1,
                                                    hemisphere_image_title_1=hemisphere_image_title_1,
                                                    hemisphere_image_url_2=hemisphere_image_url_2,
                                                    hemisphere_image_title_2=hemisphere_image_title_2,
                                                    hemisphere_image_url_3=hemisphere_image_url_3,
                                                    hemisphere_image_title_3=hemisphere_image_title_3,
                                                    hemisphere_image_url_4=hemisphere_image_url_4,
                                                    hemisphere_image_title_4=hemisphere_image_title_4)


if __name__ == "__main__":
    app.run(debug=True)
