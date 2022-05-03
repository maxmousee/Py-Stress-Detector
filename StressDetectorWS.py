"""
StressDetector WebService main class, using Python3 and Flask
For information on how to run and how to do a sample request, check README file
@author: MaxMouse
"""

import utils_stress_detector
import json
import os
import string
from flask import Flask
from flask import Response
from flask import request
from random import randint, choice

ALLOWED_EXTENSIONS = {'wav', 'wave'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + "/vsd_uploads"

min_char = 12
max_char = 60
all_char = string.ascii_letters + string.digits

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def valid_file(request):
    # check if the post request has a valid file
    if 'file' not in request.files:
        return False
    file = request.files['file']
    if file and allowed_file(file.filename):
        return True
    else:
        return False


def audio_file_is_under_stress(filename):
    sample_rate, audio_data = utils_stress_detector.get_audio_data_from_file_absolute_path(filename)
    stress_tremor_avg = utils_stress_detector.get_stress_tremor_average_from_data(audio_data, sample_rate)
    return utils_stress_detector.is_under_stress(stress_tremor_avg)


def get_invalid_file_response():
    output = {'error': 'No valid file provided'}
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=400
    )
    return response


def get_stress_response(under_stress):
    output = {'under_stress': under_stress}
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=200
    )
    return response


@app.route('/api/isunderstress', methods=["POST"])
def is_under_stress():
    if valid_file(request):
        random_file_name = "".join(choice(all_char) for x in range(randint(min_char, max_char)))
        filename = app.config['UPLOAD_FOLDER'] + "/" + random_file_name
        request.files['file'].save(filename)
        under_stress = audio_file_is_under_stress(filename)
        os.remove(filename)
        return get_stress_response(under_stress)
    else:
        return get_invalid_file_response()
