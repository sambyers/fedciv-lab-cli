from json import dumps
from os import getenv
from sys import exit
import click
from fedciv_lab_cli.services import LabAPI


@click.group()
def cli():
    pass


def get_url():
    url = getenv("CIVLAB_URL")
    if not url:
        print("Environmental variable CIVLAB_URL missing!")
        print("Ex. CIVLAB_URL=http://example.com")
        exit()
    return url


@click.command()
@click.option("--name", help="Name of device to reset.")
def reset(name: str):
    api = LabAPI(get_url())
    if name:
        resp = api.start_reset(name=name)
    else:
        print("Resetting all devices in the lab. This will take 30-45 minutes.")
        resp = api.start_reset()
    print(dumps(resp, indent=4))


@click.option("--name", help="Name of device for which to get status.")
@click.command()
def status(name: str):
    api = LabAPI(get_url())
    if name:
        resp = api.get_status(name=name)
    else:
        print(
            "Fetching status for all devices in the lab. \
            This will take a few moments..."
        )
        resp = api.get_status()
    print(dumps(resp, indent=4))


cli.add_command(reset)
cli.add_command(status)

if __name__ == "__main__":
    cli()
