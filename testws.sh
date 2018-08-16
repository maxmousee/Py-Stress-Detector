#!/usr/bin/env bash

export FLASK_APP=StressDetectorWS.py;
python3 -m flask run & sleep 5; curl -F "file=@rain_man_driver_8000.wav" http://localhost:5000/api/isunderstress;
kill $!;
cd ..;