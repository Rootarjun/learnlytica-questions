import pandas as pd

def clean_tasks(records):
    """records: list[dict] messy task rows with keys:
    id, title, status, estimate_hours.
    Return a list of tidy dicts sorted ascending by id, where:
      - title  : stripped of surrounding whitespace
      - status : trimmed and lowercased
      - estimate_hours : float; non-numeric/missing -> 0.0; rounded to 2 dp
      - duplicate ids collapsed keeping the FIRST occurrence
    """
    if not records:
        return []
    df = pd.DataFrame(records)
    # TODO: clean title (str methods)
    df.title=df.title.apply(lambda x: x.strip())
    
    
    # TODO: normalize status (str methods)
    
    df.status= df.status.apply(lambda x: x.strip().lower())
    
    # TODO: coerce estimate_hours (dtype coercion) and fill missing with 0.0
    df.estimate_hours=pd.to_numeric(df.estimate_hours,errors='coerce').fillna(0.0)
    # TODO: drop_duplicates on id keeping first, sort by id
    df.sort_values(by="id",inplace=True)
    df=df.drop_duplicates(subset="id")
    print(df)
    out = []
    for i in range(len(df)):
      
      row=df.iloc[i]
      dic={}
      dic['id']=int(row['id'])
      dic['title']=str(row['title'])
      dic['status']=str(row['status'])
      dic['estimate_hours']=round(float(row['estimate_hours']),2)
      out.append(dic)
    # TODO: build list of dicts with native python types
    return out
  
print(clean_tasks([{'id':1,'title':'A','status':'todo','estimate_hours':'1'},{'id':2,'title':'A-dup','status':'done','estimate_hours':' '}]))