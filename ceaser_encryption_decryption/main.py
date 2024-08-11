alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(texty, shifty):
    new_text = ""
    for i in range(len(texty)):
        new_text += alphabet[(alphabet.index(texty[i]) + shifty) % 26]
    return new_text


def decrypt(texty, shifty):
    new_text = ""
    for i in range(len(texty)):
        new_text += alphabet[(alphabet.index(texty[i]) - shifty) % 26]
    return new_text


print(f"Your encrypted message: {encrypt(text, shift)}")
print(f"Your original message: {decrypt(encrypt(text, shift), shift)}")
