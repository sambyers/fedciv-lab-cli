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

    def start_reset(self, name: str = None):
        try:
            if 'dnac' in name:
                resp = requests.put(f"{self.base_url}/reset/dnac")
            elif 'ise' in name:
                resp = requests.put(f"{self.base_url}/reset/ise")
            elif 'vmanage' in name:
                resp = requests.put(f"{self.base_url}/reset/vmanage")

                #pass name which would be hostname for a specific device
            elif len(name) > 1:
                resp = requests.put(f"{self.base_url}/reset/{name}")

                #if name var is 0, reset whole lab
            else:
                resp = requests.put(f"{self.base_url}/reset")
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        
        return resp.json()

    def job_status(self, jobID: str = None):
        try:
            resp = requests.put(f"{self.base_url}/job/{jobID}")
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)

        return resp.json()