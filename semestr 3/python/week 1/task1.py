from decimal import *

def vat_invoice(l): return sum(l) * 0.23
def vat_receipt(l): return sum(i * 0.23 for i in l)

purchases = [1, 2, 3, 4, 5]
purchases2 = [0.2, 0.5, 4.59, 6]

print(vat_invoice(purchases) == vat_receipt(purchases))
print(vat_invoice(purchases2) == vat_receipt(purchases2), "\n")

print(vat_invoice(purchases), vat_receipt(purchases))               #Correct answer is 3.45
print(vat_invoice(purchases2), vat_receipt(purchases2), "\n\n")     #Correct answer is 2.5967

# Mathematically, both functions should return the same value but as the 2nd example shows, this is not always the case
# This is due to the nature of floating-point numbers and their imprecision
# The 2nd function returns a worse estimate because it tends to sum small numbers more frequently than the 1st one


def dec_invoice(l): return Decimal(str(sum(l))) * Decimal('0.23')
def dec_receipt(l): return sum(Decimal(str(i)) * Decimal('0.23') for i in l)

dec = [Decimal(i) for i in purchases]
dec2 = [Decimal(i) for i in purchases2]

print(dec_invoice(dec) == dec_receipt(dec))
print(dec_invoice(dec2) == dec_receipt(dec2), "\n")

print(dec_invoice(dec), dec_receipt(dec))       #Correct answer is 3.45
print(dec_invoice(dec2), dec_receipt(dec2))     #Correct answer is 2.5967

#When using the decimal arithmetic the results are much better.