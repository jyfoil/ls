# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for the operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

language = 'en'

while True:

    prompt(messages('introduction', language))

    prompt(messages('numbers', language)[0])
    number1 = input()

    while invalid_number(number1):
        prompt(messages('invalid', language))
        number1 = input()

    prompt(messages('numbers', language)[1])
    number2 = input()

    while invalid_number(number2):
        prompt(messages('invalid', language))
        number2 = input()

    prompt(messages('operation', language))
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(messages('operation_choice', language))
        operation = input()

    # if operation == '1':
    #     output = int(number1) + int(number2)
    # elif operation == '2':
    #     output = int(number1) - int(number2)
    # elif operation == '3':
    #     output = int(number1) * int(number2)
    # elif operation == '4':
    #     output = int(number1) / int(number2)

    # Using match/case

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    prompt(messages('result', language) + str(output))
    prompt(messages('another_calculation', language))
    decision = input()

    if decision and decision[0].lower() == 'n':
        break
