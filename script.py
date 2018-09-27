# custom script file.
# takes in argument and runs
import sys
import subprocess
import glob
import os


# Create script to run challenges with user arguments. 
# Day 1
subprocess.call("python challenges/q1.py 'arg1'", shell=True)