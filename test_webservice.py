from werkzeug.datastructures import FileStorage

import pytest

import StressDetectorWS

@pytest.fixture
def client():
    StressDetectorWS.app.config['TESTING'] = True

    with StressDetectorWS.app.test_client() as client:
        with StressDetectorWS.app.app_context():
            print("Initialized functional tests")
        yield client


def test_no_file(client):
    """No file sent."""

    rv = client.post('/api/isunderstress')
    assert b'No valid file provided' in rv.data


def test_under_stress(client):
    """Under stress."""

    my_audio = "rain_man_driver_8000.wav"

    my_file = FileStorage(
        stream=open(my_audio, "rb"),
        filename="rain_man_driver_8000.wav",
        content_type="multipart/form-data",
    ),

    rv = client.post(
        "/api/isunderstress",
        data={
            "file": my_file,
        },
        content_type="multipart/form-data"
    )
    assert b'{"under_stress": true}' in rv.data