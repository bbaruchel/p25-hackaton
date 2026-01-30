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
    return (f/d*(goo1.position_x-x,goo1.position_y-y))

