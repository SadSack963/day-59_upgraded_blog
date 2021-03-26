from flask import Flask, render_template, request
import requests


app = Flask(__name__)


def get_blog_data():
    npoint_api_endpoint = 'https://api.npoint.io/43644ec4f0013682fc0d'
    response = requests.get(url=npoint_api_endpoint)
    response.raise_for_status()
    return response.json()


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<blog_id>')
def post(blog_id):
    id_int = int(blog_id) - 1
    return render_template("post.html", blog=blogs[id_int])


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/form-entry', methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    return f'<h1>Successfully sent your message.</h1>' \
           f'Name: {name}<br>' \
           f'Email: {email}<br>' \
           f'Phone: {phone}<br>' \
           f'Message: {message}<br>'


if __name__ == '__main__':
    # To enable all development features (including debug mode) you can export the
    #   FLASK_ENV environment variable and set it to development before
    #   running the server:
    #
    # $ set FLASK_ENV=development

    blogs = get_blog_data()
    # print(blogs)
    app.run(host='localhost', port=5001, debug=True)
