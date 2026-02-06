def is_strong(password):
    if len(password) < 8:
        return False
    if password.islower() or password.isupper():
        return False
    if password.isalnum():
        return False
    return True
