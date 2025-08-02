import sys
for size in sys.stdin:#1.的 2.對...做...
    r, c = map(int, size.split())

    #sol.1
    '''
    A = []
    for i in range(r):
        row = list(map(int, input().split()))
        A.append(row)
    '''

    #sol.2
    A = [list(map(int, input().split())) for i in range(r)]

    AT = []

    for i in range(len(A[0])):
        r = []
        for j in range(len(A)):
            r.append(A[j][i])
        AT.append(r)

    #sol.1
    # for i in range(len(AT)):
    #     print(*AT[i])

    #sol.2
    # for row in AT:
    #     print(*row)

    #sol.3
    [print(*row) for row in AT]