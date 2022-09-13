import matplotlib.pyplot as plt
import numpy as np


def graph(filename, approximation_degree):
    # reading data from a file
    data = np.loadtxt(filename, delimiter=' ')

    num = []
    time = []

    for i in range(len(data)):
        num.append(data[i][0])
        time.append(data[i][1])

    # least squares approximation -
    if filename == "data/quick_sort1.txt" or filename == "data/tim_sort1.txt":
        p = np.polyfit(num * np.log(num), time, approximation_degree)
        fit = np.poly1d(p)
        plt.errorbar(num, time)
        plt.errorbar(num, fit(np.log(num)*num))

    else:
        p = np.polyfit(num, time, approximation_degree)
        yp = np.polyval(p, num)
        plt.errorbar(num, time)
        plt.errorbar(num, yp)

    plt.legend(["experimental data", "approximation"])
    if filename == "data/matrix_function.txt":
        plt.xlabel("matrix dimension")
    else:
        plt.xlabel("vector dimension")
    plt.ylabel("time, seconds")
    plt.show()


# constant function - O(1)
graph("data/const_function.txt", 0)
# sum of the elements - O(n)
graph("data/sum_function.txt", 1)
# product of the elements - O(n)
graph("data/prod_function.txt", 1)
# direct polynomial calculation - O(n*n)
graph("data/direct_polynom.txt", 2)
# horner's method - O(n)
graph("data/horner_polynom.txt", 1)
# bubble sort - O(n*n)
graph("data/bubble_sort.txt", 2)
# quick sort - O(n*log(n))
graph("data/quick_sort1.txt", 1)
# timsort - O(n*log(n))
graph("data/tim_sort1.txt", 1)
# matrix product - O(n*n*n)
graph("data/matrix_function.txt", 3)
