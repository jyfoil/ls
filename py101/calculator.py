# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for the operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

# language = 'en'
# prompt(data[language]["introduction"])

while True:

    prompt('What language would you like to display?\n 1) en 2) es 3) fr')
    language = input()

    while language not in ['1', '2', '3']:
        prompt('You must choose en, es, or fr')
        language = input()

    if language == '1':
        language = 'en'
    elif language == '2':
        language = 'es'
    else:
        language = 'fr'

    prompt(data[language]["introduction"])

    # language function goes here

    prompt(data[language]["numbers"][0])
    number1 = input()

    while invalid_number(number1):
        prompt(data[language]["invalid"])
        number1 = input()

    prompt(data[language]["numbers"][1])
    number2 = input()

    while invalid_number(number2):
        prompt(data[language]["invalid"])
        number2 = input()

    prompt(data[language]["operation"])
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
        prompt(data[language]["operation_choice"])
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

    prompt(data[language]["result"] + str(output))
    prompt(data[language]["another_calculation"])
    decision = input()

    if decision and decision[0].lower() == 'n':
        break

