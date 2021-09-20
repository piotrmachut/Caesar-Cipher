from ascii import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_amount, user_direction):
  output_text = ""
  if user_direction == "decode":
    shift_amount *= -1
  for character in input_text:
    if character in alphabet:
      position = alphabet.index(character)
      new_position = position + shift_amount
      output_text += alphabet[new_position]
    else:
      output_text += character
  print(f"The {user_direction}d text is: {output_text}")

print(logo)

app_exit = False
while not app_exit:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(text, shift, direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    app_exit = True
    print("Goodbye!")
