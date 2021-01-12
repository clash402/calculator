from art import logo
import os

# PROPERTIES
add = lambda n1, n2: n1 + n2
subtract = lambda n1, n2: n1 - n2
multiply = lambda n1, n2: n1 * n2
divide = lambda n1, n2: n1 / n2


# METHODS
def calculate():
  ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
  n1 = float(input("What's the first number? "))

  for op in ops:
    print(op)

  calculation_is_in_progress = True

  while calculation_is_in_progress:
    op = input("Choose an operation: ")

    if op not in list(ops.keys()):
      print(f"ERROR: {op} is not a valid operation")
      continue

    n2 = float(input("What's the next number? "))
    calc = ops[op]
    answer = calc(n1, n2)

    print(f"{n1} {op} {n2} = {answer}")

    will_continue_operating = input("Continue operating? (y/n) ").lower()

    if will_continue_operating == "y":
      n1 = answer
    else:
      calculation_is_in_progress = False
      will_repeat = input("Perform another calculation? (y/n) ").lower()

      if will_repeat == "y":
        # clear()
        calculate()


# MAIN
print(logo)
calculate()
