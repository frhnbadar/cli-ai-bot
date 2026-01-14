INFO = "Evaluates math expressions safely"

def run(expr):
    if not expr:
        return "Usage: /tool calc <expression>"

    try:
        return str(eval(expr, {"__builtins__": {}}))
    except Exception:
        return "Invalid expression"
