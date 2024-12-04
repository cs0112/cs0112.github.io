
def merge(orig_l1: list, orig_l2: list) -> list:
    '''Version using list slicing, which is perhaps not as 
    efficient as the version from the notes; read both!
    
    The index version in the notes is _linear_ time in 
    the sum of the lengths, because each copy takes constant time
    '''    
    result = []
    l1 = list(orig_l1) # workspace
    l2 = list(orig_l2) # workspace

    while len(l1) > 0 or len(l2) > 0:
        if len(l1) == 0:
            result.append(l2[0]) 
            l2 = l2[1:] # copy l2, but without the 1st element 
            #? why not just return result + l2
        elif len(l2) == 0:
            result.append(l1[0])
            l1 = l1[1:]
            #? why not just return result + l1
        elif l1[0] > l2[0]:
            result.append(l2[0])
            l2 = l2[1:]
        else:
            result.append(l1[0])
            l1 = l1[1:]

    return result
