import sys
import numpy

def solve_one(lawn):
    lawn = numpy.array(lawn)
    height, width = lawn.shape
    for i in range(height):
        row = lawn[i,:]
        for j in range(width):
            val = lawn[i,j]
            col = lawn[:,j]
            if val < max(row) and val < max(col):
                return False

    return True

def solution(infilename, outfilename):
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")

    line = infile.readline()
    lawns = []
    while line:
        try:
            line = infile.readline()
        except:
            break
        if not line:
            break
        rows = int(line.split(" ")[0])
        lawns.append([ [ int(entry) for entry in infile.readline().split(" ")] 
                       for i in range(rows) ])

    for i, lawn in enumerate(lawns):
        outval = "Case #%d: %s"%(i, "YES" if solve_one(lawn) else "NO")
        print outval
        outfile.write(outval)
        outfile.write("\n")

    return True

def main():
    solution(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
  main()
