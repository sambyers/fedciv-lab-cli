import requests


class LabAPI:
    def __init__(self, url):
        self.base_url = url

    def get_status(self):
        try:
            resp = requests.get(f"{self.base_url}/status")
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        return resp.json()
