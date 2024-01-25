from django.db import models


class Subscription(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.IntegerField(null=True)
    description = models.TextField() # Para textos más largos
    created_at = models.DateTimeField(auto_now_add=True) # Solo primer valor
    updated_at = models.DateTimeField(auto_now=True)# Siempre último valor

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        db_table = "subscription" # Cambia el nombre


"""
Pasos para crear una tabla:
1: Crear la migración: Crea un archivo con el código necesario para crear
   la tabla (no la crea).

    python manage.py makemigrations subscription

2: Ejecutar la migración (se crea la tabla)

    python manage.py migrate subscription 
"""

"""
CharField: Para textos cortos/medianos
FloatField: Para decimales
TextField: Para textos largos
DateTimeField: Para la fecha y hora
"""