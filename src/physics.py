import numpy as np

def sphere(theta,phi):
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    
    return np.array([x,y,z])

def v_square(v):
    """
    Kinetic energy / mass

    """
    return 1/2 * np.einsum('ij,ij->i',v,v)

## Physical constants

m0    = 8e22
mu0   = 4*np.pi*1e-7
m     = 1.6e-27
q     = 1.6e-19
a     = 6.4e6

B_0   = mu0 * m0/(4*np.pi*a**3) 

C     = 1e5

B_0  *= C

theta = 11 * np.pi/180 
phi   = 0

m_hat = sphere(theta,phi)
