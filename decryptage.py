class SDES:

    def __init__(self, _key):
        #self.master_key = [False] * 10
        self.master_key = [char == '1' for char in _key]


    def p10(self, key):
        # Vérifier que la clé est bien de longueur 10
        if len(key) != 10:
            raise ValueError("La clé doit être composée de 10 bits.")

        # Permutation P10 : (k3, k5, k2, k7, k4, k10, k1, k9, k8, k6)
        permutation = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
        permuted_key = ''.join(key[i] for i in permutation)
        #permuted_key = [key[i] for i in permutation] => for the utilisation of true or false

        return permuted_key

        # Fonction de décalage circulaire à gauche
    def circularLeftShift(self, key, bits):
        # S'assurer que le nombre de bits est positif et normaliser avec le modulo
        bits = bits % len(key)

        # Effectuer le décalage circulaire à gauche
        shifted_key = key[bits:] + key[:bits]

        return shifted_key

        # Fonction P8
    def p8(self, key):
        # Permutation P8 : (k6, k3, k7, k4, k8, k5, k10, k9)
        permutation = [5, 2, 6, 3, 7, 4, 9, 8]
        permuted_key = [key[i] for i in permutation]

        return permuted_key

    # Fonction de génération des sous-clés
    def generateKeys(self, key):
        # Appliquer P10 sur la clé principale
        p10_key = self.p10(key)

        # Séparer en deux moitiés de 5 bits
        left = p10_key[:5]
        right = p10_key[5:]

        # Décalage circulaire de 1 bit pour K1
        left_shifted1 = self.circularLeftShift(left, 1)
        right_shifted1 = self.circularLeftShift(right, 1)

        # Combinaison pour K1
        combined1 = left_shifted1 + right_shifted1

        # Appliquer P8 pour obtenir K1
        k1 = self.p8(combined1)

        # Décalage circulaire de 2 bits supplémentaires (1+2 = 3) pour K2
        left_shifted2 = self.circularLeftShift(left_shifted1, 2)
        right_shifted2 = self.circularLeftShift(right_shifted1, 2)

        # Combinaison pour K2
        combined2 = left_shifted2 + right_shifted2

        # Appliquer P8 pour obtenir K2
        k2 = self.p8(combined2)

        # Retourner K1 et K2
        return [k1, k2]

