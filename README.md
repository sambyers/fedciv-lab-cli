[![.github/workflows/lint-fmt-test.yml](https://github.com/sambyers/fedciv-lab-cli/actions/workflows/lint-fmt-test.yml/badge.svg)](https://github.com/sambyers/fedciv-lab-cli/actions/workflows/lint-fmt-test.yml)

# FedCiv Lab CLI

## Download and Install
```shell
git clone https://github.com/sambyers/fedciv-lab-cli
pip install .
```

## Setup
```shell
export CIVLAB_URL=http://x.x.x.x
export CIVLAB_API_KEY=access_token
```

## Usage
```shell
civlab --help
Usage: civlab [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  job     Provide a Job ID argument to get the status of a job.
  list    List all devices available via the CivLab API.
  reset   Provide a device name argument to reset.
  status  Provide a device name argument to get status.
```
```shell
civlab status ise
{
    "status": {
        "ise": {
            "host": "10.1.2.3",
            "last_restore": "Thu Nov 03 01:16:32 UTC 2022",
            "restore_file": "ise_backup1.tar.gpg",
            "status": "RESTORE COMPLETED"
        }
    }
}
```
