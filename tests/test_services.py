import pytest
from fedciv_lab_cli import services


@pytest.fixture()
def labapi():
    yield services.LabAPI("http://test.lab", "12345")


@pytest.fixture()
def mock_status_data():
    resp = {
        "status": {
            "dnac": {
                "host": "10.1.1.1",
                "last_restore": "10-26 19:36:57",
                "restore_file": "multidomain3.tar.gz",
            },
            "devices": [
                {
                    "name": "br1-sw1",
                    "host": "10.1.1.1",
                    "default_cfg_on_flash": True,
                    "status": "default",
                },
            ],
        }
    }
    yield resp


@pytest.fixture()
def mock_list_data():
    resp = {
        "appliances": [
            {"name": "dnac", "host": "10.1.1.1"},
        ],
        "network_devices": [
            {"name": "br1-sw1", "host": "10.1.1.1"},
        ],
    }
    yield resp


def test_get_status_all(requests_mock, labapi, mock_status_data):
    requests_mock.get("http://test.lab/status", json=mock_status_data)
    resp = labapi.get_status_all()
    assert resp == mock_status_data


def test_get_status_netdevices(requests_mock, labapi, mock_status_data):
    requests_mock.get("http://test.lab/status/network-devices", json=mock_status_data)
    resp = labapi.get_status_netdev()
    assert resp == mock_status_data


def test_get_status_device(requests_mock, labapi, mock_status_data):
    requests_mock.get("http://test.lab/status/test", json=mock_status_data)
    resp = labapi.get_status("test")
    assert resp == mock_status_data


def test_reset_lab(labapi):
    pass


def test_reset_lab_device(labapi):
    pass
