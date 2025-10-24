from flask import Flask, render_template, request
import requests
import smtplib
# import os
# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)

posts_response = requests.get(" https://api.npoint.io/4d3316bdf20d51544192")
posts = posts_response.json()

EMAIL="testingpythongoo@gmail.com"
PASSWORD="thisisatest5678"

@app.route('/')
def get_all_posts():
    return render_template("index.html",all_posts=posts)

@app.route('/<int:blog_id>')
def post_open(blog_id):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == blog_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post,img=requested_post["img"])

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact', methods=["GET","POST"])
def contact_page():
    if request.method=="POST":
        data=request.form
        send_email(data["name"], data["email"], data["phoneno"], data["message"])
        heading = "Contact Me"
        return render_template("contact.html", data_entered=True)
    return render_template("contact.html",data_entered=False )

@app.post('/contact')
def receive_data():
    heading="Successfully sent message"
    return render_template("contact.html", heading=heading)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)

