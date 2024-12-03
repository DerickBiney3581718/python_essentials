# areanagrams

def areanagrams():
    entered_phr:str = input('Enter two words here, separted by space:')
    [first, second] = entered_phr.lower().split(' ')
    print(first, second)
    are_anagrams = True

    if (len(first) != len(second)):
        print('not anagrams')
        return
    
    for ch in first:
        if ch not in second:
            are_anagrams = False
            break
    else:
        for ch in second:
            if ch not in first:
                are_anagrams= False
                break
    
    print('not anagrams') if not are_anagrams else print('Voici anagrams')
    


areanagrams()