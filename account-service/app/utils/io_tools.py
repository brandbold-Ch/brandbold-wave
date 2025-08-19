import random


def auto_select_avatar(avatar_file: bytes = None):
    if avatar_file is None:
        return f"avatar{random.randint(1, 5)}.jpeg"
