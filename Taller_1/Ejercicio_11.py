# Con interacción de consola
# ¿Desea continuar Si/No?

print("\n**** Desea continuar Si/No ****")

respuesta = "si"


while respuesta == "si":
    respuesta = input("\n¿Desea contisinuar? (Si/No): ").lower()
    print(respuesta)
    if respuesta!="si":
        if respuesta=="no":
            break
        else:
            print("Ingrese una opcion validas")
            respuesta = "si"
    else:
        respuesta = "si"