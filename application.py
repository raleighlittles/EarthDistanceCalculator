from flask import Flask
from flask import request
from flask import render_template

# see: https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
# https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template

import calculation as Distance

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("basic-view.html")

@app.route('/', methods=['POST'])
def my_form_post():
    point_A_text = request.form['point-A']
    point_B_text = request.form['point-B']
    print(point_A_text)
    point_A_lat, point_A_lon = float(point_A_text.split(',')[0]), float(point_A_text.split(',')[1])
    point_B_lat, point_B_lon = float(point_B_text.split(',')[0]), float(point_B_text.split(',')[1])
    print(point_A_lat)

    euclid = Distance.euclidean_distance(point_A_lat, point_A_lon, point_B_lat, point_B_lon)
    greatcircle = Distance.great_circle_distance(point_A_lat, point_A_lon, point_B_lat, point_B_lon)
    vincenty = Distance.vincenty_distance(point_A_lat, point_A_lon, point_B_lat, point_B_lon)
    return("Euclid distance: {} \n Great Circle distance: {} \n Vincenty Distance: {}".format(str(euclid), str(greatcircle), str(vincenty)))


if __name__ == '__main__':
    app.run()