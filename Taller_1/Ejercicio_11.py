# Con interacción de consola
# ¿Desea continuar Si/No?

print("\n**** Desea continuar Si/No ****")

respuesta = "si"

while respuesta == "si":
    respuesta = input("\n¿Desea continuar? (Si/No): ").lower()
    print(respuesta)
    if respuesta == "No" or respuesta == "nO" or respuesta == "NO" or respuesta == "no":
        respuesta = "no"
    else:
        respuesta = "si"