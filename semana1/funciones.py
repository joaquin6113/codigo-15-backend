print("==== FUNCIONES ====")

def saludar(name):
    print(f"Hola me llamo {name}")

saludar("Joaquín")

def sumar(n1=0, n2=0):
    print(f"n1 {n1}, n2 {n2}")
    return n1 + n2

print(sumar(30, 15))
print(sumar(n2=10, n1=20))

def saludar2(nombre, apellido, edad):
    print(f"Hola me llamo {nombre} {apellido} y tengo {edad} año(s)")
saludar2("Joaquín", "Guevara", 17)
saludar2(apellido="Al", edad=17, nombre="Le")

print("-"*50)
print("==== ARGS ====")

def average(*notas):
    print(notas)
    suma = 0
    for nota in notas:
        suma += nota
    print(suma / len(notas))

average(10, 20, 15, 17, 12, 15)
average(18)

print("-"*50)
print("==== Kwargs ====")

def persona(**datos):
    print("====KEYS====")
    for keys in datos.keys():
        print(keys)
    
    print("====VALUES====")
    for values in datos.values():
        print(values)
    
    print("====ITEMS====")
    for key, value in datos.items():
        print(key, value)


persona(
    name="Joaquín",
    lastname="Guevara",
    phone_number=9895724895215789619,
    dni=12387632,
    age=17,
    is_developer="maso"
)