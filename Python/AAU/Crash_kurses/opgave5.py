
class Person:
    def SetData(self):
        
        self.navn = input("navn: ")
        
        self.alder = int(input("alder: "))
        
        self.foedeby = input("fødeby: ")

        self.yndlingstal = int(input("yndlingstal: "))

    def PrintData(self):
        PrintString = f'Mit navn er {self.navn}, og jeg er {self.alder}. år. Jeg er født i {self.foedeby} og mit ynglingstal er {self.yndlingstal}.'
        print(PrintString)

PD = Person()

while True:
    print("1: Indsæt Data \n 2: Print Data")
    x = input(":")

    match x:
        case "1":
            PD.SetData()
        case "2":
            PD.PrintData()
        case _:
            exit()

