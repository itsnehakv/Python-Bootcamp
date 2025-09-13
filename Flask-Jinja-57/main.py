from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(url=blog_url)
all_posts = blog_response.json()


@app.route('/')
def home():
    return render_template("index.html",posts=all_posts)

@app.route('/post/<int:blog_id>')
def post_open(blog_id):
    post=all_posts[blog_id-1]
    return render_template("post.html",post=post)


if __name__ == "__main__":
    app.run(debug=True)
