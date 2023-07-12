def sort_the_dict(array):
    newarr = [] # 12
    while len(array)!=0: # true
        max1 = array[0] # 12
        for number in array[1:]:
            if number>max1: # true
                max1 = number # 23
        newarr.append(max1)
        array.remove(max1)
    return newarr
                
            
# []