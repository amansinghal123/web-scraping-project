import scrapy
from ..items import CelebrityItem
import glob
import os


ctr = -1
def get_image(img_dir):
    global ctr
    ctr += 1
    data_path = os.path.join(img_dir, '*g')
    files = glob.glob(data_path)
    data = []
    for f1 in files:
        with open(f1, "rb") as imageFile:
            data.append(imageFile.read())
    return data[ctr]

class celebrity_spider(scrapy.Spider):

    name = 'my_spider'
    start_urls = [
        'https://www.imdb.com/list/ls068010962/',
        'https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=2'
    ]

    def parse_dir_contents2(self, response):
        a = response.css("div.soda.odd p::text").extract()
        a = " ".join(a)[12:]

        items = CelebrityItem()
        items['name'] = response.css(".parent a::text").extract_first()
        items['bio'] = a
        items['urls'] = response.css("img.poster").xpath("@src").extract_first()
        items['img'] = get_image("C:/Users/DELL/Desktop/bipoar2/images/full")
        items['counter'] = ctr
        yield items


    def parse_dir_contents1(self, response):
        url = response.urljoin(response.css("span.see-more.inline.nobr-only a").xpath("@href").extract_first())
        yield scrapy.Request(url, callback=self.parse_dir_contents2)


    def parse(self, response):
        href_list = response.css("div.lister-item-image a").xpath("@href").extract()
        for i in range(100):
            url = response.urljoin(href_list[i])
            yield scrapy.Request(url, callback=self.parse_dir_contents1)
