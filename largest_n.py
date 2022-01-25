#(Finding the largest n such that n^3 < k)
#Use a while loop to find the largest integer n such that n^3 is less than k.
def largestN(k):
    n = 1
    while n ** 3 < k:
        n = n + 1
    return n - 1