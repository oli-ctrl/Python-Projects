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


def search (search, hashed_position):
    x = hashed_position 
    tries = 1
    for i in list:
        if search == hashlist[x]:
            return f"found in position {x} in {tries} attempts" 
        x += 1
        if x > len(hashlist):
            return "failed to find value"
        tries += 1

list = ["Frank", "Victor", "Arthur", "Winston", "Neil", "Abdulla", "Charlie", "Scott", "Ed",  "Ben"]
hashlist = [None]*len(list)

for i in list:
    hashtable(i, ASCIIhash(i, len(list)))

print(hashlist)
searched = "Winston"

print(search(searched, ASCIIhash(searched, len(list))))
