# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import a connector to connect python to mysql database
import mysql.connector

class CentcompscrapingPipeline:

    # this method initializes an object by creating a db connection and a table within that db
    def __init__(self):
        self.create_connection()
        self.create_table()

    # create a connection to "centcomp.db" and a cursor to send commands
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'lablab90...',
            database = 'centcomp'
        )
        self.curr = self.conn.cursor()

    # create a method that creates a table & drop the table if it exists
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS laptops_tb""")
        self.curr.execute("""CREATE TABLE laptops_tb(
                title text,
                price text,
                image text,
                detail text
            )"""
        )

    # create a method to insert items into the table
    def store_db(self, item):
        title = item.get('title')
        price = item.get('price')
        image = item.get('image')
        detail = item.get('detail')

        # check if all required fields are present
        if title and price and image and detail:
            self.curr.execute("""INSERT INTO laptops_tb VALUES (%s, %s, %s, %s)""", (
                    title[0],
                    price[0],
                    image[0],
                    detail[0]

                )
            )
            self.conn.commit()
        else:
            pass

    # this method stores items inside of the database
    def process_item(self, item, spider):
        self.store_db(item)
        return item
