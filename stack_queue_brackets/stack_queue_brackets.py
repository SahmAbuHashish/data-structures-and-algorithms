def validate_brackets(string):
    stack = []
    brackets_map = {"(": ")", "[": "]", "{": "}"}

    for char in string:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            last_open_bracket = stack.pop()
            if brackets_map[last_open_bracket] != char:
                return False

    return len(stack) == 0



print(validate_brackets("()"))  # True
print(validate_brackets("[]"))  # True
print(validate_brackets("{}"))  # True
print(validate_brackets("(]"))  # False
print(validate_brackets("([)]"))  # False
print(validate_brackets("{[()]}"))  # True