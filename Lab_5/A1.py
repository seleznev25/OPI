def remove_parentheses(text: str) -> str:
    result = ""
    skip = 0
    for char in text:
        if char == "(":
            skip += 1
        elif char == ")" and skip > 0:
            skip -= 1
        elif skip == 0:
            result += char
    return result.strip()

# Пример
text = "Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (())."
print(remove_parentheses(text))
