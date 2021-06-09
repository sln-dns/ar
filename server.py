from flask import Flask, render_template, request
from coordinates import longitude_now, latitude_now

app = Flask(__name__)

@app.route('/')

def index():
    title = "AR vision"
    longitude = longitude_now()
    latitude = latitude_now()
    return render_template('index.html', page_title=title, longitude=longitude, latitude=latitude)


if __name__ == "__main__":
    app.run(debug=True)