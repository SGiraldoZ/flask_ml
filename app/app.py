from flask import Flask
from joblib import load
import numpy as np

app = Flask(__name__)

@app.route("/")
def base_route():
    test_np = np.array([[1],[2]])
    model = load('../model/model.joblib')
    preds = model.predict(test_np)
    return str(preds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


    