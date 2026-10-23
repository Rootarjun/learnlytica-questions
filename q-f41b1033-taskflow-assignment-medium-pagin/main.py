import itertools


def paginate(items, size):
    """Lazily yield successive lists ('pages') of up to `size` items
    from the iterable `items`. If size <= 0, yield nothing.
    Hint: iter(items) + itertools.islice.
    """
    # TODO
    ''' if size>0 :
    
        for i in range(0,len(items),size):
            yield list(itertools.islice(items,i,i+size))
    else:
        yield None'''

    iterator=iter(items)

    if size<=0:
        return None
    while True:
        
        page= list(itertools.islice(iterator,size))
        if not page:
            return
        yield page


    
    

def find_first(events, status):
    """Return the 'id' of the first event whose 'status' matches,
    else None. Use next(<generator expression>, None).
    """
    # TODO
    if not events:
        return None
    it=iter(events)
    while(True):
        item=next(it,None)
        if item is None:
            break
        stat=item.get("status")
        id=item.get("id")
        if status==stat:
            return id
        
    return None

