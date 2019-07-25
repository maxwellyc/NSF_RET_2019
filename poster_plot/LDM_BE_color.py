import numpy as np
import matplotlib.pyplot as plt
import csv
# For Adobe illustrator text
import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 42

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
        #print (A, Z, N, BE)

def bind_energy(Z, A, a_vol, a_surf, a_sym, a_coul):
    N = A - Z
    BE = a_vol*A - a_surf* A**(2.0/3) - a_sym*(N-Z)**2/A - a_coul* Z**2 / A**(1.0/3)
    return BE

a_vol = 15.7
a_surf = 17.22
a_sym = 23.35
a_coul = .72

x,y,z = [],[],[]
for i in range(len(A_list)):
    Z, A, BE = Z_list[i], A_list[i], BE_list[i]
    LD = bind_energy(Z, A, a_vol, a_surf, a_sym, a_coul)
    x.append(A-Z)
    y.append(Z)
    z.append(LD - BE)
    print (Z,A-Z,LD,BE)

# Fig initialization
fig, ax = plt.subplots(1,1,figsize=(6.7,4.55))   # 5.3:2.2 is perfect for 290:120
ax2 = fig.add_axes([0.93, 0.14, 0.02, 0.7])

# specify color map
cmap = plt.cm.bwr
bounds = np.linspace(-5,5,11)
norm = mpl.colors.Normalize(vmin=-5.0, vmax = 5.0)

#color bar axis
cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm = norm, ticks=bounds)
ax2.set_title(r"           $\Delta E$(MeV)", size=10)
cb.ax.tick_params(labelsize=6)

# main plotting
ax.scatter(x, y, c=z, marker="s",linewidths=0.1,s=19,cmap=cmap,norm=norm,edgecolor='k')

ax.set_xticks(range(20,161,20))
ax.set_yticks(range(10,111,10))
ax.set_ylim([0,115])
ax.set_xlim([0,170])
ax.set_xlabel("N")
ax.set_ylabel("Z")
ax.set_title(r"$BE_{LDM} - BE_{exp}$ (even-even nuclei)")
ax.grid(linestyle="--",alpha=0.3)
plt.savefig("2D_diff.pdf",format='pdf',bbox_inches='tight')
