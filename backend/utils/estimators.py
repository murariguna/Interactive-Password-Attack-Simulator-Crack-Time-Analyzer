ATTACKER_SPEEDS = {
    "cpu": 10**6,
    "gpu": 10**9,
    "botnet": 10**11
}

def estimate_time(combinations, attacker):
    speed = ATTACKER_SPEEDS.get(attacker, 10**6)
    seconds = combinations / speed

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"
