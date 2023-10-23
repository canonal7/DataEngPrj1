# importing Flask and other modules
import json
import logging
import os
from io import StringIO

import pandas as pd
from flask import Flask, request, render_template, jsonify

from iris_predictor import IrisPredictor

# Flask constructor
app = Flask(__name__)

dp = IrisPredictor(os.environ.get('MODEL_NAME', 'MODEL_NAME environment variable is not set.'))


# A decorator used to tell the application
# which URL is associated function
@app.route('/checkspecies', methods=["GET", "POST"])
def check_species():
    if request.method == "GET":
        return render_template("input_form_page.html")

    elif request.method == "POST":
        prediction_input = [
            {
                "sl": int(request.form.get("sl")),  
                "sw": int(request.form.get("sw")),  
                "pl": int(request.form.get("pl")),
                "pw": int(request.form.get("pw"))
                
            }
        ]
        logging.debug("Prediction Input : %s", prediction_input)
        df = pd.read_json(StringIO(json.dumps(prediction_input)), orient='records')
        status = dp.predict_single_record(df)

        return render_template("response_page.html",
                               prediction_variable=status)

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkdiabetes' path


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
