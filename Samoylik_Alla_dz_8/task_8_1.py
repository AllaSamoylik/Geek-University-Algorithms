import hashlib
import random
import string


def get_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def count_substring(string):
    hash_substrings = set()
    for i in range(len(string)):
        for j in range(len(string), i, - 1):
            hash_substring = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            hash_substrings.add(hash_substring) if len(string[i:j]) != len(string) else None
    return len(hash_substrings)


n = int(input('Введите длину строки: '))
s = get_string(n)

print(f'В строке "{s}" {count_substring(s)} подстрок(и)')
