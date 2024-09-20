# opgave 1
d1 = {
    "Navn": 	"Alice",
	"Alder": 	1997,
	"Højde": 	171,
	"Bopæl": 	"Vodskov",
	"Bruger_briller": "Nej"
}

d2= {
    "Navn":	"Bob",
	"Alder": "Ukendt",
	"Højde": 	180,
	"Bopæl": 	"Aalborg",
	"Bruger_briller": 	"Ja"
}

# opgave 2
print(d1["Alder"])
# opgave 3
print(d2["Alder"])

# opgave 4
print(len(d1))
print(len(d2))

# opgave 5
d2["Alder"] = 190

# opgave 6
for i in d1:
    print(d1[i])

for i in d2:
    print(d2[i])