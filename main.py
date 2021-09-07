alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(0, 2):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      if position + shift_amount > 25:
        shifted_letter = alphabet[(position-26)+shift_amount]
      else:
        shifted_letter = alphabet[position+shift_amount]
      cipher_text += shifted_letter
    print(f"The encoded text is: {cipher_text}")

  def decrypt(cipher_text, shift_amont):
    plain_text = ""
    for letter in cipher_text:
      position = alphabet.index(letter)
      shifted_letter = alphabet[position-shift_amont]
      plain_text += shifted_letter
    print(f"The decoded text is: {plain_text}")

  if direction == "encode":
    encrypt(text, shift)
  elif direction == "decode":
    decrypt(text, shift)
