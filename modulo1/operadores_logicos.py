# OPERADORES LÓGICOS
# and (True when all true) 
# or (True when at least one true)
# not (Inverts boolean value)

number1 = 10.4
number2 = 33.4

result = (
    (number1 == number2 and True) # False
    and (number1 < 100)
    and (number2 < 100)
    or (number1 > 100 and number2 > 200)
)
print(result)