from goo import Goo
from platform import Platform

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





def verlet_integration(goo:Goo, initial_point, initial_velocity, delta_t):
    a_x,a_y= force(goo)/masse_goo
    x,y = initial_point
    v_x, v_y = initial_velocity

    #Mise à jour
    n_x,n_y = x+ v_x* delta_t + 1/2*a_x*delta_t**2, y+ v_y * delta_t + 1/2*a_y*delta_t**2

    n_ax,n_ay = force(n_x,n_y)/masse_goo

    n_vx,n_vy = v_x + (a_x + n_ax)/2*delta_t

    return (n_x ,n_y ,n_vx ,n_vy ,n_ax ,n_ay )

