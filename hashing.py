def ASCIIhash (string, n ):
    total = 0
    for letter in string:
        total += ord(letter)
    result = total %n
    return result

def hashtable(input,index):
    b = index
    while True:
        if b > len(list)-1:
            b = 0
        print (b)
        if hashlist[b] == None:
            hashlist[b] = input
            break
        else:
            b += 1

list = []
hashlist = [None]*len(list)

for i in list:
    print(i)
    hashtable(i, ASCIIhash(i, len(list)))




print(hashlist)
    