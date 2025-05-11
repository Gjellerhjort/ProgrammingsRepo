import os

folder = "./opgave5/"

def removeAllFiles():
    for i in range(0, 1000):
        os.remove(f"number_{i:03d}.txt")

number = 0
def fileHighNumber():
    for i in range(0, 1000):
        with open(folder+f"number_{i:03d}.txt") as Infile:
            Readnumber = int(Infile.read())
            if number < Readnumber:
                number = Readnumber
                print(number)



print(number)
