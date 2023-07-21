import serial
import csv
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import shutil


ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2, parity=serial.PARITY_NONE, bytesize=8, stopbits=1,
                    xonxoff=0,)  # open serial port
ser.write(':SENS:FUNC:CONC OFF \r'.encode())  # Desligua as funções simultâneas
ser.write(':SOUR:FUNC VOLT \r'.encode())  # Função fonte de volts
ser.write(':SENS:FUNC "CURR:DC" \r'.encode())  # Função, medida de corrrente
ser.write(':SENS:CURR:PROT 0.04 \r'.encode())  # Corrente proteção 40mA
ser.write(':SOUR:VOLT:START -5 \r'.encode())  # Voltagem começa -5V
ser.write(':SOUR:VOLT:STOP 5 \r'.encode())  # Voltagem termina 5V
ser.write(':SOUR:VOLT:STEP 2E-2 \r'.encode())  # paso de voltagem 0.02V
ser.write(':SOUR:VOLT:MODE SWE \r'.encode())  # Modo de varredura em volts
ser.write(':SOUR:SWE:RANG AUTO \r'.encode())  # Variação automática de fonte.
ser.write(':SOUR:SWE:SPAC LIN \r'.encode())  # Varredura em escada linear
ser.write(':TRIG:COUN 501 \r'.encode())  # Numero de pontos de varredura.
ser.write(':SOUR:DEL 0.01 \r'.encode())  # atraso da fonte de 100 ms
ser.write(':OUTP ON \r'.encode())  # Ativar a saída da fonte
ser.write(':READ? \r'.encode())  # Ativar varredura, solicitar dados

corrente = ser.readlines()
print(corrente)

ser.write(':OUTP OFF \r'.encode())  # Desligar a saida
ser.close()

a = np.array((corrente))
np.savetxt('300K.txt', a, fmt='%s')

bis = np.sort(glob.glob('./*.txt'))
arr = np.char.replace(np.array(bis), '.txt', '')
arr02 = np.char.replace(arr, './', '')
# print(arr02)
for i in range(len(bis)):
    c = np.genfromtxt(bis[i], dtype=float, delimiter=',')
    d = np.reshape(c, (501, 5))
    e = np.c_[d, np.abs(d[:, 1])]
    plt.title('Amostra 1380 \n'
              'mesa02-Terra04')
    plt.ylabel('Corrente (A)')
    plt.xlabel('Tensão (V)')
    plt.scatter(e[:, 0], e[:, 5])
    plt.yscale('log')
    plt.legend(bis, prop={'size': 6})
    plt.grid(b=True, which='minor', color='b', linestyle='--')
    plt.grid(b=True, which='major', color='b', linestyle='-')
# plt.savefig('LnRAvsT.jpg', dpi=300)
plt.show()

# a = np.genfromtxt('80K_hit.txt', dtype=float, delimiter=',')
# b = np.reshape(a, (501, 5))
# print(len(a))
