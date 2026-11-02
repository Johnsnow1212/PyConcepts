items=[34,98,23,78,52,44,98,12,66,98]
def find_max(items):
    """Returns the max item of the list"""
    best=items[0]
    for i in items:
        if best<i:
            best=i
    return best
max=find_max(items) 
print(f"Maximum item: {max}")

def no_of_occurance(items):
    """Returns the no of Occurance"""
    count=0
    target=items[-1]
    for i in items:
        if target == i:
            count+=1
    return count
occurs=no_of_occurance(items)
print(f"No of Occurance of this item {occurs}")

