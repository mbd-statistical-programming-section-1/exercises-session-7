

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


#%%

def print_decreasing_range(number):
    
    for i in range(number, -1, -1):

        print(i)

#%%
        
def maximum(lst):
    
    current_max = -1
    
    for number in lst:
        
        if number > current_max:
            current_max = number
        
    return current_max






























