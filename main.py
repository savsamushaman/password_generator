import secrets
import itertools
import random

collection = {
    'lower_case': [x for x in range(97, 123)],
    'upper_case': [x for x in range(65, 91)],
    'numbers': [x for x in range(48, 58)],
    'symbols': list(itertools.chain(range(32, 48), range(58, 65), range(91, 97), range(123, 127)))
}


def generate_password(length, upper=False, numbers=False, symbols=False):
    """Returns an arbitrary string with the specified characteristics"""
    if length < 5:
        return 'Unsafe password length'
    new_pass = list()
    base = []
    base.extend(collection['lower_case'])
    new_pass.append(secrets.choice(base))
    if upper:
        temp = collection['upper_case']
        base.extend(temp)
        new_pass.append(secrets.choice(temp))
    if numbers:
        temp = collection['numbers']
        base.extend(temp)
        new_pass.append(secrets.choice(temp))
    if symbols:
        temp = collection['symbols']
        base.extend(temp)
        new_pass.append(secrets.choice(temp))

    current_len = len(new_pass)
    while current_len < length:
        new_pass.append(secrets.choice(base))
        current_len += 1

    random.shuffle(new_pass)
    new_pass = [chr(elem) for elem in new_pass]
    return ''.join(new_pass)


if __name__ == "__main__":
    pass
