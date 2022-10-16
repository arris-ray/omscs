###
# ALGORITHM
###

def SMS1(s):
    # Special case: Empty list
    if len(s) == 0:
        return []

    # Define and init storage
    SUM = [s[0]]
    SUB = [[s[0]]]

    # Main loop
    for i, v in enumerate(s, start=1):
        sum = max(v, SUM[i-1] + v)
        sub = [v] if sum == v else SUB[i-1] + [v]
        SUM.append(sum)
        SUB.append(sub)

    # Return result
    maxIndex = SUM.index(max(SUM)) 
    return SUB[maxIndex]

###
# TEST CASES
###

print(SMS1([])) # []
print(SMS1([-30, -5, -10])) # [-5]
print(SMS1([5, 15, -30, 10, -5, 40, 10])) # [10, -5, 40, 10]