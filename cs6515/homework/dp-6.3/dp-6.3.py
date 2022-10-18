'''
' ALGORITHM
'''

def QVH1(M, P, k):
    # Validate we have anything to choose
    if len(M) == 0 or len(P) == 0:
        return 0

    profits = []
    for i, m in enumerate(M):
        # Base case
        if (i == 0):
            profits.append(P[i])
            continue

        # Determine max profit of the last location k distance behind
        P_j = 0
        for j in range(i):
            if M[j] <= (m - k):
                P_j = profits[j]

        # Determine max profit for current location
        profit = max(profits[i-1], P[i] + P_j)
        profits.append(profit)

    # Report max profit at the last location
    return profits[len(M)-1]

'''
' TEST CASES
'''

print(QVH1([], [], 1)) # 0
print(QVH1([1,3,5], [2,4,6], 3)) # 8
print(QVH1([1,2,3,5,8,9,10], [10,5,20,50,30,35,2], 1)) # 152
print(QVH1([1,2,3,5,8,9,10], [10,5,20,50,30,35,2], 3)) # 95