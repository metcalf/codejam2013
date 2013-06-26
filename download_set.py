#!/usr/bin/env python2

import os
import subprocess

from lib.helper import select_problem, select_io_set

def main():
    problem = select_problem()
    print
    io_set = select_io_set(problem)
    print "Using set %s from problem %s"%(io_set["name"], problem["name"])

    prefix = "%s-%s"%(problem["name"], io_set["name"])
    inputs = [i for i in os.listdir("source/input") if i.startswith(prefix)]
    if not inputs:
        idx = "000"
    else:
        latest = sorted(inputs)[-1]
        idx = "%03d"%(int(latest.split("-")[-1])+1)

    cmd = ["python", "gcj_download_input", "-f",
           problem["name"], io_set["name"], idx]
    subprocess.check_output(cmd)

    print "Input %s downloaded"%idx

if __name__ == '__main__':
    main()
