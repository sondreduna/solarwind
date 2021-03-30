from integration import *
from plots import *

def simulations():

    # fast particle: 
    
    x0 = -15
    v0 = 10

    t0   = 0
    Tmax = 50
    N    = 5000

    X = integrate(x0,0,v0,Tmax,N)
    saveX(X,f"../data/X_fast.npy")

     # slow particle: 
    
    x0 = -15
    v0 = 1

    t0   = 0
    Tmax = 50
    N    = 5000

    X = integrate(x0,0,v0,Tmax,N)
    saveX(X,f"../data/X_slow.npy")

    ## Particles at different heights z0

    z  = np.array([0,0.25, 0.5, 0.75, 1])
    x0 = -15
    v0 = 7
    
    for zi in z:
        X = integrate(x0,zi,v0,Tmax,N);
        # save only the initial z value
        saveX(X,f"../data/X_z0={zi}.npy")

    ## Do some simulations for weaker fields 
    
    x0   = -15
    v0   = 1

    for zi in z:
        X = integrate_weak(x0,zi,v0,Tmax,N);
        # save only the initial z value
        saveX(X,f"../data/Xw_z0={zi}.npy")

    # Save only one time array (same for all trajectories)
    T = np.linspace(0,Tmax,N)
    np.save("../data/T.npy",T)
    

if __name__ == "__main__":

    simulations()
