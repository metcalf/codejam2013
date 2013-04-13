#!/usr/bin/env python2

import os
import stat
import sys
import shutil

from lib.helper import select_problem

def main():
    problem = select_problem()

    directory = "source/%s"%problem["name"]
    fname = "%s.py"%problem["name"].lower().replace(" ", "_")
    fpath = "%s/%s"%(directory, fname)
    
    print
    print "Initializing %s"%(problem["name"])

    if os.path.exists(directory):
        print "The problem directory already exists"
        sys.exit(1)
    
    os.makedirs(directory)
    shutil.copyfile("template.py", fpath)
    os.chmod(fpath, stat.S_IWUSR|stat.S_IRUSR|stat.S_IXUSR|
             stat.S_IRGRP|stat.S_IXGRP|stat.S_IROTH|stat.S_IXOTH)

    open("%s/__init__.py"%directory, "a").close()
    open("source/input/%s-sample-000"%problem["name"], "a").close()

if __name__ == '__main__':
  main()
