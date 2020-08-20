word = input("Enter word: ").lower()
text_out = ""
vowel_num = 0
for text_in in word:
    if text_in == "o":
        vowel_num += 1
        if vowel_num == 2:
            text_out += "ooo"
        else:
            text_out += text_in
    else:
        text_out += text_in

    if text_in == "e":
        vowel_num += 1
        if vowel_num == 2:
            text_out += "eee"
        else:
            text_out += text_in
    else:
        text_out += text_in
print(text_out)


#####   STILL WORKING ON THIS ONE ######