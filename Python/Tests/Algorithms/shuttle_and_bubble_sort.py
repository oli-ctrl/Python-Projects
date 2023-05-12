from random import randint

def shuttle_sort (data):
    finished = False
    while not finished:
        finished = True
        # normal bubble sort
        for position in range(0, len(data)-1):
            if data[position] > data [position+1]:
                hold = data[position]
                data[position] = data[position+1]
                data[position+1] = hold
                finished = False
        # bubble sort but backwards :O
        if not finished:
            for rev_position in range (len(data)-1,0):
                if data[rev_position] < data [rev_position-1]:
                    rev_hold = data[rev_position-1]
                    data[rev_position-1] = data[rev_position]
                    data[rev_position] = rev_hold
                    finished = False
    return data

def bubble_sort (data_):
    finished = False
    while not finished:
        finished = True
        for position in range(0, len(data_)-1):
            if data_[position] > data_ [position+1]:
                hold = data_[position]
                data_[position] = data_[position+1]
                data_[position+1] = hold
                finished = False
    return data_


stuff = []
stuff_2 = []
for i in range(0,25):
    stuff.append(randint(0,100))
    stuff_2.append(randint(0,100))
    
print("running shuttle")
print("shuttle",shuttle_sort(stuff))
print("running bubble")
print("bubble",bubble_sort(stuff_2))
