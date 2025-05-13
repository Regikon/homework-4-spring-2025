from random import choices
import string

def generate_random_string(n: int):
    return ''.join(choices(string.ascii_letters + string.digits, k=n))
