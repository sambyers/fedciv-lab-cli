# Main CLI code here

import click

@click.group()
def cli():
    pass

@click.command()
@click.option("--arg1", help="Input arg1")
@click.option("--arg2", help ="Input arg2")
def reset_lab(arg1, arg2):
    #do something
    print('you inputted arg1: ', arg1, ' arg2 is: ', arg2)

@click.command()
@click.option("--arg1", help="input arg1")
def lab_status(arg1):
    #do something
    print('you inputted arg1: ', arg1)



cli.add_command(reset_lab)
cli.add_command(lab_status)


if __name__ == "__main__":
    cli()

    



   




