import numpy as np
import time


# matrix product
def product_function(a, b):
    length = len(a)
    c = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                c[i][j] += a[i][k] * b[k][j]
    return c


file = open('data/matrix_function.txt', 'w')
for n in range(1, 501):
    total_time = 0
    # generation of the random matrices a and b of size n*n
    a = np.random.random((n, n))
    b = np.random.random((n, n))
    # five runs to calculate the average time
    for k in range(5):
        start_time = time.perf_counter()
        product_function(a, b)
        stop_time = time.perf_counter()
        # computer execution time
        total_time = total_time + stop_time - start_time
    # the average time
    avg_time = total_time / 5
    # saving the results in file
    file.write('%d %s\n' % (n, avg_time))
file.close()
