# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for the operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

while True:
    prompt('Welcome to Calculator!')

    prompt("What's the first number")
    number1 = input()

    while invalid_number(number1):
        prompt('Hmm... that doesn\'t look like a valid number')
        number1 = input()

    prompt("What's the second number")
    number2 = input()

    while invalid_number(number2):
        prompt('Hmm... that doesn\'t look like a valid number')
        number2 = input()

    prompt(f'{number1} {number2}')

    prompt("""What operation would you like to perform?
    1) Add 2) Subtract 3) Multiply 4) Divide""")
    operation = input()

    # if operation == '1':
    #     output = int(number1) + int(number2)
    # elif operation == '2':
    #     output = int(number1) - int(number2)
    # elif operation == '3':
    #     output = int(number1) * int(number2)
    # elif operation == '4':
    #     output = int(number1) / int(number2)

    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3, 4')
        operation = input()

    # Using match/case

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    prompt(f'The result is {output}')
    prompt(f"""Would you like to perform another calculation
    y/n""")
    decision = input()

    if decision and decision[0].lower() == 'n':
        break

