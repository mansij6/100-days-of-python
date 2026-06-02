def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(operation["*"](n1 =4, n2=8))

def calculator():
    should_accumalate = True
    num1 = float(input("what is the first number?:"))

    while should_accumalate:
      for symbol in operations:
        print(symbol)
      operations_symbol = input("pick an operations:")
      num2 = float(input("what is the second number?:"))
      answer = operations[operations_symbol](num1, num2)
      print(f"{num1} {operations_symbol} {num2}={answer}")

      choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")

      if choice == "y":
       num1 = answer
    else:
        should_accumalate = False
        print("\n" * 20)
        calculator()

calculator()



