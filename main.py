from flask import Flask, render_template
import requests

app = Flask(__name__)

json_endpoint_url = " https://api.npoint.io/2f69e31b2a0c018e9f83"


@app.route('/')
def home():
    response = requests.get(url=json_endpoint_url)
    response_json = response.json()
    print(response_json)
    return render_template("index.html", blogs=response_json)


@app.route('/<int:post_id>')
def show_post(post_id):
    response = requests.get(url=json_endpoint_url)
    response_json = response.json()
    return render_template("post.html", blog=response_json[post_id])


if __name__ == "__main__":
    app.run(debug=True)
