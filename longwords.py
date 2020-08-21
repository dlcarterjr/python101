#When given an English word with a long double same vowel, it prints the word with added same vowels.

word = input("Enter word: ").lower()  #Takes word input, converts to lower case.
text_out = ""
vowel_num = 0
for text_in in word:  #For loop iterates through each letter in word.
    

    #  These else/if statements checks for the three same-doubld vowels in word and adds the extra vowels.
    if text_in == "o":
        vowel_num += 1
        if vowel_num == 2:
            text_out += "ooo"
            vowel_num = 0
        else:
            text_out += text_in  
            
    
    elif text_in == "e":
        
        vowel_num += 1
        if vowel_num == 2:
            text_out += "eee"
            vowel_num = 0
        else:
            text_out += text_in

    elif text_in == "u":
        
        vowel_num += 1
        if vowel_num == 2:
            text_out += "uuu"
            vowel_num = 0
        else:
            text_out += text_in
              
    else:
        text_out += text_in
        vowel_num = 0
print(text_out.capitalize())  #Prints out final word(capitalized)