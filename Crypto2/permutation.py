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


def p4(part1: str, part2: str) -> list:
    """Applique la permutation P4 sur les résultats des sand-boxes.

    :param part1: Résultat de S0 (2 bits sous forme de chaîne).
    :param part2: Résultat de S1 (2 bits sous forme de chaîne).
    :return: Liste de 4 booléens représentant la permutation P4.
    """
    s00, s01 = part1  # Extraction des bits de S0
    s10, s11 = part2  # Extraction des bits de S1

    # Appliquer P4 : (s01, s11, s10, s00)
    return [s01 == '1', s11 == '1', s10 == '1', s00 == '1']

def initial_permutation(plaintext: str) -> str:
    """Applique la permutation initiale IP.

    :param plaintext: Une chaîne binaire de 8 bits représentant le texte clair.
    :return: Le texte permuté selon IP.
    """
    ip = [1, 5, 2, 0, 3, 7, 4, 6]  # Définition de la permutation IP
    return permute_bits(plaintext, ip)

def inverse_initial_permutation(permuted_text: str) -> str:
    """Applique la permutation inverse IP⁻¹.

    :param permuted_text: Une chaîne binaire de 8 bits après IP.
    :return: Le texte clair initial restauré.
    """
    ip_inverse = [3, 0, 2, 4, 6, 1, 7, 5]  # Définition de la permutation inverse IP⁻¹
    return permute_bits(permuted_text, ip_inverse)

def expansion_permutation(bits: str) -> str:
    """Applique l'opération d'expansion/permutation E/P sur 4 bits.

    :param bits: Une chaîne binaire de 4 bits.
    :return: Une chaîne binaire de 8 bits après l'expansion/permutation.
    """
    ep = [3, 0, 1, 2, 1, 2, 3, 0]  # Indices corrigés pour une indexation à 0 en Python
    return "".join(bits[i] for i in ep)


# Exemple d'utilisation
right_half = "1101"  # Exemple de 4 bits
expanded = expansion_permutation(right_half)

print(f"Entrée  : {right_half}")
print(f"Sortie E/P : {expanded}")  # Doit renvoyer 8 bits


# Exemple d'utilisation
plaintext = "110100il"
permuted = initial_permutation(plaintext)
restored = inverse_initial_permutation(permuted)

print(f"Texte clair : {plaintext}")
print(f"Après IP : {permuted}")
print(f"Après IP⁻¹ : {restored}")  # Doit être égal à plaintext


key = "1010000010"  # Clé initiale de 10 bits
permuted_key = P10(key)
print(f"Clé originale : {key}")
print(f"Clé après P10 : {permuted_key}")
