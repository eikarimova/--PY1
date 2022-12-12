from random import sample
from string import ascii_uppercase, ascii_lowercase, ascii_letters


def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    n = 8
    allowed_alphabet = (ascii_uppercase, ascii_lowercase, ascii_letters)
    alphabet = ''.join(allowed_alphabet)
    return ''.join(sample(alphabet, n))


random_password = get_random_password()
print(''.join(random_password))
