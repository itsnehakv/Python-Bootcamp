from bs4 import BeautifulSoup
from matplotlib.pyplot import title

with open("website.html") as file:
    contents=file.read()

BS=BeautifulSoup(contents, "html.parser")

print(BS.title)   #<title>Angela's Personal Site</title>    gets the FIRST title tag
print(BS.title.string)  #Angela's Personal Site


all_anchor_tags=BS.find_all(name="a")    #BS.find() -->returns first item with mentioned tag name  eg. the first h1 tage
for anchor in all_anchor_tags:
    print(anchor.getText()) #The App Brewery   My Hobbies  Contact Me
    print(anchor.get("href"))   #https://www.appbrewery.co/   https://angelabauer.github.io/cv/hobbies.html


heading=BS.find(name="h1", id="name")
print(heading)  #<h1 id="name">Angela Yu</h1>
print(heading.name)  #h1
'''ALSO, class_="...."'''


url=BS.select_one(selector="p a")
'''Indicates an anchor tag within a para tag. Mentioned in style section
.select_one() selects first instance     .select() selects all instances, returns list'''
selecting_byid=BS.select_one(selector="#name")   #for ID, not mentioned in style, just an attr.  .name for class