def circular_left_shift(bits: str, shift: int) -> str:
    """Effectue un décalage circulaire à gauche sur une chaîne binaire.

    :param bits: Une chaîne binaire représentant les bits.
    :param shift: Nombre de positions à décaler vers la gauche.
    :return: La chaîne binaire après décalage circulaire.
    """
    length = len(bits)
    shift = shift % length  # Assure que le décalage ne dépasse pas la taille
    return bits[shift:] + bits[:shift]


# Exemple d'utilisation
bits = "10000"
shifted_bits = circular_left_shift(bits, 1)
print(f"Avant LS-1 : {bits}")
print(f"Après LS-1  : {shifted_bits}")
