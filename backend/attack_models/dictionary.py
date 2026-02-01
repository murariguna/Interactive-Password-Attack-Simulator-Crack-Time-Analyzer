def dictionary_attack(password):
    with open("data/common_passwords.txt", encoding="utf-8", errors="ignore") as f:
        common = f.read().splitlines()

    return password.lower() in common
