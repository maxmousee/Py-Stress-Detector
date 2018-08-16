"""
StressDetector WebService class, using Python3 and Flask
For information on how to run and how to do a sample request, check README file
@author: MaxMouse
"""

import emd
import json
import numpy as np
import utils_stress_detector
from flask import Flask
from flask import Response
from flask import jsonify
from flask import request
from flask import flash, request, redirect, url_for


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


ALLOWED_EXTENSIONS = set(['wav', 'wave'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/isunderstress', methods=["POST"])
def isunderstress():
    # check if the post request has the file part
    if 'file' not in request.files:
        response = Response(
            mimetype="application/json",
            status=400
        )
        return response
    file = request.files['file']

    dat2 = request.get_json()
    dat2 = dat2[2:-2]
    dat1 = np.fromstring(dat2, dtype=int, sep=', ')
    rate1 = len(dat1)
    the_emd = emd.emd(dat1, extrapolation=None, nimfs=8, shifting_distance=0.2)
    count_zeros = utils_stress_detector.get_zero_crossings(the_emd)
    audio_time_length = len(dat1)/float(rate1)

    stress_tremor_avg = count_zeros - 1
    stress_tremor_avg = stress_tremor_avg/audio_time_length
    under_stress = False
    if stress_tremor_avg > 12:
        under_stress = True
    elif stress_tremor_avg < 8:
        under_stress = True

    output = {'under_stress':under_stress}
    response = Response(
            mimetype="application/json",
            response=json.dumps(output),
            status=200
        )
    return response

