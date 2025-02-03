import requests
from bs4 import BeautifulSoup
feed = requests.get("https://www.cyclobold.com/")
htmlData = feed.content
feedback = BeautifulSoup(htmlData, "html.parser")
all_img = feedback.find_all("img")
print(all_img)
# print(feedback.title.string)