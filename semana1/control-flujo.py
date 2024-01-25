edad = 18

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

price = 500
has_card = True

if has_card:
    print(price - 100)
elif price < 1000:
    print(price - 50)
else:
    print(price - 10)

colors = ["Yellow", "Red", "Brown", "Black", "White"]
print("==== FOR IN ====")

for colorcito in colors:
    print(colorcito)

teams = [
    "Barcelona", 
    "Real Madrid", 
    "PSG", 
    "Otros equipos", 
    ["botella", "silla", "juego", "pantalla"]
]

things = teams[4]
for thing in things:
    print(thing)

print("==== RANGE ====")
numbers = range(11)
print(list(numbers))
print("-"*50)
numbers2 = range(10, 21)
print(list(numbers2))
print("-"*50)
numbers3 = range(20, 101, 5)
print(list(numbers3))
print("-"*50)

for number in range(1, 10):
    if number % 2 == 0:
        print(f"{number} es par")
    else:
        print(f"{number} es impar")