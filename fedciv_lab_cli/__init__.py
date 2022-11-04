import json
import os
import click
from fedciv_lab_cli.services import LabAPI
from fedciv_lab_cli.util import timer


LAB_URL = os.environ["CIVLAB_URL"]
LAB_TOKEN = os.environ["CIVLAB_API_KEY"]


@click.group()
def cli():
    pass


@click.command(
    "reset",
    help=(
        "Provide a device name argument to reset. For "
        "available devices, use `civlab list`. "
        "Use the `civlan reset all` to reset all lab devices. "
        f"Check out the API docs at {LAB_URL}/docs"
    ),
)
@click.argument("devicename")
def reset_lab(devicename):
    click.echo("Depending on which device you are resetting, this could take from 5 to 20 minutes. "
               "Check status of the job by using `civlab job [JOB ID] and "
               "after the job is finished, check status of the device "
               "by using `civlab status [DEVICE NAME].")
    api = LabAPI(LAB_URL, LAB_TOKEN)
    devicename = devicename.strip()
    devicename = devicename.lower()
    resp = api.start_reset(devicename)
    click.echo(json.dumps(resp, indent=4))


@click.command(
    "status",
    help=(
        "Provide a device name argument to get status. For "
        "available devices, use `civlab list`. "
        "Use the `civlan status all` to get all lab device status and  "
        "`civlab status network-devices` for just network devices. "
    ),
)
@click.argument("devicename")
@timer
def status(devicename):
    api = LabAPI(LAB_URL, LAB_TOKEN)
    devicename = devicename.strip()
    devicename = devicename.lower()
    if devicename == "all":
        resp = api.get_status_all()
    elif devicename == "network-devices":
        resp = api.get_status_netdev()
    else:
        resp = api.get_status(devicename)
    click.echo(json.dumps(resp, indent=4))


@click.command("job", help="Provide a Job ID argument to get the status of a job.")
@click.argument("id")
def job_status(id):
    api = LabAPI(LAB_URL, LAB_TOKEN)
    id = id.strip()
    id = id.lower()
    resp = api.job_status(id)
    click.echo(json.dumps(resp, indent=4))


@click.command("list", help="List all devices available via the CivLab API.")
def get_list():
    api = LabAPI(LAB_URL, LAB_TOKEN)
    resp = api.get_list()
    click.echo(json.dumps(resp, indent=4))


cli.add_command(reset_lab)
cli.add_command(status)
cli.add_command(job_status)
cli.add_command(get_list)

if __name__ == "__main__":
    cli()
