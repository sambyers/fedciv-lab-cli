import json
import os
import click
from fedciv_lab_cli.services import LabAPI


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
        "Use the `civlan reset all` to reset all lab devices."
    ),
)
@click.argument("devicename")
def reset_lab(devicename):
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
def status(devicename):
    api = LabAPI(LAB_URL, LAB_TOKEN)
    devicename = devicename.strip()
    devicename = devicename.lower()
    resp = api.get_status(devicename)
    click.echo(json.dumps(resp, indent=4))


@click.command("job", help="Provide a Job ID argument to get the status of a job.")
@click.argument("job_id")
def job_status(jobID):
    api = LabAPI(LAB_URL, LAB_TOKEN)
    jobID = jobID.strip()
    resp = api.job_status(jobID)
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
