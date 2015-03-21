import cython
from libcpp.vector cimport vector

@cython.cdivision(True)
def up_to(size_t n):
    ''' Probably not the most efficient way to generate primes... '''
    cdef size_t i, j
    cdef vector[long] primes
    cdef bint is_prime
    for i in range(2, n):
        is_prime = True
        for j in range(primes.size()):
            if i % primes[j] == 0:
                is_prime = False
                break
        if is_prime:
            primes.push_back(i)
    return list(primes)

#annie

