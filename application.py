from flask import Flask
from flask import request
from flask import render_template
import re

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

    point_A_lat, point_A_lon = float(point_A_text.split(',')[0]), float(point_A_text.split(',')[1])
    point_B_lat, point_B_lon = float(point_B_text.split(',')[0]), float(point_B_text.split(',')[1])

    euclid_distance = Distance.euclidean_distance(point_A_lat, point_A_lon, point_B_lat, point_B_lon)
    greatcircle_distance = Distance.great_circle_distance(point_A_lat, point_A_lon, point_B_lat, point_B_lon)
    vincenty_distance = Distance.vincenty_distance(point_A_lat, point_A_lon, point_B_lat, point_B_lon)

    print (euclid_distance)
    print (greatcircle_distance)
    print (vincenty_distance)

    euclid_error, greatcircle_error  = Distance.compute_percentage_error(euclid_distance, greatcircle_distance, vincenty_distance)
    #return("Euclid distance: {} \n Great Circle distance: {} \n Vincenty Distance: {}".format(str(euclid), str(greatcircle), str(vincenty)))
    return render_template('results.html', euclid_distance = euclid_distance, euclid_error = euclid_error, greatcircle_distance = greatcircle_distance, greatcircle_error = greatcircle_error, vincenty_distance = vincenty_distance)



if __name__ == '__main__':
    app.run()