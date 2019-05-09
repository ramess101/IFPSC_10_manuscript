# -*- coding: utf-8 -*-
"""
Response to reviewer on thermodynamic scaling
"""

import numpy as np
import matplotlib.pyplot as plt

font = {'size' : '24'}
plt.rc('font',**font)

Prhoeta = np.loadtxt('IFPSC_10_data.txt',skiprows=1)

P = Prhoeta[:,0] #[MPa]
rho = Prhoeta[:,1] #[kg/m3]
eta = Prhoeta[:,2] #[mPa*s]

P[0] = 0.1

V = 1./rho #[m3/kg]

T = 293 #[K]

gamma_16 = 16./2.78 + 0.68
print(gamma_16)

gamma_range = np.array([gamma_16,6.400,6.500])
#gamma_range = np.array([6,6.1,6.2,6.3])
colors = ['k','b','r','g']
lines = ['-','--',':','-.']
markers = ['o','s','^','d']

fig = plt.figure(figsize=[12,12])  

for igamma, gamma in enumerate(gamma_range):
    
    color = colors[igamma]
    line = lines[igamma]
    line=''
    marker = markers[igamma]
    
    TVgamma = 1e-15/(T*V**gamma)
    
#    fig = plt.figure(figsize=[12,12])    
#    plt.semilogy(TVgamma,eta,color+line+marker)
#    plt.show()
    if igamma == 0:
        plt.semilogy(TVgamma,eta,color+line+marker,markersize=10,mfc='w',markeredgewidth=2,label=r'$\gamma = \frac{16}{2.78}+ 0.68 \approx$'+str(np.round(gamma,3)))
    else:
        plt.semilogy(TVgamma,eta,color+line+marker,markersize=10,mfc='w',markeredgewidth=2,label=r'$\gamma = $'+str(np.round(gamma,3)))
 
#plt.text(0,4000,r'$P = 0 \rm{MPa} \Rightarrow P = 1000 \rm{MPa}$',fontsize=28)
plt.text(12,4000,r'$P$ (MPa)',fontsize=28)
plt.text(10,2000,r'0 $\rightarrow$ 1000',fontsize=28)
    
plt.ylabel(r'$\eta$ [mPa $\cdot$ s]')
plt.xlabel(r'$\rho^{\gamma} T^{-1}$ [(kg/m$^3$)$^\gamma$ K$^{-1}$] $\times 10^{-15}$')
plt.legend()
plt.show()

#fig, ax1 = plt.subplots(figsize=[12,12])  

fig = plt.figure(figsize=[12,12])

ax1 = fig.add_subplot(111)  

for igamma, gamma in enumerate(gamma_range):
    
    color = colors[igamma]
    line = lines[igamma]
    line=''
    marker = markers[igamma]
    
    TVgamma = 1e-15/(T*V**gamma)
    
#    fig = plt.figure(figsize=[12,12])    
#    plt.semilogy(TVgamma,eta,color+line+marker)
#    plt.show()
    
    if igamma == 0:
        ax1.semilogy(TVgamma,eta,color+line+marker,markersize=10,mfc='w',markeredgewidth=2,label=r'$\gamma = \frac{16}{2.78}+ 0.68 \approx$'+str(np.round(gamma,3)))
    else:
        ax1.semilogy(TVgamma,eta,color+line+marker,markersize=10,mfc='w',markeredgewidth=2,label=r'$\gamma = $'+str(np.round(gamma,3)))
 
ax1.set_ylabel(r'$\eta$ [mPa $\cdot$ s]')
ax1.set_xlabel(r'$\rho^{\gamma} T^{-1}$ [(kg/m$^3$)$^\gamma$ K$^{-1}$] $\times 10^{-15}$')
ax1.legend()

ax1.set_ylim([0.5,6000])

#ax2 = ax1.twiny()
#ax2.semilogy(P,eta,color+line+marker,mfc='w')
#ax2.set_xlim([None,None])

#ax2 = ax1.twinx()
##ax2.semilogy(TVgamma,P,color+line+marker,mfc='w')
#ax2.semilogy([],[])
#ax2.set_ylim([0,1000])
#ax2.set_ylabel(r'$P$ (MPa)')

ax2 = ax1.twinx()
#fig.subplots_adjust(bottom=0.2)
new_tick_locations = np.array([0.1,28,4920])
#new_tick_locations = eta


def tick_function(eta):
    logeta = np.log10(eta)
    P = -2.07103*10*logeta**2 + 3.338712*100*logeta + 5.09115*10
    
#    for iP, P_i in enumerate(P): P[iP] = int(np.ceil(P_i / 10.0)) * 10

    return P

# Move twinned axis ticks and label from top to bottom
ax2.yaxis.set_ticks_position("right")
ax2.yaxis.set_label_position("right")

ax2.spines['right'].set_position(('axes',1))

ax2.set_frame_on(True)
#ax2.patch.set_visible(False)
#for sp in ax2.spines.itervalues():
#    sp.set_visible(False)
ax2.spines["right"].set_visible(True)
ax2.set_yscale('log')
#ax2.set_yticks(new_tick_locations)
#ax2.set_yticklabels(tick_function(new_tick_locations))
ax2.set_ylim(ax1.get_ylim())
ax2.set_yticks([0.5,1.6,26.6,4920])
ax2.set_yticklabels([0,100,500,1000])
#ax2.set_yticks(eta[1::2])
#ax2.set_yticklabels(P[1::2])
ax2.set_ylabel(r"Pressure (MPa)")
plt.show()