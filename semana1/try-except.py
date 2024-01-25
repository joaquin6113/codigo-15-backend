def dividir(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
    
print(dividir(10, 20))
print(dividir(50, 0))


def convertir_a_entero(text):
    try:
        return int(text)
    except ValueError as e:
        return f"ValueError: {e}"
    except Exception as e:
        return f"Error: {e}"

print(convertir_a_entero("123"))
print(convertir_a_entero(False))
print(convertir_a_entero("hola"))