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

xx, y_exp, y_ldm = [], [], []
LDM_data, exp_data = {}, {}
for i in range(len(A_list)):
    Z, A, N, BE = Z_list[i], A_list[i], N_list[i], BE_list[i]
    LD = bind_energy(Z, A, N, a_vol, a_surf, a_sym, a_coul)
    if A not in LDM_data:
        LDM_data[A] = []
    if A not in exp_data:
        exp_data[A] = []
    LDM_data[A].append(LD/A)
    exp_data[A].append(BE/A)

for A in sorted(LDM_data.keys()):
    xx.append(A)
    y_ldm.append(sum(LDM_data[A]) / len(LDM_data[A]))
    y_exp.append(sum(exp_data[A]) / len(exp_data[A]))

fig, ax = plt.subplots(figsize=(12,6))
plt.scatter(xx, y_ldm, label = 'LDM', marker = 'o', s=20, c='w',linewidths=1,edgecolors='k')
plt.scatter(xx, y_exp, label = 'exp.', marker = 'o', s=20,c='k')
plt.xticks(range(0,281,20))
plt.xlim([0,280])
ax.grid(axis='x',linestyle='--',alpha=0.3)
plt.legend()
plt.xlabel("A", fontsize = 20)
plt.ylabel("BE/A (MeV)")
plt.title("Binding energy per nucleon between LDM and experiment")

plt.savefig("BE_A_compare.pdf",bbox_inches='tight')
# chi2 = 0
# for i in range(len(A_list)):
#     chi2 += bind_energy(Z_list[i], A_list[i], N_list[i], BE_list[i], a_vol, a_surf, a_sym,  a_coul)
# chi2 /= len(A_list)
# chi2 = chi2**0.5
# chi2_history.append(chi2)
# if chi2 < min_chi2:
#     min_chi2 = chi2
#     final_chi2 = round(a_vol,3)
