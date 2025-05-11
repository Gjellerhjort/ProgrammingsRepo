import argparse
import sys

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('--name', type=str)
parser.add_argument('--age', type=int)

args = parser.parse_args()

# takes command-line arguments a prints a string.
print(f"My name is {args.name} and i am {args.age} years old")