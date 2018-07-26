#!/usr/bin/env bash

export FLASK_APP=StressDetectorWS.py;
python3 -m flask run & sleep 5; curl -H "Content-Type: application/json" --data @audiodata.json http://localhost:5000/api/isunderstress;
kill $!;
cd ..;