from bs4 import BeautifulSoup as bs
import requests
import pymongo
import time
from splinter import Browser
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    browser = init_browser()

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(10)

    html = browser.html
    soup = bs(html, 'html.parser')

    #news title
    results = soup.find_all('div', class_='content_title')
    news_title = results[1].text
    #news p
    results = soup.find_all('div', class_='article_teaser_body')
    news_p = results[0].text
    #news date
    results = soup.find_all('div', class_='list_date')
    news_date = results[0].text
    #news img url
    results = soup.find_all('div',class_='list_image')
    news_img_relative_url = results[0].find('img')['src']
    base_url = "https://mars.nasa.gov/"
    news_img_complete_url = base_url+news_img_relative_url


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(10)

    html = browser.html
    soup = bs(html, 'html.parser')


    relative_featured_image_url = soup.find_all('article', class_='carousel_item')[0]['style'].split("url('")[1][:-3]
    base_url = "https://www.jpl.nasa.gov"
    featured_image_url = base_url + relative_featured_image_url

    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    df = df.rename(columns={0:"",1:"Mars"}).set_index("")
    df.to_html('table.html')


    url_list = ["https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",
                "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
                "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",
                "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"]

    hemisphere_image_urls=[]
    for url in url_list:
        response = requests.get(url)
        soup = bs(response.text,'html.parser')
        
        
        url_base = "https://astrogeology.usgs.gov/"

        relative_path = soup.find_all('img', class_='wide-image')[0]['src']

        img_url = url_base + relative_path
        title = soup.find_all('h2', class_='title')[0].text

        hemisphere_image_urls.append({"title":title,"img_url":img_url})


    scrape_data = {"news_title":news_title,
                   "news_p":news_p,
                   "news_date":news_date,
                   "news_img_complete_url":news_img_complete_url,
                   "featured_image_url":featured_image_url,
                   "hemisphere_image_urls":hemisphere_image_urls}
        
    browser.quit()

    
    return scrape_data