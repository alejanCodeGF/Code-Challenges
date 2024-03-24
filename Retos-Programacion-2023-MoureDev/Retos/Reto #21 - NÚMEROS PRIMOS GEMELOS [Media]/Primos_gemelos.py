# Crea un programa que encuentre y muestre todos los pares de números primos
# gemelos en un rango concreto.
# El programa recibirá el rango máximo como número entero positivo.
#
# - Un par de números primos se considera gemelo si la diferencia entre
#   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#
# - Ejemplo: Rango 14
#   (3, 5), (5, 7), (11, 13)


def primo(n):  # Primo = solamente divisible por 1 y por él mismo
    divisores = 0
    if n > 0:
        for i in range(1, n+1):
            if n % i == 0:
                divisores += 1
        if divisores == 2:
            return True


def primo_gemelo(n_rango):
    l = []
    for i in range(n_rango-1):
        if primo(i) and primo(i+2):
            print(f"({i}, {i+2})")


primo_gemelo(10)
