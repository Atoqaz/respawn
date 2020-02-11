""" Restart script if it crashes, and exist when script finishes. 
    Use: respawn.py {script_name} {*args}
"""

from subprocess import Popen, PIPE, STDOUT
# from analysis.upload_openstreetmap import BASE_DIR
from datetime import datetime
import sys


def execute(filename):
    errcode = 1
    while errcode == 1:
        process = Popen("python " + filename, shell=False, stdout=PIPE, # stderr=STDOUT,
        universal_newlines=True)
        for stdout_line in iter(process.stdout.readline, ""):
            print(stdout_line)
        # process = Popen("python " + filename, shell=False, stdout=PIPE, stderr=PIPE)
        process.communicate()
        errcode = process.returncode
        print(f"errcode: {errcode} | Time: {datetime.now()}")
        process.wait()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        for i, inpt in enumerate(sys.argv[1:]):
            if i == 0:
                filename = inpt
                # filename = str(BASE_DIR.joinpath("scrape_geo_polygons.py"))
            else:
                filename += " " + inpt
    else:
        raise ValueError("No filename provided.")

    print(f"Starting {filename} \nTime: {datetime.now()}\n")
    execute(filename)
    print(f"Finished running {filename} \nTime: {datetime.now()}")
