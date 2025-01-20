ALPHABET = "abcdefghijklmnopqrstuvwxyz .,!?-_0123456789"
ALPHABET_SIZE = len(ALPHABET)

CHAR_TO_INDEX = {char: i for i, char in enumerate(ALPHABET)}
INDEX_TO_CHAR = {i: char for i, char in enumerate(ALPHABET)}

def intify(strword):
    word = strword.lower()
    number = 0
    for char in word:
        if char not in CHAR_TO_INDEX: raise ValueError(f"Caractère '{char}' non supporté.")
        number = number * ALPHABET_SIZE + CHAR_TO_INDEX[char]
    return number

def stingify(number):
    word = []
    while number > 0:
        number, remainder = divmod(number, ALPHABET_SIZE)
        word.append(INDEX_TO_CHAR[remainder])
    return ''.join(reversed(word))

def lst(n): return list(range(2, n, 1 if n <= 10 else n // 10)) if n > 2 else [1, 2]