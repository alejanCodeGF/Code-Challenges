# * Crea un programa que realize el cifrado César de un texto y lo imprima.
# * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
# *
# * Te recomiendo que busques información para conocer en profundidad cómo
# * realizar el cifrado. Esto también forma parte del reto.

# Consiste en sustituir cada letra del mensaje original por otra letra que se encuentre un número fijo de posiciones hacia la derecha en el alfabeto.
# Por ejemplo, si utilizamos un desplazamiento de 3, la letra "A" se sustituiría por la letra "D", la "B" por la "E", y así sucesivamente. Al llegar al final del alfabeto, se continúa desde el principio.
# ("HELLO" -> "KHOOR" con n=3)

# Por favor acentos no [>:-(]

def cifrado_cesar(text: str, n: int):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
    string_fin = ""

    n = n % len(letters)

    for letra_text in text:
        if letra_text.isalpha():
            pos_ini = letters.index(letra_text.upper())
            posfin = (pos_ini + n) % len(letters)
            if letra_text in letters:
                string_fin += letters[posfin]
            else:
                string_fin += letters[posfin].lower()
        else:
            string_fin += letra_text
    return string_fin


def descifrado_cesar(texto: str, n: int):
    return cifrado_cesar(texto, -n)


# Ejemplo de uso
texto_original = "Hola, esto es un ejemplo de cifrado Cesar!"
desplazamiento = 12312986749817

texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print("Texto cifrado:", texto_cifrado)

texto_descifrado = descifrado_cesar(texto_cifrado, desplazamiento)
print("Texto descifrado:", texto_descifrado)
