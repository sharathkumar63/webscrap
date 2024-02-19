import requests
from bs4 import BeautifulSoup

url = "https://www.abc.com"  # Replace this with the actual URL

response = requests.get(url)
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

desc_elements = soup.find_all(class_="title")
desc_elementss = soup.find_all(class_="desc")
feed_elements = soup.find_all(class_="feed")

for no, (title, desc, feed) in enumerate(zip(desc_elements, desc_elementss, feed_elements)):
    print("Title -", no)
    print("Title:", title.get_text())
    print("Description:", desc.get_text())
    print("Feed:", feed.get_text())
    print("--------------------")
