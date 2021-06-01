#Kadans algorithm

A =  [4, -2, -8, 5, -2, 7, 7, 2, -6, 5, 4, -2, -8, 5, -2, 7, 7, 2, -6, 5, -4, -6, -7, -8 , -10, -12, -3, 8, 5, 6, 12, 6, 8 ,25]
def solution(A):
    meh = 0
    max = A[0]

    for i in range(0,len(A)):
        #print(i)
        print(F"meh is {meh} and a[i] is {A[i]}")
        meh = meh + A[i]
        if meh < A[i]:
            print(F"changing meh to {A[i]}")
            meh = A[i]
            start = i
            print(F"start is { i }")
        if max < meh or max is None:
            print(F"changing max to {meh}")
            max = meh
            end = i
            print(F"end is {i}")

    return list([start, end])

print(solution(A))
