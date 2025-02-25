class SDES:
    """ Implémentation simplifiée de l'algorithme SDES. """

    # Définition des Sand-Boxes S0 et S1 sous forme de matrices 4x4
    S0 = [
        ["00", "00", "11", "10"],
        ["01", "10", "01", "00"],
        ["00", "10", "01", "11"],
        ["11", "01", "11", "10"]
    ]

    S1 = [
        ["00", "01", "10", "11"],
        ["10", "00", "01", "11"],
        ["11", "00", "01", "00"],
        ["10", "01", "00", "11"]
    ]

    @staticmethod
    def sbox_lookup(bits: str, sbox: list) -> str:
        """Applique une sand-box (S0 ou S1) sur 4 bits pour renvoyer 2 bits.

        :param bits: Chaîne binaire de 4 bits (ex: "0100").
        :param sbox: La sand-box utilisée (S0 ou S1).
        :return: Deux bits résultants après passage dans la sand-box.
        """
        if len(bits) != 4 or not all(bit in "01" for bit in bits):
            raise ValueError("L'entrée doit être une chaîne binaire de 4 bits.")

        row = int(bits[0] + bits[3], 2)  # Ligne = premier et dernier bit
        col = int(bits[1] + bits[2], 2)  # Colonne = deuxième et troisième bit

        return sbox[row][col]

# Exemple d'utilisation des sand-boxes
sdes = SDES()

bits_left = "0100"  # Exemple de 4 bits pour S0
bits_right = "1011"  # Exemple de 4 bits pour S1

s0_output = sdes.sbox_lookup(bits_left, SDES.S0)
s1_output = sdes.sbox_lookup(bits_right, SDES.S1)

print(f"Entrée S0 : {bits_left} → Sortie S0 : {s0_output}")
print(f"Entrée S1 : {bits_right} → Sortie S1 : {s1_output}")
