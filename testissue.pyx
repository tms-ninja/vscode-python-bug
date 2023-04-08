
def f():
    cdef int* ptr = NULL

    # Dereference null pointer to cause unexpected termination
    # On my system this produces a segmentation fault
    # ptr[0] = 5

    return 1
