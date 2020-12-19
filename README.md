# web-scraping-challenge

## Mission to Mars

### Overview

The goal of this project was to build a flask web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

### Part 1 - Scraping

The initial scraping was complted using Pandas, BeautifulSoup, Requests/Splinter, and Jupyter Notebook.  This can be found in the Jupyter notebook file titled [mission_to_mars.ipynb](mission_to_mars.ipynp).

#### NASA News

Using splinter and Beautiful soup, the [NASA Mars News Site](https://mars.nasa.gov/news/) was scraped to collect the latest news headline and paragraph text.

#### JPL Mars Space Images - Featured Image

Splinter was used to navigate to the site for the [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

Using BeautifulSoup, the site was scraped to obtain the url string for the full-sized featured image.

#### Mars Facts

Again, splinter was used to navigate to the [Mars Facts webpage](https://space-facts.com/mars/).  The tables were scraped directly into a dataframe using pandas.  From there, the command 'to.html' was used to convert the dataframe into an HTML string.

#### Mars Hemispheres

The [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) was scraped to obtain high resolution images for each of Mars' hemispheres.

Using pandas, a for loop was used to and save the url for the full sized image for each hemisphere and save the results in a dictionary.

### Part 2 - MongoDB and Flask Application

Using MongoDB with Flask templating, a new HTML page was created that displays all of the information scraped in Part 1 of this project.

- The Jupyter notebook was converted into a Python script called [scrape_mars.py](scrape_mars.py) that contains a function called 'scrape' that executes all of the code from Part 1 and returns one Python dictionary containing all the data.

- Using a Flask application, called [mars_app.py](mars_app.py), the python file and scrape function were imported and the return was stored in Mongo.

-A template was created called [index.html](index.html) that calls the information from the flask dictionary and displays the data using Bootstrap elements. The final results are displayed as follows:

[Screenshot1](Screenshots/Mission_to_Mars_Screenshot.png)
[Screenshot2](Screenshots/Hemispheres_Screenshot.png)