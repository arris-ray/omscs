###
# ALGORITHM
###

def MUL1(S):
    M = [[[] for i in S] for j in S]
    n = len(S)

    for i in range(n):
        M[i][i] = [S[i]]

    for l in range(1, n):
        for i in range(n-l):
            j = i + l
            for s in range(i,j):
                m1 = M[i][s]
                m2 = M[s+1][j]
                m = _mul(m1, m2) 
                M[i][j] = _merge(M[i][j], m)
                # print ("[{},{}] - M[{}][{}] x M[{}][{}] = {}".format(i,j,i,s,s+1,j,M[i][j]))

    # print (M)
    return 'a' in M[0][n-1] 

def _mul(m1, m2):
    r = []
    for _m1 in m1:
        for _m2 in m2:
            m = _lut(_m1, _m2)
            _merge(r, m)
    # print ('{} x {} = {}'.format(m1, m2, r))
    return r

def _merge(dst, src):
    for m in src:
        if m not in dst:
            dst.append(m) 
    return dst

def _lut(m1, m2):
    if m1 == 'a' and m2 == 'a':
        return 'b'
    if m1 == 'a' and m2 == 'b':
        return 'b'
    if m1 == 'a' and m2 == 'c':
        return 'a'
    if m1 == 'b' and m2 == 'a':
        return 'c'
    if m1 == 'b' and m2 == 'b':
        return 'b'
    if m1 == 'b' and m2 == 'c':
        return 'a'
    if m1 == 'c' and m2 == 'a':
        return 'a'
    if m1 == 'c' and m2 == 'b':
        return 'c'
    if m1 == 'c' and m2 == 'c':
        return 'c'
    raise ValueError([m1, m2])

###
# TEST CASES
###

s = 'bbbbbb'
m = MUL1(s)
print('s=[%s] m=%s' % (s, m))

s = 'baab'
m = MUL1(s)
print('s=[%s] m=%s' % (s, m))

s = 'aabc'
m = MUL1(s)
print('s=[%s] m=%s' % (s, m))

s = 'bbac'
m = MUL1(s)
print('s=[%s] m=%s' % (s, m))

s = 'bbbbac'
m = MUL1(s)
print('s=[%s] m=%s' % (s, m))