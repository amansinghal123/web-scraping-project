# web scraping project
scraping a website to get information about Indian celebrities using python and scrapy

I used:

Pycharm as the IDE
scrapy as the scraping library
MongoDB as the databse
pyMongo as the Database manging library The images in the database are in base64 form. Please decode it to view the image

I scraped the IMDb top 200 indian celebrities website and got the data of all the celebrities mentioned there with there images but I wasn't able to order the images properly. The images are actually jumbled up. I am very sorry for this mess but its because I wasnt very familiar with database management.

There are 2 spiders.

1) my_spider: For scraping the website for the data and loading the data with the images into the database
2) my_spider2: For scraping the and downloading the images

But as these are two different spider I couldnt synchronise them properly leading to the jumbled images.

- you will need a pymongo compass to store the data from above
- you will ne to change path in settings.py of both the spiders
- please use pycharm for ease of use

steps for making my project work:
1) open pycharm 
2) new project
this should create the venv(virtual envirnment)
3) install scrapy from project entrepreneur
4) terminal -> scrapy startproject celebrity
5) terminal -> scrapy startproject download_images
6) add my_spider in celebrity->celebrity->spiders
7) add my_spider2 in download_images->download_images->spiders
8) replace all the files by the files i provided according to structure
9) change the path in settings.py of my_spider2 (where to store images)
9) terminal -> scrapy crawl my_spider
10) terminal -> scrapy crawl my_spider2
