from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    post_json = blog_posts.json()
    return render_template("index.html", posts=post_json)

@app.route("/post/<int:blog_id>")
def post(blog_id):
    post_url = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_post = post_url.json()[blog_id - 1]
    return render_template("post.html", post=blog_post)

if __name__ == "__main__":
    app.run(debug=True)
