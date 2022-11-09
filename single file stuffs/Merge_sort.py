def Merge(a,b):
    a_pos= 0
    b_pos = 0
    output = []

    while a_pos < len(a) and b_pos < len(b):
        if a[a_pos] < b[b_pos]:
            output.append(a[a_pos])
            a_pos +=1
        else:
            output.append(b[b_pos])
            b_pos +=1 
    
    if a_pos == len(a):
        output = output+ b[b_pos::]
    else:
        output = output +a[a_pos::]
    return output

def half(_input):
    mid = len(_input)//2
    a = _input[mid:]
    b = _input[:mid]
    return (a,b)



list1 = [1,4,5,14]
list2 = [2,6,8,20]

print(Merge(list1,list2))