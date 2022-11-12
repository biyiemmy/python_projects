from barcode import EAN13
from barcode.writer import ImageWriter

number_of_barcodes = int(input("How many barcodes, do you wanna generate? "))
numbers = range(number_of_barcodes)

for i in numbers:
    id = input("Kindly, drop your 12-digit numbers for the barcode id? ")
    my_code = EAN13(id, writer=ImageWriter)
    name = input("What do you wanna save it with? ")
    my_code.save(name)