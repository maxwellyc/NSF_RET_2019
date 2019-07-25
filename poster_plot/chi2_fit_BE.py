import numpy as np
import matplotlib.pyplot as plt
import csv
BE_list, A_list, Z_list, N_list = [],[],[],[]
chi2_history = []
final_a_vol = 0
min_chi2 = float("Inf")
a_vol = float("Inf") #first coefficient in SEMF based on volume
a_surf = float("Inf") #second coefficient in SEMF based on surface area
a_sym = float("Inf") #third coefficient in SEMF based on symmetry
a_coul = float("inf")#fourth coefficient in SEMF based on coulomb attraction/electrostatic


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
            #print (type(A),type(Z),type(N),type(BE))

def bind_energy(Z, A, N, BE, a_vol, a_surf, a_sym, a_coul):
    LD_BE = a_vol*A - a_surf* A**(2.0/3) - a_sym*(N-Z)**2/A - a_coul* Z**2 / A**(1.0/3)
    return ((BE) - LD_BE)**2

iter = 0
for a_vol in np.arange(15.68,15.73,.01):
    a_vol = round(a_vol,4)
    for a_surf in np.arange(17.2,17.4,.01):
        a_surf = round(a_surf,4)
        for a_sym in np.arange(23.2,23.5,.01):
            a_sym = round(a_sym,4)
            for a_coul in np.arange(.7,.75,0.01):
                iter += 1
                if not iter % 1000:
                    print (iter)
                a_coul = round(a_coul,3)
                chi2 = 0
                for i in range(len(A_list)):
                    chi2 += bind_energy(Z_list[i], A_list[i], N_list[i], BE_list[i], a_vol, a_surf, a_sym,  a_coul)
                chi2 /= len(A_list)
                chi2 = chi2**0.5
                chi2_history.append(chi2)
                if chi2 < min_chi2:
                    min_chi2 = chi2
                    final_a_vol, final_a_surf, final_chi2 = round(a_vol,3), round(a_surf,4), chi2
                    final_a_sym, final_a_coul = round(a_sym,4), round(a_coul,4)

print (final_chi2, final_a_vol, final_a_surf, final_a_sym, final_a_coul)
