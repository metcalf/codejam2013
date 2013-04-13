import sys
import math

def is_palindrome(integer):
    strval = str(int(integer))
    return strval == strval[::-1]

def solution(infilename, outfilename):
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")

    ranges = infile.read().strip().split("\n")[1:]
    
    for i, rng in enumerate(ranges):
        start, end = rng.split(" ")
        cnt = 0
        for possible in range(int(math.ceil(math.sqrt(float(start)))), int(math.sqrt(float(end)))+1):
            if is_palindrome(possible) and is_palindrome(possible**2):
                cnt += 1
        outval = "Case #%d: %d"%(i+1, cnt)
        print outval
        outfile.write(outval)
        outfile.write("\n")

    return True

def main():
    solution(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
  main()
