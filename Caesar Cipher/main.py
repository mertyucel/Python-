import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

situation = True
while situation:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = (int(input("Type the shift number:\n"))) % 26 
  
  
  def caesar(text_function,shift_function,direction_function):
    
      text = ""
      if (direction_function == "decode"):
            shift_function *= -1
      for letter in text_function:
        if (letter in alphabet):
          position = alphabet.index(letter)        
          new_position = position + shift_function
          text += alphabet[new_position]
        else:
          text += letter
      print(f"The {direction_function}d text is {text}")
    
  caesar(text_function = text,shift_function = shift,direction_function 
       = direction)
  
  answer = input("Do you want to continue? :\n").lower()
  if (answer == "no"):
    print("Good bye :)")
    situation = False

