import numpy as np

dim = 2 #dimensiones
p_simplex = dim + 1 #numero de puntos en el simplex
alpha, gamma, pho, sigma = 1, 2, 0.5, 0.5 #ref, exp, contr, shrink
rango_inf, rango_sup = -50, 50 #rangos

def sacar_fitness(triangulo):
    fitness = np.apply_along_axis(np.sum, 1, triangulo**2)
    return fitness

triangulo = np.random.uniform(rango_inf, rango_sup, size=(dim+1, dim))
fitness = sacar_fitness(triangulo)

print(triangulo, fitness)

# Calcular el punto medio de los dos puntos mejor evaluados segun el fitness.
