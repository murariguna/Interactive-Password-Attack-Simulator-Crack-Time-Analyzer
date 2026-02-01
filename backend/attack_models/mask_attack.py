def mask_reduction(password):
    reduction = 1.0

    if password[0].isupper():
        reduction *= 0.5
    if password[-1].isdigit():
        reduction *= 0.4
    if password[-1] in "!@#$":
        reduction *= 0.3

    return reduction

