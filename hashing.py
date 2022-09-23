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
        if hashlist[b] == None:
            hashlist[b] = input
            break
        else:
            b += 1

list = ["Frank", "Victor", "Arthur", "Winston", "Neil", "Abdulla", "Charlie", "Scott", "Ed",  "Ben"]
hashlist = [None]*len(list)

for i in list:
    hashtable(i, ASCIIhash(i, len(list)))

print(hashlist)

print (ASCIIhash("hello",len(list)))
