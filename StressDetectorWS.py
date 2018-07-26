"""
To run it just go to the folder and type "python StressDetectorWS.py" without the quotes
It will run as a http service listening to port 8080

Audio data array should be 8000 samples of wav data, 1 second of a 8KHz sample rate audio
To send a test request just run "curl -H "Content-Type: application/json" --data @audiodata.json http://localhost:8080/processAudio"
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


app = Flask(__name__)


@app.route('/api/isunderstress', methods=["POST"])
def isunderstress():
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