from itertools import groupby
from sys import getsizeof

#itertools.groupby groups elements from the iterable by a given criterium and returns a dictionary-like object
#If criterium is not provided, it defaults to an identity function
#It generates a new group every time the value of a key changes, so it considers the order of the elements
#In a nutshell it groups neighbouring elements that match the same criterium together
#Python's string is a iterable so we don't need to convert it into an array
def encode(s): return [(ch, len(list(chs))) for ch, chs in groupby(s)]
def decode(encoded): return "".join(ch * chs for ch, chs in encoded)

print(encode("suuupeeeerr"))
print(decode(encode("suuupeeeerr")))
print()

#I included the text file (example.txt) in skos, it's "Dagon" by H.P. Lovecraft
#Taken from https://www.hplovecraft.com/writings/texts/fiction/d.aspx
with open("example.txt", encoding = "utf-8") as f: lovecraft = f.read()
lvc = encode(lovecraft)
print(len(lvc), len(lovecraft))             #Compressing an actual text doesn't make a considerable difference in its length
print(getsizeof(lvc), getsizeof(lovecraft)) #In fact, compressed text takes way more memory than plaintext
#print(lvc)
#print(decode(lvc))
print(decode(lvc) == lovecraft)