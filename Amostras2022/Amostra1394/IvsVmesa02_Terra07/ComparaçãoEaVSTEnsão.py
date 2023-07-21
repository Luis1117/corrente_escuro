from cProfile import label
import imp
from tkinter.ttk import Separator
import numpy as np
import matplotlib.pyplot as plt
import glob

a = np.loadtxt('EaVSTensao.txt', delimiter=',')
b = np.loadtxt('EavsV1394PUC.txt')
# print(b)

plt.figure('figura 1')
plt.title('Comparação Medidas PUC - UFRJ')
plt.scatter(a[:, 2], a[:, 5], label='UFRJ')
plt.scatter(b[:, 2], b[:, 5], label = 'PUC')
plt.legend(loc= "upper right")
plt.xlabel('Tensão (V)')
plt.ylabel('Ea(meV)')
plt.grid()
plt.show()
