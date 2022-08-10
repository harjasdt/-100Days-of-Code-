from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
page=response.text
soup=BeautifulSoup(page,"html.parser")
heading=soup.find_all(name="a",class_="titlelink")
allheading=[]
allvotes=[]
alllinks=[]
for heading in heading:
    allheading.append(heading.getText())
    alllinks.append(heading.get("href"))


upvotes=soup.find_all(name="span", class_="score")
for i in upvotes:
    allvotes.append(int(i.getText().split(" ")[0]))

print(alllinks)
print(allvotes)
print(allheading)

ind=allvotes.index(max(allvotes))

print(alllinks[ind])
print(allvotes[ind])
print(allheading[ind])