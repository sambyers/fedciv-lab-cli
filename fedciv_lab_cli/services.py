import requests


class LabAPI:
    def __init__(self, url):
        self.base_url = url

    def get_status(self, name: str = None):
        try:
            if name:
                resp = requests.get(f"{self.base_url}/status/{name}")
            else:
                resp = requests.get(f"{self.base_url}/status")
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        return resp.json()
