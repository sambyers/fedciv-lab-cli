import requests, os


class LabAPI:
    def __init__(self, url):
        self.base_url = url
        self.headers = {'access_token':os.environ['CIVLAB_API_KEY']}

    def get_status(self, name: str = None):
        try:
            name = name.strip()
            if name != 'all':
                
                resp = requests.get(f"{self.base_url}/status/{name}", headers = self.headers)
            elif name == 'all':
                resp = requests.get(f"{self.base_url}/status", headers = self.headers)
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        return resp.json()

    def start_reset(self, name: str = None):
        try:
            name = name.strip()
            if name != 'all':
                
                resp = requests.get(f"{self.base_url}/reset/{name}", headers = self.headers)
            elif name == 'all':
                
                resp = requests.get(f"{self.base_url}/reset", headers = self.headers)
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        
        return resp.json()

    def job_status(self, jobID: str = None):
        try:
            jobID = jobID.strip()
            resp = requests.put(f"{self.base_url}/job/{jobID}", headers = self.headers)
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)

        return resp.json()