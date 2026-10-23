import pandas as pd


def high_priority_titles(records):
    # `records` is a list of task dicts. Do NOT read any file.
    # 1. Build df = pd.DataFrame(records)
    
    # 2. Keep rows where priority == 'high' with a boolean mask
    # 3. Return the 'title' values as a plain list of strings ([] when none).
    if not records:
        return []
    df = pd.DataFrame(records)
    df1=df[df['priority']=='high']
    #print(df1)
    return list(df1['title'])
print(high_priority_titles([]))