# Stress Detector

[![CI Status](https://circleci.com/gh/maxmousee/Py-Stress-Detector.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/maxmousee/Py-Stress-Detector)

[![BCH compliance](https://bettercodehub.com/edge/badge/maxmousee/Py-Stress-Detector?branch=master)](https://bettercodehub.com/)

# WebService

To run it just go to the folder and type "export FLASK_APP=StressDetectorWS.py; python3 -m flask run" without the quotes
It will run as a http service listening to port 5000

To send a test request just run "curl -H "Content-Type: application/json" --data @audiodata.json http://localhost:5000/api/isunderstress"

# Desktop

To run it just go to the folder and type "python3 StressDetectorDesktop.py -i <inputfile>" without the quotes
It will verify stress level for the input file passed by argument. Feel free to change the code to check for other files.
It should print the graph of the stress data as well.

## Tested only with 8000KHz sample rate WAV files
