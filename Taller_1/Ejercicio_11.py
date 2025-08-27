# Con interacción de consola
# ¿Desea continuar Si/No?

print("\n**** Desea continuar Si/No ****")

respuesta = "Si"

while respuesta == "Si":
    respuesta = input("\n¿Desea continuar? (Si/No): ")
    if respuesta == "No" or respuesta == "nO" or respuesta == "NO" or respuesta == "no":
        respuesta = "No"
    else:
        respuesta = "Si"