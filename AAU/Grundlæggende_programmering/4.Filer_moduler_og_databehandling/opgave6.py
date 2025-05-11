import pandas as pd


# opgave 6.1

# Opret en ordbog med dataene
data = {
    "Fødselsdato": ["24/12/2001", "02/02/1998", "12/11/1999", "31/01/2003", "07/08/2000"],
    "By": ["Randers", "Åbybro", "Aalborg", "Nibe", "Aalborg"],
    "Køn": ["Mand", "Mand", "Kvinde", "Kvinde", "Mand"],
}

# Navnene bruges som indeks
index = ["Arne Andersen", "Bob Bertelsen", "Charlie Carlsen", "Dorthe Damsgaard", "Emil Ebbehøj"]

# Opret DataFrame med navnene som indeks
df = pd.DataFrame(data, index=index)

# opgave 6.2
print(df.columns)

# opgave 6.3
print(df.loc["Dorthe Damsgaard"])

# opgave 6.4
df["Børn"] = [1,0,2,0,0]
print(df)

# opgave 6.5

kvinder = df[df["Køn"] == "Kvinde"]

print(kvinder)
# opgave 6.6
