alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
def encrypt(text, shift):
    fin = " "
    for i in text:
        posiition = alphabet.index(i)
        posiition = posiition+shift
        if posiition >= len(alphabet):
            posiition = posiition-len(alphabet)
        newword = alphabet[posiition]
        fin += newword
    print(fin)


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(text=text, shift=shift)

