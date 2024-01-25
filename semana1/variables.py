name = "Joaquín" #string
lastname = "Guevara"
number1 = 10 #int
number2 = 100.123 #float
is_higher = True #bool
is_lower = False #bool

print(name, number1, number2)

print("Hola mi nombre es " + name + " " + lastname + ", saludos") #muy complejo :p
print(f"Hola mi nombre es {name} {lastname}, saludos")

print(name + " " + str(number1))
print(number1 + number2)

print("==== LISTAS ====")

teams = ["Barcelona", "Real Madrid", "PSG", "Otros equipos", ["botella", "silla", "juego", "pantalla"]]
print(teams)
print(teams[2])
print(teams[4][2])

print("-" * 50)
tv_shows = ["Spiderman", "The Big Bang Theory", "Moises"]
print(tv_shows)
tv_shows.append("Black Sails")
print(tv_shows)
tv_shows.append(["Breaking Bad", "Batman"])
print(tv_shows)

movies = ["Movie1", "Película2", "Otro_idioma3"]
tv_shows.extend(movies)
print(tv_shows)

tv_shows.remove("Spiderman")
print(tv_shows)
tv_shows.pop()
print(tv_shows)
tv_shows.pop(4)
print(tv_shows)
tv_shows[3].pop(0)
print(tv_shows)
print(tv_shows.index("Película2"))

print("-" * 50)
print("==== TUPLAS ====")

months = ("Enero", "Febrero", "Marzo")
print(len(months))
print(len("hola mundo")) #cuenta caracteres