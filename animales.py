@@ -0,0 +1,19 @@
# Lista de animales
animales = ["Perro", "Gato", "Conejo", "Loro", "Tortuga"]
edades = [5, 3, 2, 1, 10]

# Mostrar todos los animales
print("Animales y sus edades:")
for i in range(len(animales)):
    print(animales[i], ":", edades[i])

# Encontrar el animal más viejo
mas_viejo = max(edades)
pos = edades.index(mas_viejo)
print("\nEl animal más viejo es:", animales[pos], "con", mas_viejo, "años")

# Mostrar solo los que tienen más de 3 años
print("\nAnimales con más de 3 años:")
for i in range(len(animales)):
    if edades[i] > 3:
        print(animales[i], ":", edades[i])
