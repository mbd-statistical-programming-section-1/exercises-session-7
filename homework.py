

#%%

def zero_to_five_hundred():
    i = 0
    lst = []
    
    while i <= 500:
        lst.append(i)
        
        i += 1
        
    return lst

#%%
    
def sum_list(lst):
    acc = 0
    for number in lst:
        acc = acc + number
        
    return acc