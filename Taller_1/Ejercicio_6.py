#cilindro neumático de doble efecto.
import math
presion = 600000; # Pascales
Lvastago = 0.025; # metros
Lembolo = 0.1; # metros

# superficie del embolo
se= math.pi * math.pow((Lembolo / 2),2)

# superficie del Vastago
sv= math.pi * math.pow((Lvastago / 2),2)

#Principio de pascal P=F/S; F=P*S
# Fuerza de avance (F = P * A)
fuerzaa = presion * se

# Fuerza de retroceso (F = P * A)
fuerzar = presion * (se-sv)

print("Fuerza de avance: ", fuerzaa," N")
print("fuerza de retroceso ", fuerzar," N")