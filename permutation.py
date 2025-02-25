def permute_bits(bits: str, permutation: list) -> str:
    """Applique une permutation sur une chaîne de bits.

    :param bits: Une chaîne de bits (ex: "1010000010").
    :param permutation: Une liste d'indices indiquant le nouvel ordre.
    :return: La chaîne binaire permutée.
    """
    # Vérification de la longueur
    if len(bits) != len(permutation):
        raise ValueError("La longueur des bits doit correspondre à la permutation.")

    # Création de la nouvelle chaîne après permutation
    permuted_bits = ""
    for i in permutation:
        permuted_bits += bits[i]  # Ajoute chaque bit selon l'ordre de permutation

    return permuted_bits


def P10(key: str) -> str:
    """Applique la permutation P10 sur une clé binaire de 10 bits.

    P10 réorganise les bits selon l'ordre spécifié :
    P10 (k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) → (k3, k5, k2, k7, k4, k10, k1, k9, k8, k6)

    :param key: Une clé binaire de 10 bits sous forme de chaîne de caractères.
    :return: La clé permutée de 10 bits sous forme de chaîne.
    """
    if len(key) != 10 or not all(bit in "01" for bit in key):
        raise ValueError("La clé doit être une chaîne binaire de 10 bits.")

    # Indices de permutation (les indices Python commencent à 0)
    permutation_order = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]

    # Appliquer la permutation
    permuted_key = ''.join(key[i] for i in permutation_order)
    return permuted_key


# Exemple d'utilisation
key = "1010000010"  # Clé initiale de 10 bits
permuted_key = P10(key)
print(f"Clé originale : {key}")
print(f"Clé après P10 : {permuted_key}")
