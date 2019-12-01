from math import floor
from io import TextIOBase
import sys

def calculate_fuel(mass: int):
    return floor(mass/ 3) - 2

def main(fd: TextIOBase):
    print(sum([calculate_fuel(int(x.rstrip())) for x in fd.readlines()]))
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
       sys.exit(1) 
    with open(sys.argv[1], 'r') as fd:
        main(fd)