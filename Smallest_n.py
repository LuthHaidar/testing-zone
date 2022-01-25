#(Finding the smallest n such that n2 > k)
#Use a while loop to find the smallest integer n such that n2 is greater than k.
def smallestN(k):
    n = 1
    while n ** 2 < k:
        n = n + 1
    return print(n)