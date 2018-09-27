# custom script file.
# takes in argument and runs
from sys import argv
import subprocess
import glob
import os


# Create script to run challenges with user arguments. 
# Day 1
# subprocess.call("python challenges/{}.py '{}'".format(argv[0], argv[1]), shell=True)
subprocess.call("python challenges/{}.py {} {}".format(argv[1], argv[2], argv[3]), shell=True)