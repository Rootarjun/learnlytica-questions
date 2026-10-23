import numpy as np

def total_estimated_hours(estimates):
    # TODO: if estimates is not a list, return None
    if not type(estimates).__name__=="list":
        return None
    
    # TODO: if any entry is None or non-numeric, return None (never NaN)
    for i in estimates:
        if not (type(i).__name__=='int' or type(i).__name__=="float"):
            return None
    # TODO: empty list -> 0
    if not estimates:
        return 0
    # TODO: build a float NumPy array and return int(arr.sum())
    
    np_array=np.array(estimates,dtype='float')
    return int(np_array.sum())