# TODO-1: Import and print the logo from art.py when the program starts.
import art
import string
alphabet=[]
alphabet.extend(list(string.ascii_uppercase))
alphabet.extend(list(string.ascii_lowercase))
alphabet.extend(list(string.digits))
alphabet.extend(list(string.punctuation))
alphabet.extend(list(string.whitespace))
print(art.logo)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")




yOrN= input(str("Do you want to run the program? type yes or no"))



while yOrN =="Yes"or yOrN== "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    yOrN = input(str("Do you want to run the program? type yes or no"))











