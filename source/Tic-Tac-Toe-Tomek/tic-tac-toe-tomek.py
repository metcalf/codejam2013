import sys
import numpy
import itertools

def check_row(row):
    if "O" in row and not "X" in row:
        return "O won"
    elif "X" in row and not "O" in row:
        return "X won"
    else:
        return None

def solve_one(board):
    try:
        board = numpy.array(board)
    except:
        print board
        raise
    spaces_remain = False

    for row in itertools.chain(board, board.transpose(), (numpy.diag(board), numpy.diag(numpy.flipud(board)))):
        if "." in row:
            spaces_remain = True
            continue
        res = check_row(row)
        if res:
            return res


    if spaces_remain:
        return "Game has not completed"
    else:
        return "Draw"

def solution(infilename, outfilename):
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")

    indata = infile.read().strip().split("\n",1)[1]
    boards = [ [list(row) for row in board.split("\n")] for board in indata.split("\n\n") ]
    for i, board in enumerate(boards):
        result = solve_one(board)
        outval = "Case #%d: %s"%(i+1, result)
        print outval
        outfile.write(outval)
        outfile.write("\n")

    return True

def main():
    solution(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
  main()
