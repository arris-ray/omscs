# Algorithm
def CC(C,v):
    n = len(C)

    # Initialize everything to false except for all cases where value = 0
    M = [[True if y == 0 else False for x in range(n)] for y in range(v+1)]

    # Build DP table using the recurrence relationship
    for i in range(1, v+1):
        for j in range(0, n):
            M[i][j] = True if ((i >= C[j]) and M[i-C[j]][j-1]) else False

    # Return result
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in M]))
    return any(M[v])

# Test cases
print(CC([1,5,10,25], 14)) # False
print(CC([1,5,10,25], 15)) # True
print(CC([1,5,10,25], 16)) # True
print(CC([10,5,1,25], 16)) # True
print(CC([25,5,1,10], 16)) # True
    