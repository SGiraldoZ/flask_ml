from flask import Flask, render_template, request
from joblib import load
import numpy as np
from functions import floats_string_to_np_arr

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def base_route():
    return render_template('index.html')


@app.route("/addValues", methods=['GET','POST'])
def add_value():
    model = load("../model/model.joblib")
    input = request.form["values"]
    input_arr = floats_string_to_np_arr(input)
    return str(input_arr)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
