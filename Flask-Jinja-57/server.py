from flask import Flask, render_template
import requests

app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/')
def api_calls(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_txt=age_response.json()
    age=age_txt["age"]

    gender_response=requests.get(f"https://api.genderize.io?name={name}")
    gender_txt=gender_response.json()
    gender=gender_txt["gender"]
    return render_template("index.html", age=age, gender=gender, name=name.title())

#or put "name, age, gender" into a dictionary and pass dict to render_template
'''**response.text V/S response.json()
-- response.text -> This is a string, formatted as JSON, but not yet parsed. Cannot access fields
-- response.json() -> Python dictionary. Values can be accessed.
'''
@app.route("/blog/<num>")
def blog_posts(num):
    print(num)
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    blog_response=requests.get(url=blog_url)
    all_posts=blog_response.json()
    return render_template("blog.html",posts=all_posts)

if __name__=="__main__":
    app.run(debug=True)