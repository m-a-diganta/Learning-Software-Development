def min(*args):
    if not args:
        raise ValueError("At least one argument is required")
    min_value = args[0]
    for arg in args[1:]:
        if arg < min_value:
            min_value = arg
    return min_value