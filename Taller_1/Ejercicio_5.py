# Funciones las rotaciones en X, Y y Z entrada angulo salida matriz 
import numpy as np
import math
def RX(Angulo):
    h=math.radians(Angulo)    
    u= np.array([ [1, 0, 0],[0, math.cos(h),  -math.sin(h)],[0, math.sin(h), math.cos(h)],])
    j=np.rint(u)
    return j
print(RX(90))

def RZ(Angulo):
    h=math.radians(Angulo)    
    u= np.array([ [ math.cos(h),  -math.sin(h),0],[ math.sin(h), math.cos(h),0,],[0, 0, 1],])
    j=np.rint(u)
    return j

def RY(Angulo):
    h=math.radians(Angulo)    
    u= np.array([[ math.cos(h),0,  math.sin(h)], [0, 1, 0],[ -math.sin(h),0, math.cos(h)],])
    j=np.rint(u)
    return j
print(RY(0))

print("Rotacion X")
print(RX(90))
print("Rotacion Y")
print(RY(0))
print("Rotacion Z")
print(RZ(-90))