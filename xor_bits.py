def xor_bits(bits1: str, bits2: str) -> str:
    """Applique l'opération XOR bit à bit entre deux chaînes binaires.

    :param bits1: Première chaîne binaire.
    :param bits2: Deuxième chaîne binaire (de même longueur que bits1).
    :return: Résultat du XOR sous forme de chaîne binaire.
    """
    if len(bits1) != len(bits2):
        raise ValueError("Les deux chaînes binaires doivent avoir la même longueur.")

    # Appliquer XOR bit à bit
    result = ""
    for b1, b2 in zip(bits1, bits2):
        result += str(int(b1) ^ int(b2))  # XOR entre bits (int) puis conversion en str

    return result


# 🔹 Exemple d'utilisation :
bits_a = "11001100"
bits_b = "10101010"

result_xor = xor_bits(bits_a, bits_b)
print(f"{bits_a} ⊕ {bits_b} = {result_xor}")  # Résultat attendu : 01100110
