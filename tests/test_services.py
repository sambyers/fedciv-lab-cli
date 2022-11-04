import pytest
from fedciv_lab_cli import services


@pytest.fixture()
def labapi():
    yield services.LabAPI("http://test.lab", "12345")


@pytest.fixture()
def mock_status_data():
    resp = {
        "status": {
            "dnac": None,
            "sdwan": None,
            "ise": None,
            "devices": [
                {
                    "name": "br1-sw1",
                    "status": "default",
                    "ip": "10.83.16.159",
                    "credentials": None,
                    "default_cfg": True,
                },
                {
                    "name": "br2-sw1",
                    "status": "default",
                    "ip": "10.83.16.160",
                    "credentials": None,
                    "default_cfg": True,
                },
                {
                    "name": "campus1-bn1",
                    "status": "configured",
                    "ip": "10.83.16.161",
                    "credentials": None,
                    "default_cfg": True,
                },
                {
                    "name": "campus1-bn2",
                    "status": "configured",
                    "ip": "10.83.16.162",
                    "credentials": None,
                    "default_cfg": True,
                },
                {
                    "name": "campus1-fe1",
                    "status": "configured",
                    "ip": "10.83.16.163",
                    "credentials": None,
                    "default_cfg": True,
                },
                {
                    "name": "campus1-fe2",
                    "status": "configured",
                    "ip": "10.83.16.164",
                    "credentials": None,
                    "default_cfg": True,
                },
                {
                    "name": "campus2-bn1",
                    "status": "default",
                    "ip": "10.83.16.165",
                    "credentials": None,
                    "default_cfg": True,
                },
                {
                    "name": "campus2-fe1",
                    "status": "configured",
                    "ip": "10.83.16.166",
                    "credentials": None,
                    "default_cfg": True,
                },
            ],
        }
    }
    yield resp


def test_get_status(requests_mock, labapi, mock_status_data):
    requests_mock.get("http://test.lab/status", json=mock_status_data)
    resp = labapi.get_status("test")
    assert resp == mock_status_data


def test_get_status_device(labapi):
    pass


def test_reset_lab(labapi):
    pass


def test_reset_lab_device(labapi):
    pass
