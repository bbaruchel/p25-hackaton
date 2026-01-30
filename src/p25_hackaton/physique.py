from goo import Goo
from platform import Platform
import numpy as np
#gravité 
g=0.49

#distance attachement goo
l=0.01
masse_goo=0.4
k=100

def force_gravitation(goo: Goo):
    return (0,-goo.masse*g)


def force_rappel_goo(goo1: Goo, x,  y,ressort): #on considère que c'est le deuxieme qui attire
    d = ressort.distance
    if d == 0:
        return(0.,0.)
    l0=0.01
    f = -k*(d-l0)
    return (f/d*(goo1.x-x,goo1.y-y))

def force(goo1): 
    "Renvoie la résultante"
    (fx,fy)=force_gravitation(goo1)
    for (g,r) in goo1.voisins :
        fx+=force_rappel_goo(goo1,g[0],g[1], r)[0]
        fx+=force_rappel_goo(goo1,g[0],g[1], r)[1]
    
    for (h,r) in goo1.platforms:
        fx+=force_rappel_goo(goo1,h[0],h[1], r)[0]
        fx+=force_rappel_goo(goo1,h[0],h[1], r)[1]
    return (fx,fy)

def forces(goos):
    F=[]
    for i in range(len(goos)):
        F.append(force(goos[i]))
    return F


def verlet_integration_bis(goos, initial_points, initial_velocities, delta_t):
    A_x, A_y = np.array(force(goos)/masse_goo)
    #Mise à jour
    for i in range(len(goos)): 
        goos[i].x,goos[i].y = goos[i].x +goos[i].vx * delta_t + 1/2*A_x[i]*delta_t**2, goos[i].x+ goos[i].y * delta_t + 1/2*A_y[i]*delta_t**2
    n_Ax, n_Ay = forces(goos)/masse_goo

    for i in range(len(goos)):
        goos[i].vx,goos[i].vy = goos[i].vx + (A_x[i] + n_Ax[i])/2*delta_t, goos[i].vy + (A_y[i] + n_Ay[i])/2*delta_t
    
    return(goos, n_Ax,n_Ay )







