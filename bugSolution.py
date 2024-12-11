def function_with_uncommon_error(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Inputs must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return str(e)

#Corrected
result = function_with_uncommon_error(5, "hello")
print(result)

result = function_with_uncommon_error(5, 0)
print(result)

result = function_with_uncommon_error(5, 2)
print(result)