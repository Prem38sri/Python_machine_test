#
A = ["co", "dil", "ity"]
def solution(A):
    # write your code in Python 3.6
    if len(A) < 1 or len(A) > 8:
        return 0
    else:
        max = 0
        def check(str1,str2):
            print(F"str1 is {str1} and str2 is {str2}")
            if len(str1) + len(str2) == len(set(str1+str2)):
                return str1+str2
            else:
                return str1

        for i in range(0,len(A) -1):
            print(F"i is {i}")
            if len(A[i]) == len(set(A[i])):
                fstr = A[i]
            else:
                continue
            for j in range(i + 1, len(A)):
                print(F"j is {j}")
                fstr = check(fstr,A[j])
                if max is None or max < len(fstr):
                    max = len(fstr)
                    print(F"max is {max}")
                print(fstr)
        return max

print(solution(A))
