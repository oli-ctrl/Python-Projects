def bubble_sort (data):
    finished = False
    while not finished:
        finished = True
        for position in range(0, len(data)-1):
            if data[position] > data [position+1]:
                hold = data[position]
                data[position] = data[position+1]
                data[position+1] = hold
                finished = False
    return data


stuff = [12314124123,23,42,2,2,4,5,41212,6,7,6,7,4,5,6,9]
print(bubble_sort(stuff))

