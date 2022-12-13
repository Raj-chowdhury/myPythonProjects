mathematical_sign = ""

while mathematical_sign != "quit":
    mathematical_sign = input("Choose a mathematical sign: ").title()
    if mathematical_sign == "Quit":
        print("Powering off calculator...")
        break
    number1 = int(input("Choose a number: "))
    if mathematical_sign == "Exponent":
        number3 = int(input("What is the power you want for your number? "))
        print(number1 ** number3)
    elif mathematical_sign == "Square Root":
        print(number1 ** (1/2))
    elif mathematical_sign == "Cube Root":
        print(number1 ** (1/3))
    elif mathematical_sign != "Exponent" or "Square Root":
        number2 = int(input("Choose a second number: "))
        if mathematical_sign == "Multiplication":
            print(number1 * number2)
        elif mathematical_sign == "Division":
            print(number1 / number2)
        elif mathematical_sign == "Addition":
            print(number1 + number2)
        elif mathematical_sign == "Subtraction":
            print(number1 - number2)
        else:
            print("Sorry...You didn't give me a mathematical symbol.")
