import json
import click
import requests
from services import LabAPI


@click.group()
def cli():
    pass


@click.command()
@click.option("--devicename", help="Input 'all' or appliance name (ise, dnac, vmanage) or hostname of device to reset")
def reset_lab(devicename):
    # send info to localhost:5000 running the flask app/API backend
    try:
        api = LabAPI("http://localhost")
        resp = api.start_reset(devicename)
        print(json.dumps(resp, indent=4))
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


@click.command()
@click.option("--devicename", help="Input 'all' or appliance name (ise, dnac, vmanage) or hostname of device to reset")
def status(devicename):
    # send info to localhost running the API
    api = LabAPI("http://localhost:80")
    resp = api.get_status(devicename)
    print(json.dumps(resp, indent=4))

@click.command()
@click.option("--jobID", help="Input Job ID")
def job_status(jobID):
    # send info to localhost running the API
    api = LabAPI("http://localhost")
    resp = api.job_status(jobID)
    print(json.dumps(resp, indent=4))



cli.add_command(reset_lab)
cli.add_command(status)
cli.add_command(job_status)

if __name__ == "__main__":
    cli()