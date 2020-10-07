# My CS50 Final Project Phone Genie

[Phone genie](phone-genie.herokuapp.com/) is the web application that lets you find the right smartphone according to your price range (budget).
I build this app as part of my final project of [CS50](https://cs50.harvard.edu). 

## Making of Phone genie

There are two main parts of phone genie.
1. **The scraper:**
scraper.py is a python scraper made by using libraries like BeautifulSoup 4 and requests. 
It scrapes out useful phone information and stores in the database.
2. **The flask web application:** In the web application, first you have to choose the price or the budget of your phone. 
By that price, phone genie generates some phones with their discription and rating using a progress bar. 
The information contains RAM, ROM, Battery, Processor etc. 
Currently, Only Indian price range and phone are shown.Users can also buy that phone using buy link. 
Currently only amazon is supported.

#### This application was made my using:
* Flask
* Jquery
* Bootstrap

---

**Website:** [phone-genie.herokuapp.com](phone-genie.herokuapp.com)
