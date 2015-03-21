import numpy as np
from PIL import Image

import primes

L = 601
im = np.zeros((L, L), dtype=int)
i, j, k = L/2, L/2, 1
l = 1
im[i,j] = k
while True:
    for a in range(l):
        j += 1
        k += 1
        if j < L:
            im[i,j] = k
    if j == L:
        break
    for a in range(l):
        i -= 1
        k += 1
        im[i,j] = k
    l += 1
    for a in range(l):
        j -= 1
        k += 1
        im[i,j] = k
    for a in range(l):
        i += 1
        k += 1
        im[i,j] = k
    l += 1

pLL = set(primes.up_to(L*L))
im = im.reshape((im.size,))
for i in range(im.size):
    if im[i] in pLL:
        im[i] = 0
im = im.reshape((L, L))

im[im!=0] = -1
im += 1
im *= 255

im = im.astype(np.uint8)
Image.fromarray(im).show()

