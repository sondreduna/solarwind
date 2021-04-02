from integration import *
from plots import *
import sys

"""
To run all simulations and plot the trajectories, simply run

python problems.py v_fast v_slow

where v_fast and v_slow are the two different initial velocities to 
use in the simulations. 

"""

def simulations(v_fast,v_slow):

    # fast particle: 
    
    x0 = -15
    v0 = v_fast

    t0   = 0
    Tmax = 50
    N    = 10000

    X = integrate(x0,0,v0,Tmax,N)
    saveX(X,f"../data/X_x0={x0}_v0={v0}.npy")

     # slow particle: 

    v0 = v_slow

    X = integrate(x0,0,v0,Tmax,N)
    saveX(X,f"../data/X_x0={x0}_v0={v0}.npy")

    ## Particles at different heights z0

    z  = np.array([0,0.25, 0.5, 0.75, 1])
    x0 = -15
    v0 = 7
    
    for zi in z:
        X = integrate(x0,zi,v0,Tmax,N);
        # save only the initial z value
        saveX(X,f"../data/X_z0={zi}.npy")

    # Save one time array to use for later
    T = np.linspace(0,Tmax,N)
    np.save("../data/T.npy",T)

    ## Do some simulations for weaker fields 
    
    x0   = -12
    v0   = 1

    for zi in z:
        X = integrate_weak(x0,zi,v0,Tmax,N);
        # save only the initial z value
        saveX(X,f"../data/Xw_z0={zi}.npy")


if __name__ == "__main__":

    v_fast, v_slow = sys.argv[1], sys.argv[2]

    v_fast = float(v_fast)
    v_slow = float(v_slow)
    
    simulations(v_fast, v_slow)

    print("Plotting ...")
    plot_earth_field()
    plot_fast(v_fast)
    plot_slow(v_slow)
    plot_diffz()
    plot_diffz_weak()
    plot_energy()
    print("Finished plotting.")
