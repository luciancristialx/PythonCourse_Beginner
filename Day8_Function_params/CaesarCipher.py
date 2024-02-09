import CaesarArt
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(CaesarArt.logo)
def caesar(user_text_input, user_shift_input, user_direction_input):
    end_text = ""
    if user_direction_input == "decode":
        user_shift_input *= -1
    for char in user_text_input:
        if char in alphabet:
            alphabet_index = alphabet.index(char)
            new_position = alphabet_index + int(user_shift_input)
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {user_direction_input}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decript:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(user_text_input = text,user_shift_input = shift, user_direction_input = direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if result == "no":
        should_continue = False
        print("Goodbye!")

# def encrypt(plain_text,shift_amount):
#     cypher_text = ""
#     for letter in plain_text:
#         alphabet_index = alphabet.index(letter)
#         new_position = alphabet_index + int(shift_amount)
#         new_letter = alphabet[new_position]
#         cypher_text += new_letter
#     print(f"The encoded text is {cypher_text}")
#
# def decrypt(cypher_text, shift_amount):
#     plain_text=""
#     for letter in cypher_text:
#         alphabet_index = alphabet.index(letter)
#         new_position = alphabet_index - int(shift_amount)
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded text in {plain_text}")
#
# if direction.lower() == "encode":
#     encrypt(plain_text = text, shift_amount = shift)
# elif direction.lower() == "decode":
#     decrypt(cypher_text = text, shift_amount = shift)
# else:
#     print("Invalid command")