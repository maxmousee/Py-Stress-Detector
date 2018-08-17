FROM python:3.6
EXPOSE 5000


COPY requirements.txt /
RUN pip install -r requirements.txt --user

COPY utils_stress_detector.py /
COPY rain_man_driver_8000.wav /
COPY StressDetectorWS.py /
COPY StressDetectorDesktop.py /
COPY utils.py /
COPY emd.py /


ENV FLASK_APP StressDetectorWS.py

ENV FLASK_ENV development

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]