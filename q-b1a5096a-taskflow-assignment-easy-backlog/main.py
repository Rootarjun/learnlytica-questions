import pandas as pd


def status_counts(records):
    # `records` is a list of task dicts. Do NOT read any file.
    if not records:
        return {}
    # 1. Build a DataFrame: df = pd.DataFrame(records)
    # 2. Count the 'status' column (value_counts) and return a plain dict
    #    {status: int_count}. Return {} when there are no records.
    df = pd.DataFrame(records)
    dic=dict(df['status'].value_counts())
    
    
    ## hard type_Cast to int 
    dic={i:int(dic[i]) for i in dic}
    return dic
#print(type(status_counts([{'status':'todo'},{'status':'done'},{'status':'todo'}])['todo']))