# Import Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
from config import executable_path
from splinter import Browser

def init_browser():
    return Browser("chrome", executable_path, headless=False)

def scrape():
    browser = init_browser()

    ## Nasa Mars News ##

    # URL of page to be scraped
    url="https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #Retrieve latest news article and paragraph
    mars_news_title = soup.find_all('div', class_="content_title")[1].text
    mars_news_p = soup.find_all('div', class_="article_teaser_body")[0].text

    ## JPL Mars Space Images - Featured Image ##
   
    # URL to be scraped for mars image
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    html = browser.html
    soup_jpl = BeautifulSoup(html, "html.parser")
    # Search for featured image url link
    image_url= soup_jpl.find_all('article', class_="carousel_item")[0]['style'].split("('", 1)[1].split("')")[0]
    base_url = "https://jpl.nasa.gov"
    featured_image_url = base_url + image_url

