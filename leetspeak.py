
text_in = input("Enter text to be translated. ")   #input the string to translate
text_in = text_in.upper()   #converts input to all uppercase
text_out = ""
for chars in (text_in):   #loops through each letter in the string and replaces relevant characters.
    if chars == "A":
        chars = "4"
        text_out = text_out + chars
    elif chars == "E":
        chars = "3"
        text_out = text_out + chars
    elif chars == "G":
        chars = "6"
        text_out = text_out + chars
    elif chars == "I":
        chars = "1"
        text_out = text_out + chars
    elif chars == "O":
        chars = "0"
        text_out = text_out + chars
    elif chars == "S":
        chars = "5"
        text_out = text_out + chars
    elif chars == "T":
        chars = "7"
        text_out = text_out + chars
    else:
        text_out = text_out + chars
print(text_out)   #prints out final string with replaced characters.