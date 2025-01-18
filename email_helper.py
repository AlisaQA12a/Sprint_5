import random
import string


def email_generator(length = 7):
    prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return prefix + '@mail.ru'
