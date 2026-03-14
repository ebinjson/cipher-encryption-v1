#ord : - to convert string to ascii decimal
#chr : - to convert decimal to string


#text to decimal to text
word = input("Enter the word to encrypt: ")
length = len(word)
Ascii_arr = []
text_arr = []
for i in word:
    ascii_value = ord(i)
    new_ascii_value = ascii_value + 2 #key
    Ascii_arr.append(new_ascii_value)
for i in Ascii_arr:
    text = chr(i)
    text_arr.append(text)

msg = "".join(text_arr)
print(f"Encrypted message {msg}")
