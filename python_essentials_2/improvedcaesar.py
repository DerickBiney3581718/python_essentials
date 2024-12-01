def improved_caesar():
    text = input('Enter text: ')
    returned_text = ''
    
    entered_wrongly = True
    while entered_wrongly:
        stick = input('Enter stick from 1 to 25...')
        try:
            stick = int(stick)
            entered_wrongly = not(stick <= 25 and stick >= 1 )
        except(ValueError):
            continue
    for char in text:
        if not char.isalpha():
            returned_text += char
        elif(char.isupper()):
            newp = ord('A') + ((ord(char) + stick)  % ord('Z')) - 1 if (ord(char) + stick) > ord('Z') else (ord(char) + stick)
            returned_text += chr(newp)
        else:
            newp = ord('a') + ((ord(char) + stick)  % ord('z')) -1  if (ord(char) + stick) > ord('z') else (ord(char) + stick)
            returned_text += chr(newp)           

    print(returned_text)

improved_caesar()