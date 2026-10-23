import pandas as pd
import numpy as np
def fill_missing_status(records):
    """records: list[dict] of task rows. Return a list of each row's status
    with MISSING statuses filled as "todo".
    Missing = None, NaN, an absent "status" key, or a blank/whitespace-only string.
    """
    if not records:
        return []
    for i in records:
        if not i.get('status'):
            i['status']=np.nan
        elif i["status"] is None:
            i["status"]=np.nan
        elif not i["status"].strip():
            i['status']=np.nan
    
    df = pd.DataFrame(records)
    # TODO: ensure a "status" column exists even if some/all rows lack it
    # TODO: treat blank / whitespace-only strings as missing
    # TODO: fill missing with "todo" and return df["status"].tolist()
    df=df.fillna("todo")
    return list(df['status'])

# print(len(fill_missing_status([{'id':1,'status':'done'},{'id':2,'status':'todo'}]))) 
#print(fill_missing_status([{'id':1,'status':'done'},{'id':2,'status':'todo'}])[0]) # → done

print(fill_missing_status([{'id':1,'status':'done'},{'id':2}])[1]) # → todo