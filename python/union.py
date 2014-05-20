# Takes two lists and modifies the first to be the union of both

#union.union(list1,list2)
def union(a,b):
    
    for i in b:
        if  i not in a:
            a.append(i)
    a.sort
        
    return