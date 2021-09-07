alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(0, 2):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(input_text, shift_amount, user_direction):
    output_text = ""
    if user_direction == "encode":
      for letter in input_text:
        position = alphabet.index(letter)
        if position + shift_amount > 25:
          shifted_letter = alphabet[(position-26)+shift_amount]
        else:
          shifted_letter = alphabet[position+shift_amount]
        output_text += shifted_letter
      print(f"The encoded text is: {output_text}")
    elif user_direction == "decode":
      for letter in input_text:
        position = alphabet.index(letter)
        shifted_letter = alphabet[position-shift_amount]
        output_text += shifted_letter
      print(f"The decoded text is: {output_text}")
  
  caesar(text, shift, direction)
