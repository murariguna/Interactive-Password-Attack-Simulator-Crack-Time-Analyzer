def hybrid_attack(password):
    base = password.lower().strip("1234567890!@#$")
    return base != password and len(base) > 3
