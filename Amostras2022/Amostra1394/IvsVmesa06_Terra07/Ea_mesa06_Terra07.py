import glob
import numpy as np
import matplotlib.pyplot as plt


# a = np.genfromtxt('300K.txt', dtype=float, delimiter=',')
# # b = glob.glob('./*.txt')
# b = np.reshape(a,(501, 5))
# x = b[:, 0]
# y = b[:, 1]
# plt.figure('1')
# plt.scatter(x, y)
# plt.show()
def my_funtion():
    '''
    Funtion that to find
    :return: PLots
    '''
    m_T = []
    d = glob.glob('./*.txt')
    for i in range(len(d)):
        e = np.genfromtxt(d[i], dtype=float, delimiter=',')
        IV = np.reshape(e, (501, 5))

        for j in range(0, 11):
            a = 50*j - 2
            b = 50*j + 3

            if a == -2 and b == 3:
                a = 0
                b = 3
            elif a == 498 and b == 503:
                a = 497
                b = 500

            lr = np.polyfit(IV[a:b, 0], IV[a:b, 1], 1, cov=True)

            ang = lr[0][0], np.sqrt(lr[1][0, 0]), j - 5, d[i]

            m_T.append(ang)
    arr = np.char.replace(np.array(m_T), 'K.txt', '')
    arr02 = np.char.replace(arr, './', '')
    dl = arr02.astype(float)
    LnT = np.c_[dl, 1 / (dl[:, 0]), dl[:, 1] / (dl[:, 0] ** 2), (1 / dl[:, 0]) * 5e-8,
                dl[:, 1]/((dl[:, 0])*(10e-8)), np.log((1/dl[:, 0])*(5e-8)), dl[:, 1]/(dl[:, 0]), 1/(dl[:, 3])]
    LnTV = np.reshape(LnT, (21, 11, 11))
    Ea = []
    for i in range(11):
        LnTVn = LnTV[:, i][LnTV[:, i][:, 3].argsort()]
        Ea.append(LnTVn)
    # print(Ea)
    Ea_V = np.array(Ea)
    # test = np.reshape(Ea_V, (242, 11))
    # Dominio de plot:
    x_5V = Ea_V[0, :][:, 10]
    y_5V = Ea_V[0, :][:, 8]

    x_4V = Ea_V[1, :][:, 10]
    y_4V = Ea_V[1, :][:, 8]

    x_3V = Ea_V[2, :][:, 10]
    y_3V = Ea_V[2, :][:, 8]

    x_2V = Ea_V[3, :][:, 10]
    y_2V = Ea_V[3, :][:, 8]

    x_1V = Ea_V[4, :][:, 10]
    y_1V = Ea_V[4, :][:, 8]

    x0V = Ea_V[5, :][:, 10]
    y0V = Ea_V[5, :][:, 8]

    x1V = Ea_V[6, :][:, 10]
    y1V = Ea_V[6, :][:, 8]

    x2V = Ea_V[7, :][:, 10]
    y2V = Ea_V[7, :][:, 8]

    x3V = Ea_V[8, :][:, 10]
    y3V = Ea_V[8, :][:, 8]

    x4V = Ea_V[9, :][:, 10]
    y4V = Ea_V[9, :][:, 8]

    x5V = Ea_V[10, :][:, 10]
    y5V = Ea_V[10, :][:, 8]

    # Plot das figuras vs 1/T:

    # plt.figure(1)
    # plt.scatter(x_5V, y_5V, label='-5V')
    # plt.scatter(x_4V, y_4V, label='-4V')
    # plt.scatter(x_3V, y_3V, label='-3V')
    # plt.scatter(x_2V, y_2V, label='-2V')
    # plt.scatter(x_1V, y_1V, label='-1V')
    # plt.scatter(x0V, y0V, label='0V')
    # plt.scatter(x1V, y1V, label='1V')
    # plt.scatter(x2V, y2V, label='2V')
    # plt.scatter(x3V, y3V, label='3V')
    # plt.scatter(x4V, y4V, label='4V')
    # plt.scatter(x5V, y5V, label='5V')
    # plt.legend(loc="upper right")
    # plt.grid()
    # plt.xlabel('1/T ($K^{-1}$)')
    # plt.ylabel('Ln(RA) Ln($\\Omega$.$m^2$)')
    # plt.title('Amostra 1394 Mesa#06-Terra#07')
    # plt.savefig('LnRAvsT.jpg', dpi=300)
    # plt.show()

    EavsV = []

    for i in range(11):

        lr_Ln = np.polyfit(Ea_V[i, :][10:20, 10],
                           Ea_V[i, :][10:20, 8], 1, cov=True)
        Ang_Coef = lr_Ln[0][0], np.sqrt(lr_Ln[1][0, 0]), -5 + i

        EavsV.append(Ang_Coef)

    dados = np.array(EavsV)

    Ea1394 = np.c_[dados, dados[:, 0]*8.61e-5, dados[:, 1]
                   * 8.61e-5, dados[:, 0]*8.61e-2,  dados[:, 1]*8.61e-2]
    print(Ea1394)

    x_EA = Ea1394[:, 2]
    y_EA = Ea1394[:, 5]
    Err_Y = Ea1394[:, 6]

    plt.title('Amostra 1394 Mesa#06-Terra07')
    # plt.scatter(x_EA, y_EA, yerr=Err_Y, fmt='o' )
    plt.grid(axis='both')
    plt.xlabel('Tensão (V)')
    plt.ylabel('Ea (meV)')
    plt.errorbar(x_EA, y_EA, yerr=Err_Y, fmt='o', color='r')
    # plt.savefig('line_plot.jpg', dpi=300)
    plt.show()

    # # np.savetxt('Ea1394Mesa#5_Terra07.txt', Ea1394, delimiter=',')


print(my_funtion())
