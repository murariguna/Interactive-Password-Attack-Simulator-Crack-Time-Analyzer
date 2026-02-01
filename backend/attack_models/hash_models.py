HASH_SLOWDOWN = {
    "plaintext": 1,
    "md5": 10,
    "sha1": 50,
    "sha256": 500,
    "bcrypt": 10**6,
    "argon2": 10**7
}

def hash_multiplier(hash_type):
    return HASH_SLOWDOWN.get(hash_type, 1)
