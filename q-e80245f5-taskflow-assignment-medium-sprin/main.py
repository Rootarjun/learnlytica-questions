import numpy as np

def estimate_summary(estimates):
    # TODO: non-list -> None
    if  estimates is None or not type(estimates).__name__=="list":
        return None
    
    # TODO: FILTER out None entries (unestimated tasks); non-numeric -> None

    
    for i in estimates:
        cond=not (type(i).__name__=="int" or type(i).__name__=="float")
        if cond:
            return None
            
    
    # TODO: empty (or all-None) -> {'total':0,'mean':0.0,'std':0.0,'min':0.0,'max':0.0}
    d={'total':0,'mean':0.0,'std':0.0,'min':0.0,'max':0.0}
    if not estimates:
        return d
    
    # TODO: build float array; return total(int), mean/std/min/max rounded to 2 dp
    d['total']=int(np.sum(estimates))
    d['mean']=round(np.mean(estimates),2)
    d['std']=round(np.std(estimates),2)
    d['min']=round(np.min(estimates),2)
    d['max']=round(np.max(estimates),2)

    
    return d

print(estimate_summary([1,2,3]))
print("hi")