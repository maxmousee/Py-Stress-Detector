FROM python:3.6
EXPOSE 5000

COPY StressDetectorWS.py /
COPY StressDetectorDesktop.py /
COPY utils.py /
COPY emd.py /
COPY requirements.txt /
COPY utils_stress_detector.py /
COPY rain_man_driver_8000.wav /

RUN pip install -r requirements.txt --user

CMD [ "python", "./StressDetectorDesktop.py", "-i", "rain_man_driver_8000.wav" ]

ENV FLASK_APP StressDetectorWS.py

CMD [ "python", "-m", "flask", "run"]
