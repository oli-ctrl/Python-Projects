from random import randint, shuffle

def shuttle_sort (data):
    finished = False
    count = 0
    while not finished:
        count+=1
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
    return [data, count]

def bubble_sort (data):
    finished = False
    count= 0
    while not finished:
        count+=1
        finished = True
        for position in range(0, len(data)-1):
            if data[position] > data [position+1]:
                hold = data[position]
                data[position] = data[position+1]
                data[position+1] = hold
                finished = False
    return [data, count]



stuff = []
stuff_2 = []
shuttle_amount = []
bubble_amount = []
amount = int(input("how many cycles? "))
length = int(input("how Long is each list? "))

for i in range(0,amount):
    print(f"sorting {i+1}/{amount} ({round((i+1)/amount*100, 2)}%)", end="\r")
    stuff = []
    stuff_2 = []
    for x in range (0,length):
        stuff.append(randint(0,length*50))
        stuff_2.append(randint(0,length*50))
    shuttle_amount.append(shuttle_sort(stuff)[1])
    bubble_amount.append(bubble_sort(stuff_2)[1])


print("=====================================================")
print(f"shuttle sort max: {max(shuttle_amount)}")
print(f"bubble sort max: {max(bubble_amount)}")
print("=====================================================")
print(f"shuttle sort min: {min(shuttle_amount)}")
print(f"bubble sort min: {min(bubble_amount)}")
print("=====================================================")
print(f"shuttle sort average: {sum(shuttle_amount)/len(shuttle_amount)}")
print(f"bubble sort average: {sum(bubble_amount)/len(bubble_amount)}")


    
