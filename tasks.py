from invoke import task
import shutil
import os, glob

@task
def hello (c):
    """Hello world example"""
    print ("Hello world.")

@task
def setup(c):
    """Setup project"""
    list_of_dirs = ["output"]
    for directory in list_of_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)

@task
def clear(c):
    """Clear generated dirs"""
    list_of_dirs = ["output"]
    for directory in list_of_dirs:
        if not os.path.exists(directory):
            shutil.rmtree(directory)

@task
def reset(c):
    clear(c)
    setup(c)

@task
def sphinx(c):
    c.run("rm -r _build")
    c.run("make html")

