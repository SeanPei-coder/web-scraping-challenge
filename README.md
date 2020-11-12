# web-scraping-challenge

## Intro

In this activity, I built a web application that scraped various websites for data related to the Mission to Mars and displays the information in multi HTML pages. The following outlines what I did.

## Step 1 - Scraping

I was using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

- Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of the scraping and analysis tasks. The following outlines what I scraped.

### NASA Mars News

Scrape the [NASA Mars News Site ](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collect the latest News Title and Paragraph Text. Assign the text to variables that I can reference later.

### JPL Mars Space Images - Featured Image

- Visit the url for JPL Featured Space Image [here.](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
- Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
- Make sure to find the image url to the full size .jpg image.
- Make sure to save a complete url string for this image.

### Mars Facts

- Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
- Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

- Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

- Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

- Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create HTML pages that displays all of the information that was scraped from the URLs above.

![alt text](https://github.com/SeanPei-coder/web-scraping-challenge/blob/main/Missions_to_Mars/images/Latest%20News.png)

![alt text](https://github.com/SeanPei-coder/web-scraping-challenge/blob/main/Missions_to_Mars/images/Featured%20Image.png)

![alt text](https://github.com/SeanPei-coder/web-scraping-challenge/blob/main/Missions_to_Mars/images/Mars%20Table.png)

![alt text](https://github.com/SeanPei-coder/web-scraping-challenge/blob/main/Missions_to_Mars/images/Mars%20Hemispheres.png)
