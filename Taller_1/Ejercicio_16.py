import matplotlib.pyplot as plt

def LineaRecta(x0, y0, x1, y1):
    # Dibuja el vector
    plt.arrow(x0, y0, x1-x0, y1-y0, head_width=0.05, head_length=0.1, fc='orange', ec='orange')

opcion = int(input("\n¿Cuál nombre deseas?: \n\n1. Paola Vaquiro\n2. Sara Barreto\n3. Jeisson Avila\n"))

plt.figure()
plt.xlim(0, 45)
plt.ylim(-15, 15)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

if opcion == 1:
    # --- PAOLA ---
    # P
    LineaRecta(1, 1, 1, 9)
    LineaRecta(1, 9, 5, 9)
    LineaRecta(5, 9, 5, 5)
    LineaRecta(1, 5, 5, 5)
    # A
    LineaRecta(7, 1, 7, 9)
    LineaRecta(11, 1, 11, 9)
    LineaRecta(7, 9, 11, 9)
    LineaRecta(7, 5, 11, 5)
    # O
    LineaRecta(13, 1, 13, 9)
    LineaRecta(17, 1, 17, 9)
    LineaRecta(13, 9, 17, 9)
    LineaRecta(13, 1, 17, 1)
    # L
    LineaRecta(19, 1, 19, 9)
    LineaRecta(19, 1, 23, 1)
    # A
    LineaRecta(25, 1, 25, 9)
    LineaRecta(29, 1, 29, 9)
    LineaRecta(25, 9, 29, 9)
    LineaRecta(25, 5, 29, 5)

    # --- VAQUIRO ---
    # V
    LineaRecta(1, -2, 3, -9)
    LineaRecta(3, -9, 5, -2)
    # A
    LineaRecta(7, -9, 7, -2)
    LineaRecta(11, -9, 11, -2)
    LineaRecta(7, -2, 11, -2)
    LineaRecta(7, -5, 11, -5)
    # Q
    LineaRecta(13, -9, 13, -2)
    LineaRecta(17, -9, 17, -2)
    LineaRecta(13, -2, 17, -2)
    LineaRecta(13, -9, 17, -9)
    LineaRecta(15, -9, 18, -11)
    # U
    LineaRecta(19, -2, 19, -9)
    LineaRecta(23, -2, 23, -9)
    LineaRecta(19, -9, 23, -9)
    # I
    LineaRecta(25, -9, 29, -9)
    LineaRecta(27, -9, 27, -2)
    LineaRecta(25, -2, 29, -2)
    # R
    LineaRecta(31, -9, 31, -2)
    LineaRecta(31, -2, 35, -2)
    LineaRecta(35, -2, 35, -5)
    LineaRecta(31, -5, 35, -5)
    LineaRecta(31, -5, 35, -9)
    # O
    LineaRecta(37, -9, 37, -2)
    LineaRecta(41, -9, 41, -2)
    LineaRecta(37, -2, 41, -2)
    LineaRecta(37, -9, 41, -9)

