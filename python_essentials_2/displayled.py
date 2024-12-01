numberLEDS = [
    ['###', '# #', '# #', '# #', '###'], #0
    ['  #', '  #', '  #', '  #', '  #'], #1
    ['###', '  #', '###', '#  ', '###'], #2
    ['###', '  #', '###', '  #', '###'], #3
    ['# #', '# #', '###', '  #', '  #'], #4
    ['###', '#  ', '###', '  #', '###'], #5
    ['###', '#  ', '###', '# #', '###'], #6
    ['###', '  #', '  #', '  #', '  #'], #7
    ['###', '# #', '###', '# #', '###'],  #8
    ['###', '# #', '###', '  #', '###'], #9
    ]
def led_display():    
    user_numbers = input('Enter a number: ')
    try:
        n = int(user_numbers)
        for i in range(5):
            line = ''
            for l in user_numbers:
                line += numberLEDS[int(l)][i]
            print(line)
                
    except(ValueError):
        
        print('Input must be an integer')
        
led_display()
