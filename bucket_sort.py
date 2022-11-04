def Counting_sort(data):
    # get the largest and the smallest value, aswell as the range
    big = max(data)
    smol = min(data)
    long = big-smol
    ## create the dump list with the required length
    dump = [0] * (long + 1)
    ## tally the list for numbers
    for b in data:
        dump[b-smol] += 1
    sorted = []
    ## re-create the list but in order
    for position in range(len(dump)):
        for i in range (0,dump[position]):
            sorted.append(position +smol)
    return sorted



stuff = [23,1,1,42,2,2,4,5,12312,6,7,6,4,5,6,9]
print(Counting_sort(stuff))