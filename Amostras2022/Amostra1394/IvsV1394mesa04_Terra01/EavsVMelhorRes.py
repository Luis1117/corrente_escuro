import glob
import numpy as np
import matplotlib.pyplot as plt


def my_plot_IvsV():
    dadosiniciais = sorted(glob.glob('./*K.txt'))
    renome01 = np.char.replace(np.array(dadosiniciais), '.txt', '')
    renome02 = np.char.replace(renome01, './', '')

    for i in range(len(dadosiniciais)):

        array = np.genfromtxt(dadosiniciais[i], dtype=float, delimiter=',')
        ajeitado = np.reshape(array, (501, 5))

        col_abs = np.c_[ajeitado, np.abs(ajeitado[:, 1])]
        plt.scatter(ajeitado[:, 0], col_abs[:, 5])
        plt.title('Amostra 1394')
        plt.grid()
        plt.yscale('log')
        plt.ylabel('Corrente (A)')
        plt.xlabel('Tensão (V)')
        plt.legend(renome02, prop={'size': 6})

    return plt.show()


def my_plot_EavsV():
    '''
    This function calculate the activation energy from the product \
        of area and differential resistance as funtion of temperture. \
            The differential resistance is find from a slope of a linear \
                regression of five points in the plot IvsV
    :return: Activation Energy
    '''
    m_T = []  # To save slope, error, voltage and txt with name of temperture
    d = glob.glob('./*K.txt')  # List of txt.

    for i in range(len(d)):

        e = np.genfromtxt(d[i], dtype=float, delimiter=',')
        IV = np.reshape(e, (501, 5))

        for j in range(0, 101):
            a = 5*j - 2
            b = 5*j + 3

            if a == -2 and b == 3:
                a = 0
                b = 3
            elif a == 498 and b == 503:
                a = 497
                b = 500

            lr = np.polyfit(IV[a:b, 0], IV[a:b, 1], 1, cov=True)

            ang = lr[0][0], np.sqrt(lr[1][0, 0]), j*0.1 - 5, d[i]

            m_T.append(ang)
    arr = np.char.replace(np.array(m_T), 'K.txt', '')
    arr02 = np.char.replace(arr, './', '')
    dl = arr02.astype(float)
    LnT = np.c_[dl, 1 / (dl[:, 0]), dl[:, 1] / (dl[:, 0] ** 2), (1 / dl[:, 0]) * 5e-8,
                dl[:, 1]/((dl[:, 0])*(10e-8)), np.log((1/dl[:, 0])*(5e-8)), dl[:, 1]/(dl[:, 0]), 1/(dl[:, 3])]

    LnTV = np.reshape(LnT, (21, 101, 11))
    Ea = []
    for i in range(101):
        LnTVn = LnTV[:, i][LnTV[:, i][:, 3].argsort()]
        Ea.append(LnTVn)
    # print(Ea)
    Ea_V = np.array(Ea)
    test = np.reshape(Ea_V, (2121, 11))
    # Dominio de plot:
    # for i in range(101):
    #     x = Ea_V[i, :][:, 10]
    #     y = Ea_V[i, :][:, 8]
    #     plt.scatter(x, y)
    #     plt.grid()
    #     plt.xlabel('1/T ($K^{-1}$)')
    #     plt.ylabel('Ln(RA) Ln($\\Omega$.$m^2$)')
    #     plt.title('Amostra 1394')
    # plt.savefig('LnRAvsT.jpg', dpi=300)
    # plt.show()

    EavsV = []

    for i in range(101):

        lr_Ln = np.polyfit(Ea_V[i, :][9:19, 10],
                           Ea_V[i, :][9:19, 8], 1, cov=True)
        Ang_Coef = lr_Ln[0][0], np.sqrt(lr_Ln[1][0, 0]), -5 + i*0.1

        EavsV.append(Ang_Coef)

    dados = np.array(EavsV)
    #  EavsV = [coef ang, erro coef ang, voltagem, Ea(eV), Erro-Ea(eV), Ea(meV), Erro-Ea(meV)]

    Ea1394 = np.c_[dados, dados[:, 0]*8.61e-5, dados[:, 1]
                   * 8.61e-5, dados[:, 0]*8.61e-2,  dados[:, 1]*8.61e-2]
    # print(dados)

    x_EA = Ea1394[:, 2]
    y_EA = Ea1394[:, 5]
    Err_Y = Ea1394[:, 6]

    plt.title('Amostra 1394 (paso voltagem = 0.1V)')
    # plt.scatter(x_EA, y_EA, yerr=Err_Y, fmt='o')
    plt.grid(axis='both')
    plt.xlabel('Tensão (V)')
    plt.ylabel('Ea (meV)')
    plt.errorbar(x_EA, y_EA, yerr=Err_Y, fmt='o', color='r')
    # plt.savefig('line_plot.jpg', dpi=300)

    np.savetxt('Ea1394Mesa#4_Terra01MelhorRes.txt', Ea1394, delimiter=',')
    return plt.show()


print(my_plot_EavsV())
