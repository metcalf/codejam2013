#!/usr/bin/env python2

from lib.helper import select_problem, select_io_set

import os
import sys
import subprocess

def main():
    problem = select_problem()
    print
    io_set = select_io_set(problem)
    print "Using set %s from problem %s"%(io_set["name"], problem["name"])

    prefix = "%s-%s"%(problem["name"], io_set["name"])
    outputs = [o for o in os.listdir("source/output") if o.startswith(prefix)]
    if not outputs:
        print "No outputs found for %s"%prefix
        sys.exit(1)
    latest = sorted(outputs)[-1]
    
    response = raw_input("Submit `%s` [y/N]? "%latest) 
    if response.lower() != "y":
        print "Cancelled"
        sys.exit(1)

    print "Committing code and output to git"

    cmd = ["git", "diff", "--cached"]
    try:
        if subprocess.check_output(cmd):
            print "Changes are already staged for commit, please commit manually"
            sys.exit(1)
    except subprocess.CalledProcessError:
        print "Couldn't git diff"
        sys.exit(1)

    cmd = ["git", "add", "source/%s"%problem["name"], "source/output/%s"%latest]
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        print "Failed to stage code for commit"
        sys.exit(1)

    cmd = ["git", "diff", "--cached"]
    try:
        if subprocess.check_output(cmd):
            cmd = ["git", "commit", "-m", "TEST Pre-submission commit for %s"%latest]
            try:
                subprocess.check_call(cmd)
            except subprocess.CalledProcessError:
                print "Failed to commit code"
                sys.exit(1)
        else:
            print "No changes to commit"
    except subprocess.CalledProcessError:
        print "Couldn't git diff"
        sys.exit(1)

    
    
    cmd = ["python", "gcj_submit_solution.py", 
           problem["name"], io_set["name"], latest.split("-")[-1]]
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        print "Failed to submit code"
        sys.exit(1)
           
    

if __name__ == '__main__':
  main()
