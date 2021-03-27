from flask import Flask, render_template, request
import requests
import send_email

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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", title="Contact Me")
    else:
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        print(f'<h1>Successfully sent your message.</h1>'
              f'Name: {name}<br>'
              f'Email: {email}<br>'
              f'Phone: {phone}<br>'
              f'Message: {message}<br>')
        send_email.send_mail_yahoo(
            subject='Message from Web-form',
            msg_body=f'Name: {name}\n'
                     f'Email: {email}\n'
                     f'Phone: {phone}\n'
                     f'Message: \n{message}'
        )
        return render_template("contact.html", title="Successfully sent your message.")


# @app.route('/form-entry', methods=["GET", "POST"])
# def receive_data():
#     # name = request.form["name"]
#     # email = request.form["email"]
#     # phone = request.form["phone"]
#     # message = request.form["message"]
#     data = request.form
#     # print(data)
#     # >>> ImmutableMultiDict([('name', 'John'), ('email', 'j@jp.com'), ('phone', ''), ('message', 'Hello')])
#     name = data["name"]
#     email = data["email"]
#     phone = data["phone"]
#     message = data["message"]
#
#     return f'<h1>Successfully sent your message.</h1>' \
#            f'Name: {name}<br>' \
#            f'Email: {email}<br>' \
#            f'Phone: {phone}<br>' \
#            f'Message: {message}<br>'


if __name__ == '__main__':
    # To enable all development features (including debug mode) you can export the
    #   FLASK_ENV environment variable and set it to development before
    #   running the server:
    #
    # $ set FLASK_ENV=development

    blogs = get_blog_data()
    # print(blogs)
    app.run(host='localhost', port=5001, debug=True)
