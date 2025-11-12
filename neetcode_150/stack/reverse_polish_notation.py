def reverse_polish_notation_eval(s):
    stack = []
    result = 0
    operators = {"+", "*", "/", "-"}
    for ch in s:
        if ch not in operators:
            stack.append(int(ch))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if ch == "+":
                result = operand1 + operand2
            elif ch == "-":
                result = operand1 - operand2
            elif ch == "/":
                result = int(operand1 / operand2)
            else:
                result = operand1 * operand2
            stack.append(result)
    if stack:
        return stack[0]
    else:
        return 0
    

tokens = ["1","2","+","3","*","4","-"]
print(reverse_polish_notation_eval(tokens))

