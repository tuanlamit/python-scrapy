import scrapy
from ..items import CentcompscrapingItem

class SpiderSpider(scrapy.Spider):
    # name the spider & provide a URL for scraping (required by Spider class)
    name = "spider"
    page_number = 2
    start_urls = [
        'https://www.centralcomputer.com/all-products/computers/laptops/laptops.html?p=1'
    ]

    # create a parse method, the URL above places the website's source code into the response variable
    def parse(self, response):

        # create an instance of the CentcompscrapingItem class from "items.py" file
        items = CentcompscrapingItem()

        # select all div boxes to extract values from each box
        all_cells = response.css('li.item.product.product-item')

        # loop over each div box, which has its own title + price + image
        for cell in all_cells:

            # for css selector, class="text" = . and id="text" = #
            # strip out unnecessary whitespaces
            title = [t.strip() for t in cell.css('a.product-item-link::text').extract()]
            price = cell.css('span.price::text').extract()
            image = cell.css('img.product-image-photo::attr(src)').extract()
            detail = cell.css('a.product-item-link::attr(href)').extract()

            # map fields from "items.py" to variables created above
            items['title'] = title
            items['price'] = price
            items['image'] = image
            items['detail'] = detail
            yield items

        # follow links using numerical pagination
        # just get data for 5 pages
        next_page = 'https://www.centralcomputer.com/all-products/computers/laptops/laptops.html?p=' + str(SpiderSpider.page_number)
        if SpiderSpider.page_number < 6:
            SpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

        
        
