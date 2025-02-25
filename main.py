# This is a sample Python script.
from decryptage import SDES


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    message = str(input("Enter your message: ")).upper()
    key = str(input('Entrer une clee : ')).lower()
    sdes = SDES(key)

    #print(sdes.master_key)


    # Appliquer P10
    #permuted_key = sdes.p10(sdes.master_key) => for the utilisation of true or false
    permuted_key = sdes.p10(key)
    print("Après P10 :", permuted_key)


    # Séparer en deux moitiés de 5 bits
    left = permuted_key[:5]
    right = permuted_key[5:]

    # Appliquer le décalage circulaire à gauche de 1 bit
    left_shifted = sdes.circularLeftShift(left, 1)
    right_shifted = sdes.circularLeftShift(right, 1)
    print("Après décalage circulaire :", left_shifted, right_shifted)

    # Génération des sous-clés
    subkeys = sdes.generateKeys(key)
    print("K1 :", subkeys[0])
    print("K2 :", subkeys[1])


    # Appliquer la permutation IP
    permuted_text = sdes.ip(message)
    print("Après IP :", permuted_text)

    # Appliquer la permutation inverse IP-1
    reversed_text = sdes.rip(message)
    print("Après IP-1 :", reversed_text)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
