def Counting_sort(data):
    big = max(data)
    smol = min(data)
    long = big-smol
    dump = [0] * (long + 1)
    ## tally the list for numbers
    for b in data:
        dump[b-smol] += 1
    sorted = []
    for position in range(len(dump)):
        for i in range (0,dump[position]):
            sorted.append(position +smol)
    return sorted



stuff = [1,1,1,2,2,3,1,2,3,1,2,3,1,4,1,5,1]
print (Counting_sort(stuff))