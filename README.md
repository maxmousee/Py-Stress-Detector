# Stress Detector

[![CI Status](https://circleci.com/gh/maxmousee/Py-Stress-Detector.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/maxmousee/Py-Stress-Detector)

[![BCH compliance](https://bettercodehub.com/edge/badge/maxmousee/Py-Stress-Detector?branch=master)](https://bettercodehub.com/)

# Install dependencies

If you are using Ubuntu, you will need to install the following packages:
python3-pip libfreetype6-dev libfreetype6 libpng-dev pkg-config
To do that, run:
"sudo apt-get install -y python3-pip libfreetype6-dev libfreetype6 libpng-dev curl pkg-config"

If you are using MacOS, install brew and then run the following commands:
"brew install freetype; brew install pkg-config; brew install libpng" 

Using Python 3, run "pip -r requirements.txt --user" without the quotes

# WebService

To run it just go to the folder and type "export FLASK_APP=StressDetectorWS.py; python3 -m flask run" without the quotes
It will run as a http service listening to port 5000

To send a test request just run "curl -F "file=@rain_man_driver_8000.wav" http://localhost:5000/api/isunderstress"

Build docker image:
"docker build -t py-stress-detector:latest ."

Run using docker:
"docker run -t -p 5000:5000 -d py-stress-detector:latest"

Check if container is running:
"docker ps"

Kill (all) docker images:
"docker kill $(docker ps -q)"

# Desktop

To run it just go to the folder and type "python3 StressDetectorDesktop.py -i <inputfile>" without the quotes
It will verify stress level for the input file passed by argument. Feel free to change the code to check for other files.
It should print the graph of the stress data as well.

If you want to run it inside the docker container, just run:
"docker exec -it <containerIdOrName> bash"
then
Run it as it was in your local machine... python3 StressDetectorDesktop.py...

## Tested only with 8000KHz sample rate WAV files
