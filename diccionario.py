# trabajando con Diccionarios en Python
from pprint import pprint

# 1. Crear un Diccionario
informacion_personal = {
    "nombre": "Edwin Armijos",
    "edad": 18,
    "ciudad": "Loja",
    "profesion": "Ingeniera de Sistemas"
}

print("Diccionario original:")
pprint(informacion_personal)
print("\n")

# 2. Acceder y Modificar Valores
# Acceder y modificar la ciudad
print(f"Ciudad original: {informacion_personal['ciudad']}")
informacion_personal["ciudad"] = "Guayaquil"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Nota: La tarea menciona agregar "profesion", pero ya existe en el diccionario original,
# así que agregaré "hobbies" como ejemplo de agregar una nueva clave-valor
informacion_personal["hobbies"] = ["programación", "música", "futbol"]
print("\nDiccionario después de modificar ciudad y agregar hobbies:")
pprint(informacion_personal)
print("\n")

# 3. Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+094 5934 444"
    print("Se ha agregado un número de teléfono")
else:
    print("El teléfono ya existía en el diccionario")

print("\nDiccionario después de verificar y agregar teléfono:")
pprint(informacion_personal)
print("\n")

# 4. Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("Se elimina la clave 'edad'")

print("\nDiccionario después de eliminar la edad:")
pprint(informacion_personal)
print("\n")

# 5. Imprimir el Diccionario Final
print("Diccionario final después de todas las operaciones:")
pprint(informacion_personal)