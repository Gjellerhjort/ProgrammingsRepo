# main.py
import sys

if __name__ == "__main__":
    if len(sys.argv) == 0:
        exit()
    Base = float(sys.argv[1])
    Height = float(sys.argv[2])
    Areal = 1/2 * Base * Height
    print(f'Arealet er {Areal}')