from permutation import permute_bits
from Shift_circular import circular_left_shift


def generate_subkeys(key_10bit: str):
    """Génère les sous-clés K1 et K2 à partir d'une clé principale de 10 bits.

    :param key_10bit: Une chaîne binaire de 10 bits.
    :return: Un tuple (K1, K2) contenant les sous-clés de 8 bits.
    """
    # Étape 1 : Appliquer p10
    p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    permuted_key = permute_bits(key_10bit, p10)

    # Étape 2 : Diviser en 2 parties de 5 bits
    left, right = permuted_key[:5], permuted_key[5:]

    # Étape 3 : Décalage circulaire gauche LS-1
    left = circular_left_shift(left, 1)
    right = circular_left_shift(right, 1)

    # Étape 4 : Appliquer p8 pour obtenir K1
    # Concaténer les deux parties et ne prendre que les 8 premiers bits
    left_right = left + right
    K1 = permute_bits(left_right[:8], [3, 0, 4, 1, 5, 2, 7, 6])  # Appliquer P8 à la chaîne de 8 bits

    # Étape 5 : Décalage circulaire gauche LS-2
    left = circular_left_shift(left, 2)
    right = circular_left_shift(right, 2)

    # Étape 6 : Appliquer p8 pour obtenir K2
    left_right = left + right
    K2 = permute_bits(left_right[:8], [3, 0, 4, 1, 5, 2, 7, 6])  # Appliquer P8 à la chaîne de 8 bits

    return K1, K2


# Exemple d'utilisation
key_10bit = "1010000010"
K1, K2 = generate_subkeys(key_10bit)
print(f"K1: {K1}")
print(f"K2: {K2}")