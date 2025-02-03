import requests
import pymysql
from bs4 import BeautifulSoup


db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "password"
    # database = "scrapedb"
)

cursor = db.cursor()
cursor.execute("create database `scrapedb`")
cursor.close()
db.close()

# feed = requests.get("https://www.cyclobold.com/")
# htmlData = feed.content
# feedback = BeautifulSoup(htmlData, "html.parser")
# all_img = feedback.find_all("img")
# print(all_img)
# print(feedback.title.string)