class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return None
        removed = self.top.value
        self.top = self.top.next
        self.count -= 1
        return removed

    def peek(self):
        return None if self.is_empty() else self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count


# Validación de expresiones matemáticas (paréntesis balanceados)
def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


# Conversión de notación infija a postfija
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = Stack()

    for token in expression.split():
        if token.isnumeric():
            output.append(token)
        elif token in precedence:
            while (not stack.is_empty() and stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Eliminar '('

    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)


# Ejemplos
test_expression = "( 3 + 2 ) * ( 8 / 4 )"
print("Expresion balanceada:", is_balanced(test_expression))

test_infix = "3 + 5 * ( 2 - 8 )"
print("Notacion postfija:", infix_to_postfix(test_infix))