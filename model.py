
def calc_it(a, op, b):
    if op == "+":
        return f" {a} + {b} = {(int(a) + int(b))}"
    if op == "-":
        return f" {a} - {b} = {(int(a) - int(b))}"
    if op == "*":
        return f" {a} * {b} = {(int(a) * int(b))}"
    if op == "/":
        return f" {a} / {b} = {(int(a) / int(b))}"


