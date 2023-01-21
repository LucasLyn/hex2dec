print("Hexadecimal to Decimal converter.\n")
print("Input a hexadecmal number and press enter.")
print("Inputting '0' will terminate the script.")
print("\n")

hex = input("Hex: ")

while hex != "0":
    dec = int(hex, base=16) # Converts from base16 to int (base10)
    print("Dec:", dec) # No space after string to line up the input and output
    print("")
    hex = input("Hex: ")

exit