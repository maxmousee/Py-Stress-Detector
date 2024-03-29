# Stress Detector

[![CircleCI](https://circleci.com/gh/maxmousee/Py-Stress-Detector/tree/master.svg?style=svg)](https://circleci.com/gh/maxmousee/Py-Stress-Detector/tree/master)

# Install dependencies

If you are using Ubuntu, you will need to install the following packages:
python3-pip libfreetype6-dev libfreetype6 libpng-dev pkg-config
To do that, run:
"sudo apt-get install -y python3-pip libfreetype6-dev libfreetype6 libpng-dev curl pkg-config"

If you are using MacOS, install brew and then run the following commands:
"brew install freetype; brew install pkg-config; brew install libpng"

Using Python 3, run "pip3 -r requirements.txt --user" without the quotes

If you're using a Mac with Apple Silicon, you might need to install a nightly build of scipy

"pip3 install --pre -i https://pypi.anaconda.org/scipy-wheels-nightly/simple scipy"

# Run tests

To run unit and functional tests, just run "pytest".

# WebService

To run it just go to the folder and type "export FLASK_APP=StressDetectorWS.py; python3 -m flask run" without the quotes
It will run as a http service listening to port 5000

### If you prefer to run it using docker, here is how:

Build docker image:
"docker build -t py-stress-detector:latest ."

Run using docker:
"docker run -t -p 5000:5000 -d py-stress-detector:latest"

Check if container is running:
"docker ps"

Kill (all) docker images:
"docker kill $(docker ps -q)"

#### To send a test request just run "curl -F "file=@rain_man_driver_8000.wav" http://localhost:5000/api/isunderstress"

# Desktop

To run it just go to the folder and type "python3 StressDetectorDesktop.py -i inputfile" without the quotes
It will verify stress level for the input file passed by argument.

If you want to run it inside the docker container, just run:
"docker exec -it containerIdOrName bash"
then
Run it as it was in your local machine... python3 StressDetectorDesktop.py...

## Tested only with 8000KHz sample rate WAV files
