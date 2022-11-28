import requests


class LabAPI:
    def __init__(self, url, token):
        self.base_url = url
        self.headers = {"access_token": token}
        self.verify = False
        self.version = "v1"

    def request(self, method: str, path: str, params: dict = None, body: dict = None):
        method = method.lower()
        req = getattr(requests, method)
        url = f"{self.base_url}/{self.version}{path}"
        try:
            resp = req(
                url, headers=self.headers, verify=self.verify, params=params, json=body
            )
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        return resp.json()

    def get_status(self, name: str = None):
        return self.request("get", f"/status/{name}")

    def get_status_netdev(self):
        return self.request("get", "/status/network-devices")

    def get_status_all(self):
        return self.request("get", "/status")

    def start_reset(self, name: str = None):
        return self.request("put", f"/reset/{name}")

    def start_reset_all(self):
        return self.request("put", "/reset")

    def start_reset_netdev(self):
        return self.request("put", "/reset/network-devices")

    def job_status(self, jobID: str = None):
        return self.request("get", f"/job/{jobID}")

    def get_list(self):
        return self.request("get", "/list")