elif opcion == 2:
    # --- SARA ---
    # S
    LineaRecta(1, 1, 5, 1)
    LineaRecta(1, 5, 5, 5)
    LineaRecta(1, 9, 5, 9)
    LineaRecta(1, 1, 1, 5)
    LineaRecta(5, 5, 5, 9)
    # A
    LineaRecta(7, 1, 7, 9)
    LineaRecta(11, 1, 11, 9)
    LineaRecta(7, 9, 11, 9)
    LineaRecta(7, 5, 11, 5)
    # R
    LineaRecta(13, 1, 13, 9)
    LineaRecta(13, 9, 17, 9)
    LineaRecta(13, 5, 17, 5)
    LineaRecta(17, 9, 17, 5)
    LineaRecta(13, 5, 17, 1)
    # A
    LineaRecta(19, 1, 19, 9)
    LineaRecta(23, 1, 23, 9)
    LineaRecta(19, 9, 23, 9)
    LineaRecta(19, 5, 23, 5)

    # --- BARRETO ---
    # B
    LineaRecta(1, -2, 1, -10)
    LineaRecta(1, -2, 5, -2)
    LineaRecta(1, -6, 5, -6)
    LineaRecta(1, -10, 5, -10)
    LineaRecta(5, -2, 5, -6)
    LineaRecta(5, -6, 5, -10)
    # A
    LineaRecta(7, -10, 7, -2)
    LineaRecta(11, -10, 11, -2)
    LineaRecta(7, -2, 11, -2)
    LineaRecta(7, -6, 11, -6)
    # R
    LineaRecta(13, -10, 13, -2)
    LineaRecta(13, -2, 17, -2)
    LineaRecta(17, -2, 17, -6)
    LineaRecta(13, -6, 17, -6)
    LineaRecta(13, -6, 17, -10)
    # R
    LineaRecta(19, -10, 19, -2)
    LineaRecta(19, -2, 23, -2)
    LineaRecta(23, -2, 23, -6)
    LineaRecta(19, -6, 23, -6)
    LineaRecta(19, -6, 23, -10)
    # E
    LineaRecta(25, -2, 25, -10)
    LineaRecta(25, -2, 29, -2)
    LineaRecta(25, -6, 29, -6)
    LineaRecta(25, -10, 29, -10)
    # T
    LineaRecta(31, -2, 35, -2)
    LineaRecta(33, -2, 33, -10)
    # O
    LineaRecta(37, -2, 37, -10)
    LineaRecta(41, -2, 41, -10)
    LineaRecta(37, -2, 41, -2)
    LineaRecta(37, -10, 41, -10)

elif opcion == 3:
    # --- JEISSON ---
    # J
    LineaRecta(1, 9, 5, 9)
    LineaRecta(3, 9, 3, 1)
    LineaRecta(1, 1, 3, 1)
    # E
    LineaRecta(7, 1, 7, 9)
    LineaRecta(7, 9, 11, 9)
    LineaRecta(7, 5, 11, 5)
    LineaRecta(7, 1, 11, 1)
    # I
    LineaRecta(13, 1, 17, 1)
    LineaRecta(15, 1, 15, 9)
    LineaRecta(13, 9, 17, 9)
    # S
    LineaRecta(19, 1, 23, 1)
    LineaRecta(19, 5, 23, 5)
    LineaRecta(19, 9, 23, 9)
    LineaRecta(19, 1, 19, 5)
    LineaRecta(23, 5, 23, 9)
    # S
    LineaRecta(25, 1, 29, 1)
    LineaRecta(25, 5, 29, 5)
    LineaRecta(25, 9, 29, 9)
    LineaRecta(25, 1, 25, 5)
    LineaRecta(29, 5, 29, 9)
    # O
    LineaRecta(31, 1, 31, 9)
    LineaRecta(35, 1, 35, 9)
    LineaRecta(31, 9, 35, 9)
    LineaRecta(31, 1, 35, 1)
    # N
    LineaRecta(37, 1, 37, 9)
    LineaRecta(41, 1, 41, 9)
    LineaRecta(37, 9, 41, 1)

    # --- AVILA ---
    # A
    LineaRecta(1, -10, 1, -2)
    LineaRecta(5, -10, 5, -2)
    LineaRecta(1, -2, 5, -2)
    LineaRecta(1, -6, 5, -6)
    # V
    LineaRecta(7, -2, 9, -10)
    LineaRecta(9, -10, 11, -2)
    # I
    LineaRecta(13, -10, 17, -10)
    LineaRecta(15, -10, 15, -2)
    LineaRecta(13, -2, 17, -2)
    # L
    LineaRecta(19, -10, 19, -2)
    LineaRecta(19, -10, 23, -10)
    # A
    LineaRecta(25, -10, 25, -2)
    LineaRecta(29, -10, 29, -2)
    LineaRecta(25, -2, 29, -2)
    LineaRecta(25, -6, 29, -6)

plt.show()