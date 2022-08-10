from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
soup=BeautifulSoup(response,"html.parser")
all=soup.find_all(name="h3",class_="title")
ans=[]
for i in all:
    ans.append(i.getText())

ans.reverse()
for i in ans:
    print(i)