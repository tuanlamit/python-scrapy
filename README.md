# Python Amazon Scraping With Scrapy

This project was created and executed on Windows.

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
1) install selector gadget for chrome
2) Set logs level to display output for only warnings from terminal:

   ```scrapy crawl spider -L WARNING```

> [!NOTE]
>
> For css selector:
> 
> ```response.css('title::text')[0].extract()```
>
> is similar to:
>
> ```response.css('title::text').extract_first()```
>
> but extract_first() is usually preferred so there will be no error if result is empty

> [!NOTE]
> 
> To extract href=/page/2/, combine css and xpath to make it simpler:
>
> `response.css("li.next a").xpath("@href").extract()`
> 
> to extract all href:
>
> `response.css("a").xpath("@href").extract()`

Working Directory & Result:

![wd](https://github.com/tuanlamit/python-scrapy/assets/128099142/a56e08b0-4089-49a6-8993-af961b1b03b2)

![js](https://github.com/tuanlamit/python-scrapy/assets/128099142/80e91799-6395-416f-bf1e-3ce1ec31f675)

![db](https://github.com/tuanlamit/python-scrapy/assets/128099142/54c00278-3705-4306-932a-a86d543f4589)


