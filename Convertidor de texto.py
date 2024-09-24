# Convertidor de texto a mayúsculas, minúsculas o capitalizador.

print("Convertidor de texto a mayúsculas, minúsculas, capitalizar o poner en mayúscula cada palabra.")

texto = input("Ingresa el texto con el que deseas trabajar: ")
convertir_texto = int(input("¿Qué deseas hacer con tu texto: (Convertir a mayúsculas (1) / Convertir a minúsculas (2) / Capitalizar (3) / Poner en mayúscula cada palabra (4)?: "))

if convertir_texto == 1:
    print(texto.upper())
elif convertir_texto == 2:
    print(texto.lower())
elif convertir_texto == 3:
    print(texto.capitalize())
elif convertir_texto == 4:
    print(texto.title())
else:
    print("Ese número no está dentro de las opciones.")
