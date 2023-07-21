import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd

# EavsV = [coef ang, erro coef ang, voltagem, Ea(eV), Erro-Ea(eV), Ea(meV), Erro-Ea(meV)]

a = np.loadtxt('Ea1380Mesa#01_Terra05.txt', delimiter=',')
b = np.loadtxt('Ea1380Mesa#02_Terra04.txt', delimiter=',')
c = np.loadtxt('Ea1380Mesa#03_Terra05.txt', delimiter=',')
d = np.loadtxt('Ea1380Mesa#06_Terra10.txt', delimiter=',')
e = np.loadtxt('Ea1380Mesa#07_Terra05.txt', delimiter=',')
f = np.loadtxt('Ea1380Mesa#08_Terra05.txt', delimiter=',')
# testePUC = np.c_[g, ]
# print(b)
# plt.figure('figura 1')
# plt.title('Comparação Medidas em Difrentes Mesas (Paso=0.1V)')


fig, ax1 = plt.subplots()

fig.suptitle('Amostra 1380')
ax1.errorbar(a[:, 2], a[:, 5], yerr=a[:, 6], fmt='o', label='Mesa#01-Terra#05')
ax1.errorbar(b[:, 2], b[:, 5], yerr=b[:, 6], fmt='o', label='Mesa#02-Terra#04')
ax1.errorbar(c[:, 2], c[:, 5], yerr=c[:, 6], fmt='o', label='Mesa#03-Terra#05')
ax1.errorbar(d[:, 2], d[:, 5], yerr=d[:, 6], fmt='o', label='Mesa#06-Terra#10')
ax1.errorbar(e[:, 2], e[:, 5], yerr=e[:, 6], fmt='o', label='Mesa#07-Terra#05')
ax1.errorbar(f[:, 2], f[:, 5], yerr=f[:, 6], fmt='o', label='mesa#08-Terra#05')

ax1.set_xlabel('Tensão (V)')
ax1.set_ylabel('Ea (meV)')
ax1.legend(prop={'size': 8}, loc=0)
# plt.grid(True)
plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.4)
plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.7)
plt.minorticks_on()
# plt.savefig('UFRJvsPUCespelho.jpg', dpi=300)
plt.show()
