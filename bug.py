def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
except TypeError:
    return "Invalid input type"

# This will trigger the uncommon TypeError
result = function_with_uncommon_error(5, "hello")
print(result)