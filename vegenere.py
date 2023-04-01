import pyfiglet as fig
print("\033[32m","="*100,"\033[m")
title = "Vigenere Cipher"
print("\033[32m",fig.figlet_format(title),"\033[m")
print(fig.figlet_format("Made by: Leoj M Suaverdez",font="bubble"))
# ==========================Function=============================
# Repeat the key until it became the same length as the raw_text
def repeat_word(key, raw_text):
    target_length = len(raw_text)
    repeated_word = key * target_length
    if len(raw_text)==len(key):
        return key
    elif len(raw_text)<len(key):
        return key[0:len(raw_text)]
    else:
        return repeated_word[0:len(raw_text)]
# =================================================================
# Ask User text and save it to variable, validate it to be uppercase letters with no spaces
while True:
    while True:
        plain_text = input("Enter your Text: ")
        if plain_text.isupper() and ' ' not in plain_text:
            break
        else:
            print("Invalid input! Please enter text in uppercase and with no spaces.")
    # Convert every letters in the text into numbers(0-25)
    initial_text = ""
    for letter in plain_text:
        initial_letter = ord(letter) - 65
        initial_text += str(initial_letter) + " "
    # Ask user for the key
    while True:
        key = input("Enter your key: ")
        if key.isupper() and ' ' not in plain_text:
            break
        else:
            print("Invalid input! Please enter text in uppercase and with no spaces.")
    # Convert every letters in the text into numbers(0-25)
    initial_key = ""
    repeated_key = repeat_word(key,plain_text)
    # print(repeated_key)
    for letter in repeated_key:
        initial_letter = ord(letter) - 65
        initial_key += str(initial_letter) + " "
    # Display it in a Row
    print(initial_text)
    print(initial_key)
    # Add two columns
    ciphered_text = ""
    for i in range(len(initial_text.split())):
        ciphered_num = (int(initial_text.split()[i]) + int(initial_key.split()[i])) % 26
        ciphered_letter = chr(ciphered_num + 65)
        ciphered_text += ciphered_letter
    # Print the Ciphered Text
    print("\033[41mCiphered Text: \033[m")
    print("\033[32m",ciphered_text,"\033[m")
    print("\033[32m","="*100,"\033[m")
    while True:
        response = str(input("Do you want to try again? [Y/N]"))
        if response == "N":
            print("Program will now Exit")
            exit()
        elif response == "Y":
            print("Encrypt a text again")
            break
        else:
            print("Invalid response. Please enter Y or N.")
