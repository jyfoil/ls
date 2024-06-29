# You've been asked to implement a function called digit_product that t
# akes a string of digits as an argument and returns the product of all the digits in the string.

# When testing the function, you find that it returns 0, which is not what you expect. 
# Can you identify the issue and correct the code?

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    print(digits)

    for digit in digits:
        print(f'current digit: {digit}')
        product *= digit
        print(f'product: {product}')

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0