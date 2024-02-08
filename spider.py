import scrapy

# import CentcompscrapingItem class from "items.py" file
# .. indicates that CentcompscrapingItem is in the parent directory
from ..items import CentcompscrapingItem

# class was created by scrapy when we created the project from terminal
class SpiderSpider(scrapy.Spider):
    # name the spider & provide a URL for scraping (required by Spider class)
    name = "spider"
    start_urls = [
        'https://www.centralcomputer.com/all-products/computers/laptops/laptops.html?p=1'
    ]

    # link above is for page 1, we'll start the loop at page 2 and loop through other pages after
    page_number = 2

    # create a parse method, the URL above places the website's source code into the response variable
    def parse(self, response):

        # create an instance of the CentcompscrapingItem class from "items.py" file
        items = CentcompscrapingItem()

        # select all item cells from the website to extract values from each cell
        all_cells = response.css('li.item.product.product-item')

        # each cell has its own title + price + image + detail, loop over them
        for cell in all_cells:

            # for css selector, class="text" = . and id="text" = #
            # strip out unnecessary whitespaces
            # the extracted values will be in html and are convertered to text using ::text, store them in the variables
            title = [t.strip() for t in cell.css('a.product-item-link::text').extract()]
            price = cell.css('span.price::text').extract()
            image = cell.css('img.product-image-photo::attr(src)').extract()
            detail = cell.css('a.product-item-link::attr(href)').extract()

            # map fields from "items.py" (left) to variables created above (right)
            items['title'] = title
            items['price'] = price
            items['image'] = image
            items['detail'] = detail

            #similar to the return statement
            yield items

        # follow links using numerical pagination and get data for 5 pages
        # as long as page number is < 6 for every loop, process the parse method defined on top
        next_page = 'https://www.centralcomputer.com/all-products/computers/laptops/laptops.html?p=' + str(SpiderSpider.page_number)
        if SpiderSpider.page_number < 6:
            SpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

