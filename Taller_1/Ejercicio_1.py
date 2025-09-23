#producto punto y producto cruz
import numpy as np

nums1 = np.array([9,8,7])
nums2 = np.array([3,4,5])

#Operaciones
suma = nums1+nums2
resta = nums1-nums2
producto_p = nums1 * nums2
producto_c = np.cross(nums1, nums2)

print(f"Vector1: \n{nums1}")
print(f"Vector2: \n{nums2}")
print(f"Resultado de la suma de los vectores: \n{suma}")
print(f"Resultado de la resta: \n{resta}")
print(f"Resultado de producto punto: \n{producto_p}")
print(f"Resultado de producto cruz: \n{producto_c}")