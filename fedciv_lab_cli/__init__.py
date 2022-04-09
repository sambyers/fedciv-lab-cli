import json
import click
import requests
from .services import LabAPI


@click.group()
def cli():
    pass


@click.command()
@click.option("--arg1", help="Input arg1")
@click.option("--arg2", help="Input arg2")
def reset_lab(arg1, arg2):
    # send info to localhost:5000 running the flask app/API backend
    try:
        # template api call for now
        requests.post("127.0.0.1:5000/reset", data={"devices": "device"})

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    print("you inputted arg1: ", arg1, " arg2 is: ", arg2)


@click.option("--name", help="Name of device for which to get status.")
@click.command()
def status(name):
    api = LabAPI("http://localhost")
    if name:
        resp = api.get_status(name=name)
    else:
        print('Fetching status for all devices in the lab. This will take a few moments...')
        resp = api.get_status()
    print(json.dumps(resp, indent=4))


cli.add_command(reset_lab)
cli.add_command(status)

if __name__ == "__main__":
    cli()
