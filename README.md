Code written as part of my school project. 

Caesar Cipher encryption algorithm v1.0!!

How it works?:
- Takes each character in the word
- Converts it to ASCII value using ord()
- Adds 2 to the ASCII value (key = 2)
- Converts back to character using chr()

(Basically the code shifts every letter on the give word by 2 positions!)

Some Weaknesses:
- It doesnt wrap around - 'y' --> '{' instead of 'a'
- Caeser Cipher is comparitably easy to crack --> only 25 possible keys.
- Code doesn't handle upper and lowercase separately
