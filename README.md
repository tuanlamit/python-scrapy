# Python Amazon Scraping With Scrapy

Steps taken: (the step numbers are just there to provide the steps and don't have to be completed in order)

1) create an empty folder and cd into it 
2) create venv "python -m venv venv" from terminal
3) activate venv ".\venv\Scripts\activate" from terminal
4) upgrade pip "python.exe -m pip install --upgrade pip" from terminal
5) install scrapy "pip install scrapy" from terminal
6) create the project folder name "scrapy startproject centcompscraping" from terminal
7) cd into "centcompscraping" folder
8) create spider.py "scrapy genspider spider centralcomputer.com" from terminal
9) Folder and files to pay attention to:
- "spiders" folder: our spider.py created earlier is located here
- "items.py": temporarily stores extracted data (automatically created by scrapy, we need to create items here)
- "pipelines.py" specifies where to store extracted data (automatically created by scrapy, add database info here if exporting extracted data to a database)
- "middlewares.py" does something with the returned data or send other stuff along with the request (automatically created by scrapy, needs modification)
- "settings.py" this is where we uncomment pipeline or add user agents/proxies (automatically created by scrapy, needs modification)
10) import the class from "items.py" into "spider.py"
11) start coding in the required .py files
12) start crawling "scrapy crawl spider" from terminal
13) if it doesn't work, test it in scrapy shell by entering "scrapy shell" from terminal, fetch the website and check for error codes, ex: response.css('a.product-item-link::text').extract()
14) try crawling again "scrapy crawl spider" from terminal then extract to .json file
15) uncomment ITEM_PIPELINES in "settings.py, the default number 300 in ITEM_PIPELINES is the priority, lower number = higher priority
16) enter "pip install mysql-connector-python" from terminal 
17) download and set up a local MySQL database then create a schema
18) in "pipeline.py", import mysql.connector (if not using mysql, you could use the built-in sqlite3)
19) then in "pipeline.py", define methods to manipulate the database using SQL statements
20) entering "scrapy crawl spider -o laptops.json" from the terminal, and data will both be exported as a .json file + imported into MySQL

Optional:
install selector gadget for chrome



