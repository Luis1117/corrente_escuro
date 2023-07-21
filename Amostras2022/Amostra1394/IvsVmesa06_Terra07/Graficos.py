import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.inset_locator import (
    inset_axes, InsetPosition, mark_inset
)


a = np.genfromtxt('110K.txt', dtype=float, delimiter=',')
b = np.reshape(a, (501, 5))
# print(b)

# print(np.where(b[:, 0] == 1))
m, n = np.polyfit(b[298:303, 0], b[298:303, 1], 1)
p, q = np.polyfit(b[304:308, 0], b[304:308, 1], 1)


fig, ax1 = plt.subplots()

ax1.set_title('Amostra 1394')
ax1.scatter(b[:, 0], b[:, 1], label='Pontos Experimentais')
# ax1.plot(b[298:303, 0], b[298:303, 0] * m + n,
#          color='r', label='Regressão linear 1')
# ax1.plot(b[304:308, 0], b[304:308, 0]*p + q,
#  color='g', label='Regressão linear 2')
ax1.set_xlabel('Tensão (V)')
ax1.set_ylabel('Corrente (A)')
ax1.grid()
ax1.legend(loc=0)

# ax2 = plt.axes([0, 0, 0.1, 0.1])
# ip = InsetPosition(ax1, [0.1, 0.1, 0.5, 0.5])
# ax2.set_axes_locator(ip)

# mark_inset(ax1, ax2, loc1=3, loc2=1, fc='none', ec='0.6')

# ax2.scatter(b[294: 310, 0], b[294: 310, 1])
# ax2.plot(b[298:303, 0], b[298:303, 0] * m + n, color='r')
# ax2.plot(b[303:308, 0], b[303:308, 0] * p + q, color='g')
# plt.grid()
# ax2.legend(loc=0)

# ax1.set_ylim(-3e-6, 1.5e-6)
# ax2.set_xticklabels(ax2.get_xticks(), backgroundcolor='w')
# ax2.tick_params(axis='x', which='major', pad=8)

plt.show()


# plt.figure()
# plt.scatter(b[:, 0], b[:, 1])
# plt.plot(b[298:303, 0], b[298:303, 0] * m + n, color='r')
# plt.grid()
# plt.show()


# fig, ax1 = plt.subplots()
# ax1.scatter(b[:, 0], b[:, 1])
# ax1.grid()
# ax1.plot(b[298:302, 0], m*b[298:302, 0] + n, label='Regresão linear')
# ax1.set_xlabel('Tensão (V)')
# ax1.set_ylabel('Corrente (A)')
# # ax1.legend(loc=4)

# axins = zoomed_inset_axes(ax1, 30, loc=5)
# axins.scatter(b[:, 0], b[:, 1])


# axins.set_xlim(0.9, 1.1)
# axins.set_ylim(5.2e-8, 9e-8)

# plt.xticks(visible=True)
# plt.yticks(visible=True)

# mark_inset(ax1, axins, loc1=1, loc2=4, fc='none', ec='0.5')
# plt.draw()
# plt.show()


# Creamos inset eixos:
# ax2 = plt.axes([-0.04e-10, -5.6e-8, 1e-10, 5e-7])
# # posição e tamanho relativo  do ixo inset:
# ip = InsetPosition(ax1, [2, -1.3e-8, -4e-8, -5e-8])
# ax2.set_axes_locator(ip)
# mark_inset(ax1, ax2, loc1=1, loc2=3, fc="none", ec='0.5e-6')
