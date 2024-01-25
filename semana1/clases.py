class Person:
    def __init__(self, name, lastname, phone_number, age, dni):
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.age = age
        self.__dni = dni #es una variable privada

    def salute(self):
        print(f"Hello, my name is {self.name} {self.lastname}, my number is {self.phone_number} and I am {self.age} ")
        print("years old.")

    def get_fullname(self):
        return f"{self.name} {self.lastname}"

    def format_phone_number(self):
        return f"+51{self.phone_number}"

    def get_dni(self):
        return self.__dni


persona1 = Person("Pedro", "the Immortal", 123789, 89, "7123891")
persona1.salute()
persona1.phone_number = 1238922
persona1.salute()
print(persona1.format_phone_number())
print(persona1.get_dni())