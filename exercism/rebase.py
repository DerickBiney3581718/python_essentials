def rebase(input_base, digits, output_base):
    # if bases are same return digits
    validate_params(input_base, output_base, digits)
    if input_base == output_base:
        return digits
    base_10_digits =  to_base_10(input_base, digits)

    return  from_base_10(output_base,base_10_digits)
    
def validate_params(inp, out, digits):
    if inp < 2:
        raise ValueError('input base must be >= 2')
    if out < 2:
        raise ValueError('output base must be >= 2')
        
    if list(filter(lambda x : 0 > x or x >= inp,  digits)):
        raise ValueError('all digits must satisfy 0 <= d < input base')
    
def to_base_10(input_base, digits):
    """
    takes in digits and converts to base 10 using expansion method

    param digits: list holds digits from some base
    param input_base: int holds original base
    return list: holds base 10 digits
    """
    base_10_list =  [sum([ dig * input_base ** ind   for ind, dig in enumerate(reversed(digits))])]
    return base_10_list

def from_base_10(out_base, digits):
    """
    converts digits from base 10 using the division method

    param out_base: int - the base to convert to
    param digits: int -  digits to convert
    return out_digits: list - converted digits
    """
    try:
        digits = digits[0]
        out_digits = []
        # get the ge (greatest) of out_base
        ge = 0
        while out_base ** ge <= digits:
            ge += 1
        ge -= 1 
        print("ge", ge)
        while ge >= 0 :
            
            mul = digits // out_base ** ge
            out_digits.append(mul)
            digits -= (mul * out_base ** ge)
            ge -= 1
        print('out base', out_base, f": {out_digits}" )
        return out_digits if out_digits else [0]
    except:
        raise ValueError('Invalid digits given')
        

print(rebase(2, [1, 0, 1, 0, 1, 0], 10))
print(rebase(10, [0], 2))
print(rebase(2, [1, 0, 1], 10))
print( rebase(2, [1, 2, 1, 0, 1, 0], 10))