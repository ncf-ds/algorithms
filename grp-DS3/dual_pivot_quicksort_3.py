"""

Dual Pivot Quicksort Version 3 for DS-grp3

Erin Craig
Carlos Arias
Phil Pope

"""

def dual_pivot_quicksort(A, left, right):
    """
    By Vladimir Yaroslavskiy.
    Sorts the array A in index range left, . . . ,right.
    """
    if left < right:
        if A[left] > A[right]:
            #Swap A[left] and A[right]
            A[left], A[right] = A[right], A[left]
        p = A[left]
        q = A[right]
        l = left + 1 
        g = right - 1
        k = l
        while k <= g:
            if A[k] <= p:
                #Swap A[k] and A[l]
                A[k], A[l] = A[l], A[k]
                l += 1
            else:
                if A[k] > q:
                    while A[g] > q and k < g:
                        g -= 1
                    #Swap A[k] and A[g]
                    A[k], A[g] = A[g], A[k]
                    g -= 1
                    if A[k] < p:
                        #Swap A[k] and A[l]
                        A[k], A[l] = A[l], A[k]
                        l += 1
            k += 1
        l -= 1
        g += 1
        #Bring pivots to final position
        #Swap A[left] and A[l] 
        A[left], A[l] = A[l], A[left]
        #Swap A[right] and A[g]
        A[right], A[g] = A[g], A[right]
        dual_pivot_quicksort(A, left , l - 1)
        dual_pivot_quicksort(A, l + 1, g - 1)
        dual_pivot_quicksort(A, g + 1, right)