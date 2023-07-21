import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd

# EavsV = [coef ang, erro coef ang, voltagem, Ea(eV), Erro-Ea(eV), Ea(meV), Erro-Ea(meV)]

a = np.loadtxt('Ea1394Mesa#2_Terra07MelhorRes.txt', delimiter=',')
b = np.loadtxt('Ea1394Mesa#3_Terra07MelhorRes.txt', delimiter=',')
c = np.loadtxt('Ea1394Mesa#4_Terra07MelhorRes.txt', delimiter=',')
d = np.loadtxt('Ea1394Mesa#5_Terra07MelhorRes.txt', delimiter=',')
e = np.loadtxt('Ea1394Mesa#6_Terra07MelhorRes.txt', delimiter=',')
f = np.loadtxt('Ea1394Mesa#4_Terra01MelhorRes.txt', delimiter=',')
g = np.loadtxt('Ea1394Mesa#4_Terra01MelhorResPUC.txt', delimiter=',')
h = np.loadtxt('Ea1394Mesa#4_Terra01MelhorResTemAjeitada.txt', delimiter=',')
j = np.loadtxt('Ea1394Mesa#4_Terra07MelhorResVerificação.txt', delimiter=',')
# testePUC = np.c_[g, ]
# print(b)
# plt.figure('figura 1')
# plt.title('Comparação Medidas em Difrentes Mesas (Paso=0.1V)')


fig, ax1 = plt.subplots()

fig.suptitle('Amostra 1394 \n''Mesa#04(sinal)_Terra#01')
# ax1.errorbar(a[:, 2], a[:, 5], yerr=a[:, 6], fmt='o', label='Mesa#02-Terra#07')
# ax1.errorbar(b[:, 2], b[:, 5], yerr=b[:, 6], fmt='o', label='Mesa#03-Terra#07')
ax1.errorbar(c[:, 2], c[:, 5], yerr=c[:, 6], fmt='o', label='Mesa#04-Terra#07')
# ax1.errorbar(d[:, 2], d[:, 5], yerr=d[:, 6], fmt='o', label='Mesa#05-Terra#07')
# ax1.errorbar(e[:, 2], e[:, 5], yerr=e[:, 6], fmt='o', label='Mesa#06-Terra#07')
ax1.errorbar(f[:, 2], f[:, 5], yerr=f[:, 6],
             fmt='o', label='mesa#04-Terra#01-UFRJ')
ax1.errorbar(g[:, 2], g[:, 5], yerr=g[:, 6],
             fmt='o', label='PUC')
# ax1.errorbar(h[:, 2], h[:, 5], yerr=h[:, 6],
#  fmt='o', label='UFRJ - Temperatura Modificada \n''$ T_{Mod.} = a(T_{Med.}) + b$')
# ax1.errorbar(j[:, 2], j[:, 5], yerr=h[:, 6],
#  fmt='o', label='Mesa#04-Terra#07(Verificação)')
# ax1.errorbar(-g[:, 2], g[:, 5], yerr=h[:, 6], fmt='o', label='PucEspelho')


ax1.set_xlabel('Tensão (V)')
ax1.set_ylabel('Ea (meV)')
ax1.legend(prop={'size': 8}, loc=0)
# plt.grid(True)
plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.4)
plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.7)
plt.minorticks_on()
# plt.savefig('UFRJvsPUCespelho.jpg', dpi=300)
plt.show()
