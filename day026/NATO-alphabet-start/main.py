import pandas
df=pandas.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
# for (index, row) in df.iterrows():
#     print(row.code)

# Keyword Method with iterrows()
#TODO 1. Create a dictionary in this format:
final = {row.letter : row.code for (index, row) in df.iterrows()}
#print(final)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Enter your word bruh!!!")
u = [i for i in user.upper()]
ans = []
for i in u:
    a = [value for (key, value) in final.items() if i == key]
    print(a, sep=" ", end="")