

replace = {"computer": "body",
           "hacked": "infected with influenza",
           "hacking": "influenza",
           "hacker": "virus",
           "software": "medicine"
           }

fileName = "how_to_know_if_youve_been_hacked.txt"

newText = []

with open(fileName) as file:
    for line in file:
        for src, target in replace.items():
            line = line.lower().replace(src, target)
        newText.append(line)
        
with open(fileName, "w") as fileOut:
    for line in newText:
        fileOut.write(line)