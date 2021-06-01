import datetime


# brute force
def solution(S):
    a = datetime.datetime.now()
    # write your code in Python 3.6
    dec = 0
    for j in S:
        dec = dec * 2 + int(j)
    #print(dec)

    i = 0
    while dec > 0:
        if dec % 2 == 0:
            dec //= 2
            #print(dec)
        else:
            dec -= 1
        i += 1
    b = datetime.datetime.now()
    c = b - a
    print(F"time for first {c.microseconds} and answer is {i}")
    return i

#optimised , right shift on 0 and replace on 1
def better(S):
    a = datetime.datetime.now()
    steps = 0
    sstep = 0
    for j in range(len(S) -1,-1,-1):
        #print(F"j is {j} and item is {S[j]}")
        if int(S[j]) == 0:
            sstep += 1
        elif int(S[j]) == 1:
            #print(F"steps is { steps } and ssteps is { sstep }")
            steps = steps + sstep
            steps += 2
            sstep = 0
    b = datetime.datetime.now()
    c = b - a
    print(F"time for second {c.microseconds} and answer is {steps -1}")
    return steps -1

S = '1' * 4000000
#print(better('0001110000'))
