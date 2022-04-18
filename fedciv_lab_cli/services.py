import requests, os


class LabAPI:
    def __init__(self, url):
        self.base_url = url
        self.headers = {'access_token':os.environ['TOKEN']}

    def get_status(self, name: str = None):
        try:
            if name != 'all':
                resp = requests.get(f"{self.base_url}/status/{name}", headers = self.headers)
            elif name == 'all':
                resp = requests.get(f"{self.base_url}/status", headers = self.headers)
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        return resp.json()

    def start_reset(self, name: str = None):
        try:
            if 'dnac' in name:
                resp = requests.put(f"{self.base_url}/reset/dnac", headers = self.headers)
            elif 'ise' in name:
                resp = requests.put(f"{self.base_url}/reset/ise", headers = self.headers)
            elif 'vmanage' in name:
                resp = requests.put(f"{self.base_url}/reset/vmanage", headers = self.headers)

                #pass name which would be hostname for a specific device
            elif len(name) > 1:
                resp = requests.put(f"{self.base_url}/reset/{name}", headers = self.headers)

                #if name var is 0, reset whole lab
            elif 'all' in name:
                resp = requests.put(f"{self.base_url}/reset", headers = self.headers)
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        
        return resp.json()

    def job_status(self, jobID: str = None):
        try:
            resp = requests.put(f"{self.base_url}/job/{jobID}", headers = self.headers)
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)

        return resp.json()