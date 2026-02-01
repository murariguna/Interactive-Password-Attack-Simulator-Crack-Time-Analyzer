def rule_based(password):
    rules = [
        password.lower(),
        password.capitalize(),
        password.replace("a", "@").replace("o", "0")
    ]
    return password in rules
