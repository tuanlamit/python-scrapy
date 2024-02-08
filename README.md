# Python Amazon Scraping With Scrapy

This project was created and executed on Windows.

Steps taken: (the step numbers are just there to provide the steps and don't have to be completed in order)

1) create an empty folder and cd into it
2) create venv "python -m venv venv" from terminal
3) activate venv ".\venv\Scripts\activate" from terminal
4) upgrade pip "python.exe -m pip install --upgrade pip" from terminal
5) install scrapy "pip install scrapy" from terminal
6) create the project folder name "scrapy startproject centcompscraping" from terminal:
   - cd into "centcompscraping" folder
   - create spider.py "scrapy genspider spider centralcomputer.com" from terminal

Additional steps if exporting extracted data into a local MySQL database:
1) uncomment ITEM_PIPELINES in "settings.py, the default number 300 in ITEM_PIPELINES is the priority, lower number = higher priority
2) install mysql connector "pip install mysql-connector-python" from terminal
3) download and set up a local MySQL database then create a schema
4) import mysql connector into "pipeline.py" (if not using mysql, you could use the built-in sqlite3)
5) then in "pipeline.py", define methods to manipulate the database using SQL statements
6) entering "scrapy crawl spider -o laptops.json" from the terminal, and data will both be exported as a .json file + imported into MySQL

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


