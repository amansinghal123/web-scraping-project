# bipolar-factory-project
scraping a website to get information about Indian celebrities using python and scrapy

I used:
- Pycharm as the IDE
- scrapy as the scraping library
- MongoDB as the databse
- pyMongo as the Database manging library
The images in the database are in base64 form. Please decode it to view the image

I scraped the IMDb top 200 indian celebrities website
and got the data of all the celebrities mentioned there with there images
but I wasn't able to order the images properly. The images are actually jumbled up. 
I am very sorry for this mess but its because I wasnt very familiar with database management.
Scrapy I had used a little bit ealrier so I had to learn both scrapy and how to create a databse
in a short amount of time.
I tried to resolve the jumbled images issue but I wasnt able to. As the deadline was aproaching
so I decided to upload it.

There are 2 spiders.
1) For scraping the website for the data and loading the data with the images into the database
2) For scraping the and downloading the images

But as these are two different spider I couldnt synchronise them properly leading to the jumbled images.
