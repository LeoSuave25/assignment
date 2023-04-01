import pyfiglet as fig
print("\033[32m","="*100,"\033[m")
title = "Decryption Tool"
print("\033[32m",fig.figlet_format(title),"\033[m")
print(fig.figlet_format("Made by: Leoj M. Suaverdez",font="bubble"))
# User enter the encrypted text to decrypt
while True:
    encrypted_text = str(input("Enter the encrypted text: "))

    # Decrypt the input text by replacing each encrypted character with its original vowel
    decrypted_text = encrypted_text.replace("*","a") # Replace "*" with "a"
    decrypted_text = decrypted_text.replace("&","e") # Replace "&" with "e"
    decrypted_text = decrypted_text.replace("#","i") # Replace "#" with "i"
    decrypted_text = decrypted_text.replace("+","o") # Replace "+" with "o"
    decrypted_text = decrypted_text.replace("!","u") # Replace "!" with "u"

    # Print the decrypted text
    print("\033[32m",decrypted_text,"\033[m")
    print("\033[32m","="*100,"\033[m")
    while True:
        response = str(input("Do you want to try again? [Y/N]"))
        if response == "N":
            print("Program will now Exit")
            exit()
        elif response == "Y":
            print("Decrypt a text again")
            break
        else:
            print("Invalid response. Please enter Y or N.")
