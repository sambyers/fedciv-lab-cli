from time import time
import click
 

def timer(func):
    # This function shows the execution time of 
    # the function object passed
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        completion_time = round(time()-start, 2)
        click.echo(f"Completed in {completion_time}s")
        return result
    return wrapper