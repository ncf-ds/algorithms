import numpy as np

def partition(A, p, r):
    """Returns a partition point.
    """
    i = p - 1
    for j in range(p, r):
        if A[j] < A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r],  A[i + 1]
    return i + 1


def quicksort(A, p = 0, r = None, randomize=True):
    """Sorts an array. By default randomly chooses pivot.
    Set `randomize` to `False` to disable.
    """
    if r == None:
        r = len(A) - 1
    if p < r:
        if randomize:
            x = np.random.randint(p, r + 1)
            A[r], A[x] = A[x], A[r]
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def main():
    """Run an example of `quicksort` on an array of random integers.
    """
    N = 10
    A = list(np.random.random_integers(0, 10, N))
    print("Before:" + str(A))
    quicksort(A, 0, len(A) - 1)
    print("After:" + str(A))
