class SDES:
    """ Implémentation simplifiée de l'algorithme SDES. """

    # Définition des Sand-Boxes S0 et S1 sous forme de matrices 4x4
    S0 = [
        ["01", "00", "11", "10"],
        ["11", "10", "01", "00"],
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
    def permutation_p4(bits: str) -> str:
        """Applique la permutation P4 (indices : [1, 3, 2, 0])."""
        if len(bits) != 4:
            raise ValueError("L'entrée doit être une chaîne binaire de 4 bits.")
        return bits[1] + bits[3] + bits[2] + bits[0]  # (s01, s11, s10, s00)

    @staticmethod
    def sbox_lookup(bits: str, sbox: list) -> str:
        """Applique une sand-box (S0 ou S1) sur 4 bits pour renvoyer 2 bits."""
        if len(bits) != 4 or not all(bit in "01" for bit in bits):
            raise ValueError("L'entrée doit être une chaîne binaire de 4 bits.")

        row = int(bits[0] + bits[3], 2)  # Ligne = premier et dernier bit
        col = int(bits[1] + bits[2], 2)  # Colonne = deuxième et troisième bit

        return sbox[row][col]

    def function_f(self, bits: str) -> str:
        """Fonction F utilisant S0 et S1 suivie de P4."""
        if len(bits) != 8:
            raise ValueError("L'entrée doit être une chaîne binaire de 8 bits.")

        left, right = bits[:4], bits[4:]  # Séparation en deux blocs de 4 bits
        s0_output = self.sbox_lookup(left, self.S0)
        s1_output = self.sbox_lookup(right, self.S1)

        combined_bits = s0_output + s1_output  # Concaténation
        return self.permutation_p4(combined_bits)  # Appliquer P4

    @staticmethod
    def xor(bits1: str, bits2: str) -> str:
        """Effectue un XOR bit à bit entre deux chaînes binaires."""
        if len(bits1) != len(bits2):
            raise ValueError("Les deux chaînes doivent avoir la même longueur.")
        return "".join("1" if b1 != b2 else "0" for b1, b2 in zip(bits1, bits2))

    def fK(self, bits: str, key: str) -> str:
        """Applique la fonction fK avec une sous-clé K."""
        if len(bits) != 8 or len(key) != 4:
            raise ValueError("L'entrée doit être une chaîne binaire de 8 bits et K doit être de 4 bits.")

        left, right = bits[:4], bits[4:]  # Séparer en L et R
        right_xor_key = self.xor(right, key)  # R ⊕ K

        # 🛠 Correction ici : Ajouter `right` à `right_xor_key` pour obtenir 8 bits
        f_input = right + right_xor_key
        f_output = self.function_f(f_input)  # Appliquer F(R ⊕ K)

        left_new = self.xor(left, f_output)  # L' = L ⊕ F(R ⊕ K)

        return left_new + right


# 🚀 Exemple d'utilisation
sdes = SDES()

input_bits = "01001011"  # Exemple de 8 bits d'entrée
key = "1100"  # Exemple de sous-clé

output_f = sdes.function_f(input_bits)
output_fk = sdes.fK(input_bits, key)

print(f"Entrée F : {input_bits} → Sortie F : {output_f}")
print(f"Entrée fK : {input_bits}, Clé : {key} → Sortie fK : {output_fk}")
