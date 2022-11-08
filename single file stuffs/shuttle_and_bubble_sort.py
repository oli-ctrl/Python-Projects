def shuttle_sort (data):
    finished = False
    while not finished:
        finished = True
        # normal bubble sort
        for position in range(0, len(data)-1):
            count += 1
            if data[position] > data [position+1]:
                hold = data[position]
                data[position] = data[position+1]
                data[position+1] = hold
                finished = False
        # bubble sort but backwards :O
        if not finished:
            for rev_position in range (len(data)-1,0):
                count += 1
                if data[rev_position] < data [rev_position-1]:
                    rev_hold = data[rev_position-1]
                    data[rev_position-1] = data[rev_position]
                    data[rev_position] = rev_hold
                    finished = False
    return data

def bubble_sort (data):
    finished = False
    while not finished:
        finished = True
        for position in range(0, len(data)-1):
            count_bub += 1
            if data[position] > data [position+1]:
                hold = data[position]
                data[position] = data[position+1]
                data[position+1] = hold
                finished = False
    return data


stuff = [4,123,6,5,124123,2,123,1,4,1,14,15,32,234,2352,23423,4525,2,23,211,24,1,1243]
print("shuttle",shuttle_sort(stuff))
print("bubble",bubble_sort(stuff))