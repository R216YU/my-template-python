def get_random_feeling() -> str:
    """get a random feeling"""
    import random

    feelings = [
        "happy",
        "sad",
    ]

    return random.choice(feelings)
