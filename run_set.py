#!/usr/bin/env python

import optparse
import os
import imp
import sys
import subprocess
import cProfile
import pstats

from lib.helper import select_problem, select_io_set

def main():
    parser = optparse.OptionParser(usage='%prog [options]')
    parser.add_option("-p", "--profile", action='store_true', dest="profile",
                      help="Run with profiler")
    parser.set_defaults(profile=False)

    options, args = parser.parse_args()

    problem = select_problem()
    print
    io_set = select_io_set(problem, allow_sample=True)
    print "Using set %s from problem %s"%(io_set["name"], problem["name"])

    module_name = problem["name"].lower().replace(" ", "_")
    solution_module = imp.load_source(module_name,
                                      "source/%s/%s"%(problem["name"],
                                                      module_name+".py"
                                                      ))

    prefix = "%s-%s"%(problem["name"], io_set["name"])

    inputs = [i for i in os.listdir("source/input") if i.startswith(prefix)]
    if not inputs:
        print "No inputs available!"
        sys.exit(1)
    latest_input = sorted(inputs)[-1]
    
    outputs = [o for o in os.listdir("source/output") if o.startswith(latest_input)]
    if not outputs:
        next_output = latest_input+"_000"
    else:
        latest_output = sorted(outputs)[-1]
        next_output = "%s_%03d"%(latest_input, int(latest_output.split("_")[-1])+1)
    
    inpath = "source/input/"+latest_input
    outpath = "source/output/"+next_output
    fxn = solution_module.solution
    if options.profile:
        prof = cProfile.Profile()
        res = prof.runcall(fxn, inpath, outpath)
        prof.dump_stats("profiles/%s"%next_output)
        s = pstats.Stats(prof)
        s.strip_dirs().sort_stats("cumulative").print_stats(20)
    else:
        res = fxn(inpath, outpath)

    if res:
        print "Completed successfully, output to %s"%next_output
    else:
        print "Run failed!"

if __name__ == '__main__':
  main()
