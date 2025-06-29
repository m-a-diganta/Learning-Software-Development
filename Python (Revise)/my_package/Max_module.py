def max(*args):
    if not args:
        raise ValueError("max() arg is an empty sequence")
    max_value = args[0]
    for arg in args[1:]:
        if arg > max_value:
            max_value = arg
    return max_value
