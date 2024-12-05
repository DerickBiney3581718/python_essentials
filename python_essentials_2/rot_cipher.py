# def rotate(text, key):
#     new_text = ""
#     for letter in text:
#         if letter.isalpha():
#             change_case = False
#             if letter.isupper():
#                 change_case = True
#                 letter = letter.lower()
#             # % 
#             z_ord = ord('z')
#             a_ord = ord('a')
#             new_ord = ord(letter) + key
#             pos = ((new_ord) % (z_ord + 1)) + a_ord if new_ord > z_ord else new_ord
#             # print('pos and all', pos, key,z_ord,a_ord, new_ord, sep=':')
#             letter = chr(pos)
#             letter = letter.upper() if change_case else letter
#         new_text += letter
#     return new_text

chars = "abcdefghijklmnopqrstuvwxyz"


def rotate(text, key):
    newchars = chars[key:] + chars[:key]
    trans = str.maketrans(chars + chars.upper(), newchars + newchars.upper()) #* creating a translation table :)
    return text.translate(trans) #*translate each char using the table
            
print(rotate("a",2))