from flask import Flask, Response, jsonify, render_template
from base64 import b64encode
import requests


app = Flask(__name__)


def load_picture(url):
    response = requests.get(url)
    return b64encode(response.content).decode("ascii")

def make_SVG():
    img = load_picture("https://avatars0.githubusercontent.com/u/25467285?s=460&u=420addfbce6e418fcef537546caa6116dc51df2c&v=4")
    data_dict = {
        "image": img
    }
    return render_template("intro.html.j2", **data_dict)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    svg = make_SVG()

    resp = Response(svg, mimetype="image/svg+xml")
    resp.headers["Cache-Control"] = "s-maxage=1"

    return resp

if __name__ == "__main__":
    app.run(debug=True)
