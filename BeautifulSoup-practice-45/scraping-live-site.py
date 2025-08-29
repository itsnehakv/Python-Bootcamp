import requests
from bs4 import BeautifulSoup

response=requests.get("https://news.ycombinator.com/news")
webpage_content=response.text

soup= BeautifulSoup(webpage_content, "html.parser")

span_titleline=list(soup.find_all(name="span", class_="titleline"))
article_tags=[]
article_texts=[]
article_links=[]

for anchor in span_titleline:
    tag=anchor.find(name="a")
    article_tags.append(tag)
    text=tag.getText()
    article_texts.append(text)
    link=tag.get("href")
    article_links.append(link)

print(article_links)
print(article_tags)
print(article_texts)

article_score=[int(score.getText().split(sep=" ")[0]) for score in soup.find_all(class_="score")]
#w/o split -->158 points, 48 points....w/ split-->['158','points']

max_score=max(article_score)
index_of_max=article_score.index(max_score)
print(article_texts[index_of_max])
print(article_links[index_of_max])


