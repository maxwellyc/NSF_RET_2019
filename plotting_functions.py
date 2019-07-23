# For Adobe illustrator text
import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 42


#1. Error band for radius
    # a. Multiply input rms radius by sqrt(5.0/3)
    # b. Error bar of coef. is chi^2 from chi^2 fit of R/A**(1.0/3) vs A fit, need to redo fit of
    # R/A**(1.0/3) vs A directly
    # c. resulting y values should be around 1.2
    # d. Produce an average coef. (y value) for each A value, for plotting purpose.

fig, ax = plt.subplots(num=None, figsize=(10, 4), dpi=80, facecolor='w', edgecolor='k')
ax.fill_between(x,y_upper,y_lower,facecolor='r',alpha=0.3,label=" ")


# 2. 2D color plots

# Fig init.
fig, ax = plt.subplots(1,1,figsize=(5.3,2.2))   # 5.3:2.2 is perfect for 290:120
ax2 = fig.add_axes([0.86, 0.1, 0.02, 0.7])

# specify color map
cmap = plt.cm.Blues
bounds = np.linspace(0,2,5)
norm = mpl.colors.Normalize(vmin=0.0, vmax = 2.0)

# color bar axis
cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm = norm, ticks=bounds)
ax2.set_title(r"             $E_{oct}$(MeV)", size=10)
cb.ax.tick_params(labelsize=6)

# main plotting
ax.scatter(x, y, c=z, marker="s",linewidths=0.1,s=4,cmap=cmap,norm=norm,edgecolor='k')

# tight config.
#plt.gcf().subplots_adjust(left=0.07,right=0.85)
plt.savefig("./plots/"+fn+".pdf",format='pdf',bbox_inches= 'tight')
