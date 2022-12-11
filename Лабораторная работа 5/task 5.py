import random
import string


def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    n = 8
    allowed_alphabet = (string.ascii_uppercase, string.ascii_lowercase, string.ascii_letters)
    alphabet = ''.join(allowed_alphabet)
    return random.sample(alphabet, n)


random_password = get_random_password()
print(''.join(random_password))
