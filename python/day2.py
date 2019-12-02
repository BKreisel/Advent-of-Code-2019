from enum import Enum
from io import TextIOBase
import sys

class Opcodes(Enum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99

def main(fd: TextIOBase):
    program = [int(x) for x in fd.readline().split(",")]
    eip = 0

    while(program[eip] != Opcodes.HALT.value):
        arg1 = program[eip + 1]
        arg2 = program[eip + 2]
        dest = program[eip + 3]

        if program[eip] == Opcodes.ADD.value:
            program[dest] = program[arg1] + program[arg2]
        elif program[eip] == Opcodes.MULTIPLY.value:
            program[dest] = program[arg1] * program[arg2]
        eip += 4
        
    print(",".join(map(str,program)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
       sys.exit(1) 
    with open(sys.argv[1], 'r') as fd:
        main(fd)