"""
StressDetector WebService class, using Python3 and Flask
For information on how to run and how to do a sample request, check README file
@author: MaxMouse
"""

import emd
import json
import os
import numpy as np
import utils_stress_detector
from flask import Flask
from flask import Response
from flask import jsonify
from flask import request
from flask import flash, request, redirect, url_for
import string
from random import *


ALLOWED_EXTENSIONS = set(['wav', 'wave'])


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + "/vsd_uploads"


min_char = 12
max_char = 60
allchar = string.ascii_letters + string.digits


if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/isunderstress', methods=["POST"])
def isunderstress():
    # check if the post request has the file part
    if 'file' not in request.files:
        output = {'error':'No file provided'}
        response = Response(
            mimetype="application/json",
            response=json.dumps(output),
            status=400
        )
        return response
    file = request.files['file']
    if file and allowed_file(file.filename):
        random_file_name = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
        filename = app.config['UPLOAD_FOLDER'] + "/" + random_file_name
        file.save(filename)
        dat1 = utils_stress_detector.get_audio_data_from_file_absolute_path(filename)
        rate1 = utils_stress_detector.get_audio_sample_rate_from_file_absolute_path(filename)
        os.remove(filename)
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

