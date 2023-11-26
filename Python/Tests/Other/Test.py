def income(plane, f, e):
    econPrice = 0
    firstPrice = 0
    if plane == "Small Airframe":
        firstPrice += 16*f
        econPrice += 210+e
    elif plane == "Medium airframe":
        firstPrice += 32*f

    elif plane == "":
        firstPrice += 0

    return firstPrice + econPrice

def income(plane, f, e):
    econPrice = 0
    firstPrice = 0
    if plane == "Small Airframe":
        firstPrice += 16*f
        econPrice += 210*e
    elif plane == "Medium Airframe":
        firstPrice += 32*f
        econPrice += 300*e
    elif plane == "Large Airframe":
        firstPrice += 64*f
        econPrice += 850*f
    return firstPrice + econPrice


## I have given you some, But dont Want to give you all the answers, so edit the code above to make it work

print (f"small: {income('Small Airframe', 100, 50)}")
print (f"medium: {income('Medium Airframe', 90, 40)}")
print (f"large: {income('Large Airframe', 80, 30)}")

## running this code should return the following:
##
##      small: 12100
##      medium: 14880
##      large: 73120
##
## If these values are not returned, something is wrong, if u need a hint, ask me

