from art import logo

# PROPERTIES
def add(n1, n2): return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2): return n1 / n2


# METHODS
def calculate():
    ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    calculator_is_in_use = True

    while calculator_is_in_use:
        operation_is_in_progress = True
        n1 = float(input("What's the first number? "))
        
        for op in ops:
            print(op)

        while operation_is_in_progress:
            op = input("Choose an operation: ")

            if op not in list(ops.keys()):
                print(f"ERROR: {op} is not a valid operation")
                continue

            n2 = float(input("What's the next number? "))
            calc = ops[op]
            answer = calc(n1, n2)

            print(f"{n1} {op} {n2} = {answer}")

            if input("Continue operating? (y/n) ").lower() == "y":
                n1 = answer
            else:
                operation_is_in_progress = False

        if input("Perform another calculation? (y/n) ").lower() != "y":
            calculator_is_in_use = False


# MAIN
print(logo)
calculate()
