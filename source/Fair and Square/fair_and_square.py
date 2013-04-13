import sys
import math
import itertools
import random

def is_palindrome(integer):
    strval = str(integer)

    return strval == strval[::-1]

def solve_one(rng):
    start, end = rng.split(" ")
    cnt = 0
    invalid_cnt = 0
    rng_start = int(math.ceil(math.sqrt(float(start))))
    rng_end = int(math.sqrt(float(end)))
    for length in xrange(len(str(rng_start)), len(str(rng_end))+1):
        lrange = lambda s, e: iter(itertools.count(s).next, e)
        mids = ("",) if not length&1 else [str(v) for v in range(0, 10)]
        for mid in mids:
            xrng = ("",) if length == 1 else lrange(10**((length / 2)-1), 10**((length/2)))
            for p in xrng:
                strval = str(p)
                val = int(strval+mid+strval[::-1])
                if val >= rng_start and val <= rng_end:
                    if is_palindrome(val**2):
                        cnt += 1
                    else:
                        invalid_cnt += 1
    return cnt

def solution(infilename, outfilename):
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")

    ranges = infile.read().strip().split("\n")[1:]

    results = [ solve_one(rng) for rng in ranges ]
    output = "\n".join(("Case #%d: %d"%(i+1, cnt) for i, cnt in enumerate(results)))
    outfile.write(output)
    outfile.write("\n")

    return True

def generate_sample(filename):
    outfile = open(filename, "w")
    for i in xrange(10000):
        start = random.randint(0, 10**100)
        end = random.randint(start, 10**100) 
        outfile.write("%d %d\n"%(start, end))

def main():
    solution(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
  main()
