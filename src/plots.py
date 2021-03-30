import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib as mpl
from time import time
from mpl_toolkits.mplot3d import Axes3D

from physics import * 

fontsize = 25
newparams = {'axes.titlesize': fontsize,
             'axes.labelsize': fontsize,
             'ytick.labelsize': fontsize,
             'xtick.labelsize': fontsize, 
             'legend.fontsize': fontsize,
             'figure.titlesize': fontsize,
             'legend.handlelength': 1.5, 
             'lines.linewidth': 2,
             'lines.markersize': 7,
             'figure.figsize': (11, 7), 
             'figure.dpi':200,
             'text.usetex' : True,
             'font.family' : "sans-serif"
            }

plt.rcParams.update(newparams)

def B_hat(x,y,z):
    """
    B field function, only used for plotting 
    """
    xi_ = np.maximum(np.sqrt(x**2 + y**2 + z**2), 0.001) # avoid division by zero
    xi  = np.array([x,y,z])
    
    b1  = np.einsum('ijk,i',xi,m_hat)/xi_**5 
    b2  = m_hat[:,None,None]/xi_**3
    
    return 3 * xi * b1 - b2

def plot_earth_field():

    x = np.linspace(-10,10,400)
    y = np.linspace(-10,10,400)
    z = np.linspace(-10,10,400)

    xx, zz = np.meshgrid(x,z)
    xx, yy = np.meshgrid(x,y)

    B1 = B_hat(xx,np.zeros(np.shape(xx)),zz)
    B2 = B_hat(xx,yy,np.zeros(np.shape(zz)))
    
    fig, ax = plt.subplots(ncols = 2, figsize = (20,10))
    
    xmin = np.min(xx)
    xmax = np.max(xx)
    
    ymin = np.min(yy)
    ymax = np.max(yy)
    
    zmin = np.min(zz)
    zmax = np.max(zz)
    
    x = np.array([xmin,xmax])
    
    # xz plane
    
    # plot tilted axis 
    ax[0].plot(x,1/np.tan(theta)*x,ls = "--",color = "red", zorder = 1,lw  = 2)
    # plot the earth
    ax[0].add_patch(plt.Circle((0, 0), 1, color='b',zorder = 2))
    # plot the B-field
    ax[0].streamplot(xx,zz,B1[0],B1[2],color = "black",zorder = 1,arrowstyle = "fancy",linewidth = 2)
    
    ax[0].set_xlabel(r"$\xi_1$")
    ax[0].set_ylabel(r"$\xi_3$")
    
    ax[0].set_xlim([xmin,xmax])
    ax[0].set_ylim([zmin,zmax])
    
    #ax[0].axis("scaled")
    
    plt.tight_layout()
    
    # xy plane
    
    #plot tilted axis 
    ax[1].plot(x,np.tan(phi)*x,ls = "--",color = "red", zorder = 1,lw  = 2)
    # plot the earth
    ax[1].add_patch(plt.Circle((0, 0), 1, color='b',zorder = 2))
    # plot the B-field
    ax[1].streamplot(xx,yy,B2[0],B2[1],color = "black",zorder = 1,arrowstyle = "fancy",linewidth = 2)
    
    ax[1].set_xlabel(r"$\xi_1$")
    ax[1].set_ylabel(r"$\xi_2$")
    
    ax[1].set_xlim([xmin,xmax])
    ax[1].set_ylim([ymin,ymax])
    
    #ax[1].axis("scaled")
    
    plt.tight_layout()
    
    fig.savefig(cwd+path)
    
def plot_earth_field_traj(trajectory,title,path):

    x_  = np.min(trajectory[0,:])
    x__ = np.max(trajectory[0,:]) 
    
    x = np.linspace(x_ - 0.5,x__ + 0.5,400)
    y = np.linspace(x_ - 0.5,x__ + 0.5,400)
    z = np.linspace(x_ - 0.5,x__ + 0.5,400)

    xx, zz = np.meshgrid(x,z)
    xx, yy = np.meshgrid(x,y)

    B1 = B_hat(xx,np.zeros(np.shape(xx)),zz)
    B2 = B_hat(xx,yy,np.zeros(np.shape(zz)))
    
    fig, ax = plt.subplots(ncols = 2, figsize = (20,10))
    
    xmin = np.min(xx)
    xmax = np.max(xx)
    
    ymin = np.min(yy)
    ymax = np.max(yy)
    
    zmin = np.min(zz)
    zmax = np.max(zz)
    
    x = np.array([xmin,xmax])
    
    # xz plane
    
    plt.suptitle(title)
    
    # plot tilted axis 
    ax[0].plot(x,1/np.tan(theta)*x,ls = "--",color = "red", zorder = 1,lw  = 2)
    # plot the earth
    ax[0].add_patch(plt.Circle((0, 0), 1, color='b',zorder = 2,alpha = 0.3))
    # plot the B-field
    ax[0].streamplot(xx,zz,B1[0],B1[2],color = "black",zorder = 1,arrowstyle = "fancy",linewidth = 2)
    # plot the trajectory
    ax[0].plot(trajectory[:,0],trajectory[:,2],color ="blue")
    
    ax[0].set_xlabel(r"$\xi_1$")
    ax[0].set_ylabel(r"$\xi_3$")
    
    ax[0].set_xlim([xmin,xmax])
    ax[0].set_ylim([zmin,zmax])
    
    plt.tight_layout()
    
    # xy plane
    
    #plot tilted axis 
    ax[1].plot(x,np.tan(phi)*x,ls = "--",color = "red", zorder = 1,lw  = 2)
    # plot the earth
    ax[1].add_patch(plt.Circle((0, 0), 1, color='b',zorder = 2, alpha = 0.3))
    # plot the B-field
    ax[1].streamplot(xx,yy,B2[0],B2[1],color = "black",zorder = 1,arrowstyle = "fancy",linewidth = 2)
    # plot the trajectory
    ax[1].plot(trajectory[:,0],trajectory[:,1],color ="blue")
    
    ax[1].set_xlabel(r"$\xi_1$")
    ax[1].set_ylabel(r"$\xi_2$")
    
    ax[1].set_xlim([xmin,xmax])
    ax[1].set_ylim([ymin,ymax])
    
    plt.tight_layout()
    
    fig.savefig(cwd+path)


