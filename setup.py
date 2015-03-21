from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(
        "primes.pyx",               # our Cython source
        language="c++",             # generate C++ code
    ))

