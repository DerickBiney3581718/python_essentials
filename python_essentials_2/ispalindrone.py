from math import ceil

def is_palindrone(some_str:str):
    # two pointers from both ends
    # compare till start is greater than end 
    # falsify as soon as one comparison fails
    # if at end, true

    start = 0
    some_str= some_str.lower().replace(' ','')

    end = len(some_str) - 1
    list_range =  ceil(end / 2 )
    is_palindrone = True

    for i in range(list_range):
        # print('i:', i, ' start', some_str[i], some_str[end - i] )
        if not is_palindrone:
            break
        is_palindrone = some_str[i] == some_str[end - i]
    print('is a palindrone') if is_palindrone else print('not a palindrone')

list_ = [
    'Ten animals I slam in a net',
    'Eleven animals I slam in a net',
    'madam', 
]

for phr in list_:
    is_palindrone(phr)