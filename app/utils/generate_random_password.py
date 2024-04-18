import random
import string


def generate_random_password(length=15):
    """
    Function for generate a new password
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
