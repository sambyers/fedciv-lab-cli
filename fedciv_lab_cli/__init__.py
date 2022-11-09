import json
import os
import click
from fedciv_lab_cli.services import LabAPI
from fedciv_lab_cli.util import echo_time


LAB_URL = os.getenv("CIVLAB_URL")
LAB_TOKEN = os.getenv("CIVLAB_API_KEY")

if not LAB_URL:
    click.echo("CIVLAB_URL environment variable not set.")
    quit()
if not LAB_TOKEN:
    click.echo("LAB_API_KEY environment variable not set.")
    quit()


@click.group()
def cli():
    pass


@click.command(
    "reset",
    help=(
        "Provide a device name argument to reset. For "
        "available devices, use `civlab list`. "
        "Use the `civlab reset all` to reset all lab devices."
    ),
)
@click.argument("devicename")
def reset(devicename):
    click.echo(
        "Depending on which device you are resetting, "
        "this could take from 5 to 20 minutes. "
        "Check status of the job by using `civlab job [JOB ID] and "
        "after the job is finished, check status of the device "
        "by using `civlab status [DEVICE NAME]."
    )
    api = LabAPI(LAB_URL, LAB_TOKEN)
    devicename = devicename.strip()
    devicename = devicename.lower()
    if devicename == "all":
        resp = api.start_reset_all()
    elif devicename == "network-devices":
        resp = api.start_reset_netdev()
    else:
        resp = api.start_reset(devicename)
    click.echo(json.dumps(resp, indent=4))


@click.command(
    "status",
    help=(
        "Provide a device name argument to get status. For "
        "available devices, use `civlab list`. "
        "Use the `civlab status all` to get all lab device status and  "
        "`civlab status network-devices` for just network devices. "
    ),
)
@click.argument("devicename")
@echo_time
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


cli.add_command(reset)
cli.add_command(status)
cli.add_command(job_status)
cli.add_command(get_list)

if __name__ == "__main__":
    cli()