def add_field(ax,xmin,xmax):

    x = np.linspace(xmin,xmax,500)
    y = np.linspace(xmin,xmax,500)
    z = np.linspace(xmin,xmax,500)

    xx, zz = np.meshgrid(x,z)
    xx, yy = np.meshgrid(x,y)

    B1 = B_hat(xx,np.zeros(np.shape(xx)),zz)
    B2 = B_hat(xx,yy,np.zeros(np.shape(zz)))

    xmin = np.min(xx)
    xmax = np.max(xx)
    
    ymin = np.min(yy)
    ymax = np.max(yy)
    
    zmin = np.min(zz)
    zmax = np.max(zz)

    # plot tilted axis 
    ax[0].plot(x,1/np.tan(theta)*x,ls = "--",color = "red", zorder = 1,lw  = 2)
    # plot the earth
    ax[0].add_patch(plt.Circle((0, 0), 1, color='b',zorder = 2,alpha = 0.8))
    # plot the B-field
    ax[0].streamplot(xx,zz,B1[0],B1[2],color = "black",zorder = 1,arrowstyle = "fancy",linewidth = 2)
    ax[0].set_xlabel(r"$\xi_1$")
    ax[0].set_ylabel(r"$\xi_3$")
    ax[0].set_xlim([xmin,xmax])
    ax[0].set_ylim([zmin,zmax])

    #plot tilted axis 
    ax[1].plot(x,np.tan(phi)*x,ls = "--",color = "red", zorder = 1,lw  = 2)
    # plot the earth
    ax[1].add_patch(plt.Circle((0, 0), 1, color='b',zorder = 2, alpha = 0.8))
    # plot the B-field
    ax[1].streamplot(xx,yy,B2[0],B2[1],color = "black",zorder = 1,arrowstyle = "fancy",linewidth = 2)
    ax[1].set_xlabel(r"$\xi_1$")
    ax[1].set_ylabel(r"$\xi_2$")
    ax[1].set_xlim([xmin,xmax])
    ax[1].set_ylim([ymin,ymax])

def add_traj(ax,x,y,color="blue"):

    ax.plot(x,y,color=color)

def plot_fast(path):

    X  = np.load(path)
    
    fig, ax = plt.subplots(ncols = 2, figsize = (20,10))

    plt.suptitle(r"$v_0 = 10$")
    
    add_field(ax,-17,17)
    add_traj(ax[0],X[:,0],X[:,2])
    add_traj(ax[1],X[:,0],X[:,1])

    plt.tight_layout()
    fig.savefig("../fig/earth_traj_fast.pdf")


def plot_slow(path):

    X = np.load(path)
    
    fig, ax = plt.subplots(ncols = 2, figsize = (20,10))

    plt.suptitle(r"$v_0 = 1$")

    add_field(ax,-20,20)
    add_traj(ax[0],X[:,0],X[:,2])
    add_traj(ax[1],X[:,0],X[:,1])

    plt.tight_layout()
    fig.savefig("../fig/earth_traj_slow.pdf")

def plot_diffz():

    z  = np.array([0,0.25, 0.5, 0.75, 1])
    cmap=plt.get_cmap("viridis")
    fig, ax = plt.subplots(ncols = 2, figsize = (20,10))
    plt.suptitle(r"$v_0 = 7$")
    add_field(ax,-20,20)
    for zi in z:
        X  = np.load(f"../data/X_z0={zi}.npy")
        add_traj(ax[0],X[:,0],X[:,2],color=cmap(zi))
        add_traj(ax[1],X[:,0],X[:,1],color=cmap(zi))

        plt.tight_layout()
    fig.savefig("../fig/traj_diffz.pdf")

def plot_diffz_weak():

    z  = np.array([0,0.25, 0.5, 0.75, 1])
    cmap=plt.get_cmap("viridis")
    fig, ax = plt.subplots(ncols = 2, figsize = (20,10))

    plt.suptitle(r"$v_0 = 1$")
    add_field(ax,-20,20)
    for zi in z:
        X  = np.load(f"../data/Xw_z0={zi}.npy")
        add_traj(ax[0],X[:,0],X[:,2],color=cmap(zi))
        add_traj(ax[1],X[:,0],X[:,1],color=cmap(zi))

    plt.tight_layout()
    fig.savefig("../fig/weak_traj_diffz.pdf")

def plot_energy():

    fig = plt.figure()
    cmap=plt.get_cmap("viridis")
    
    z  = np.array([0,0.25, 0.5, 0.75, 1])
    T  = np.load("../data/T.npy")
    for zi in z:
        X = np.load(f"../data/X_z0={zi}.npy")
        E = v_square(X[:,3:])
        E = E/E[0]
        
        plt.plot(T,E,color = cmap(zi))

    plt.xlabel(r"$\tau$")
    plt.ylabel(r"$\frac{E(t)}{E(0)}$")

    plt.tight_layout()
    plt.grid(ls = "--")

    plt.savefig("../fig/energy.pdf")


if __name__ == "__main__":

    #plot_fast("../data/X_fast.npy")
    #plot_slow("../data/X_slow.npy")
    #plot_diffz()
    #plot_diffz_weak()
    plot_energy()
