import matplotlib.pyplot as plt
import pylab
import numpy as np
from numpy import *

def f(t):
    return t**2*exp(-t**2)

def main():

    # http://acm.mipt.ru/twiki/bin/view/Cintro/PythonGraphs#_qp__cp___k_h_pmekk_numpy

    # --------- 1
    plt.plot([1, 2, 3, 4])
    plt.show()
    print("===============================================================")

    # --------- 2
    # 51 между 0 і 3
    t = linspace(0, 3, 51)
    y = f(t)
    plt.plot(t, y)
    plt.show()

    # --------- 3
    t = linspace(0, 3, 51)
    y = t ** 2 * exp(-t ** 2)
    plt.plot(t, y, 'g--', label='t^2*exp(-t^2)')
    plt.axis([0, 3, -0.05, 0.5]) #[xmin, xmax, ymin, ymax]
    plt.xlabel('t')  #
    plt.ylabel('y')  #
    plt.title('My first normal plot')
    plt.legend()
    plt.show()

    # --------- 4
    t = linspace(0, 3, 51)
    y1 = t ** 2 * exp(-t ** 2)
    y2 = t ** 4 * exp(-t ** 2)
    plt.plot(t, y1, label='t^2*exp(-t^2)')
    plt.plot(t, y2, label='t^4*exp(-t^2)')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Plotting two curves in the same plot')
    plt.legend()
    plt.show()

    # --------- 5
    t = linspace(0, 3, 51)
    y1 = t ** 2 * exp(-t ** 2)
    y2 = t ** 4 * exp(-t ** 2)
    y3 = t ** 6 * exp(-t ** 2)
    plt.plot(t, y1, 'g^',
             t, y2, 'b--',
             t, y3, 'ro-')
    #
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Plotting with markers')
    plt.legend(['t^2*exp(-t^2)',
                't^4*exp(-t^2)',
                't^6*exp(-t^2)'],
               loc='upper left')
    plt.show()

    # ---------- 6
    xdata = [0, 1, 2, 4, 5, 8]
    ydata = [0.1, 0.2, 0.4, 0.8, 0.6, 0.1]
    pylab.bar(xdata, ydata)
    pylab.show()

    # -------- 7
    y = np.random.randn(1000)
    plt.hist(y, 25)
    plt.show()

    # -------- 8
    data1 = 10 * np.random.rand(5)
    data2 = 10 * np.random.rand(5)
    data3 = 10 * np.random.rand(5)
    locs = np.arange(1, len(data1) + 1)
    width = 0.27
    plt.bar(locs, data1, width=width)
    plt.bar(locs + width, data2, width=width, color='red')
    plt.bar(locs + 2 * width, data3, width=width, color='green')
    plt.xticks(locs + width * 1.5, locs)
    plt.show()
    # save
    #plt.plot(t, y)
    #plt.savefig('name_of_plot.png', dpi=200)



if __name__ == '__main__':
    main()