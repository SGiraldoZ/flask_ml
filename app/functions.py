import numpy as np

def is_float(s):
    try:
        float(s)
        return True
    except ValueError as e:
        return False

def floats_string_to_np_arr(floats_str):
    floats = np.array([float(x) for x in floats_str.split(',') if is_float(x)])
    return floats

print(floats_string_to_np_arr('1.2,      ,0,9,124.25'))

