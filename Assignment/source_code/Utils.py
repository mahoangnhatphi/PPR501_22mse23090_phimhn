def to_int_value(value):
    if value == '' or value is None:
        return None
    return int(value)

def is_best_seller(value):
    if not value:
        return False
    return True