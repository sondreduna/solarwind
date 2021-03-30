import numpy as np
import numba as nb
from scipy.integrate import odeint
from physics import * 

@nb.njit
def B(X):
    X_  = np.linalg.norm(X)
    b1  = np.dot(X,m_hat)/X_**5 
    b2  = m_hat/X_**3
    
    return C * ( 3* X* b1 - b2 ) 

@nb.njit
def B_weak(X):
    return B(X) / 100

@nb.njit
def f(X,t):
    a = np.cross(X[3:],B(X[:3]))
    return np.concatenate((X[3:],a),axis = 0)

@nb.njit
def f_weak(X,t):
    a = np.cross(X[3:],B_weak(X[:3]))
    return np.concatenate((X[3:],a),axis = 0)

def integrate(x0,z0,v0,Tmax,N):

    X0 = np.array([x0,0,z0,v0,0,0])
    
    times = np.linspace(0, Tmax, N)
    X, infodict = odeint(f, X0,times, full_output = True)

    print(infodict["message"])
    return X

def integrate_weak(x0,z0,v0,Tmax,N):

    X0 = np.array([x0,0,z0,v0,0,0])

    times = np.linspace(0, Tmax, N)
    X, infodict = odeint(f_weak, X0,times, full_output = True)

    print(infodict["message"])
    return X

def saveX(X,path):

    # Save file with initial conditions as markers
    # Saving to .npy file is way faster than going via .txt
    
    np.save(path,X)
    
