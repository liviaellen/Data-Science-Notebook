# helpers/__init__.py
import random
import string

def generate_password(size):
    """Generate a random lowercase ASCII password of given size"""
    breakpoint()
    letters = string.ascii_lowercase

    return ''.join(random.choice(letters) for i in range(size))

if __name__ == '__main__':
    print(generate_password(10))
