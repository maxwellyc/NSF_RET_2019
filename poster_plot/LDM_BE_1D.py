import numpy as np
import matplotlib.pyplot as plt
import csv

BE_list, A_list, Z_list, N_list, DBE_list = [],[],[],[],[]
Z_plot = []

a_vol = 15.7
a_surf = 17.22
a_sym = 23.35
a_coul = .72

def isNum(x):       #this checks if the input from file can be written as a float term (not str of words)
    try:
        x = float(x)
        return True
    except:
        return False

with open('b_energy.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    headers = next(readCSV) #to discount header row without numbers
    for row in readCSV:
        N = int(row[1])
        Z = int(row[0])
        BE = float(row[2])
        A = Z + N
        if not Z%2 and not N%2:
            Z_list.append(Z)
            A_list.append(A)
            N_list.append(N)
            BE_list.append(BE)

def bind_energy(Z, A, N, a_vol, a_surf, a_sym, a_coul):
    LD_BE = a_vol*A - a_surf* A**(2.0/3) - a_sym*(N-Z)**2/A - a_coul* Z**2 / A**(1.0/3)
    return LD_BE

for i in range(len(A_list)):
    Z, A, N, BE = Z_list[i], A_list[i], N_list[i], BE_list[i]
    Z_plot.append(N)
    LD = bind_energy(Z, A, N, a_vol, a_surf, a_sym, a_coul)
    print (Z,N,LD,BE)
    DBE = (LD - BE)
    DBE_list.append(DBE)

plt.scatter(Z_plot, DBE_list, marker = 'o', s=2,c='r')
plt.xlabel("N", fontsize = 20)
plt.xlim([0,170])
plt.ylabel(r"$\Delta E$ (MeV)")
plt.title(r"$BE_{LDM} - BE_{exp}$ (even-even nuclei)")

plt.savefig("1D_difference.pdf",bbox_inches='tight')
# chi2 = 0
# for i in range(len(A_list)):
#     chi2 += bind_energy(Z_list[i], A_list[i], N_list[i], BE_list[i], a_vol, a_surf, a_sym,  a_coul)
# chi2 /= len(A_list)
# chi2 = chi2**0.5
# chi2_history.append(chi2)
# if chi2 < min_chi2:
#     min_chi2 = chi2
#     final_chi2 = round(a_vol,3)
