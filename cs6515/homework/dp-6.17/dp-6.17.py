# Algorithm
def CC(C,v):
    n = len(C)

    # Initialize everything to false except for all cases where value = 0
    M = [True if x == 0 else False for x in range(v+1)] 

    # Build DP table using the recurrence relationship
    for i in range(1, v+1):
        for j in range(0, n):
            if C[j] <= i and M[i-C[j]] == True:
                M[i] = True
                break

    # Return result
    return M[v]

# Test cases
print(CC([5,10,25], 13)) # False
print(CC([4,5,10,25], 15)) # True
print(CC([4,6,10,25], 16)) # True
print(CC([10,6,4,25], 16)) # True
print(CC([25,4,6,10], 16)) # True
    