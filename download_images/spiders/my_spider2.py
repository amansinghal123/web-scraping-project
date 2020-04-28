import scrapy
from ..items import DownloadImagesItem

class celebrity_spider(scrapy.Spider):

    name = 'my_spider2'
    start_urls = [
        'https://www.imdb.com/list/ls068010962/',
        'https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=2'
    ]

    def parse_dir_contents2(self, response):
        items = DownloadImagesItem()
        url = response.css("img.poster").xpath("@src").extract_first()
        items['image_urls'] = [url]
        yield items

    def parse_dir_contents1(self, response):
        url = response.urljoin(response.css("span.see-more.inline.nobr-only a").xpath("@href").extract_first())
        yield scrapy.Request(url, callback=self.parse_dir_contents2)

    def parse(self, response):

        href_list = response.css("div.lister-item-image a").xpath("@href").extract()
        for i in range(100):
            url = response.urljoin(href_list[i])
            yield scrapy.Request(url, callback=self.parse_dir_contents1)