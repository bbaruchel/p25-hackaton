from .goo import Goo
from .platform import Platform

import numpy as np
#gravité 
g=-0.49

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
    return (f/d*(goo1.x-x),f/d*(goo1.y-y))

def force(goo1 : Goo): 
    "Renvoie la résultante"
    (fx,fy)=force_gravitation(goo1)
    for (g,r) in goo1.voisins :
        fx+=force_rappel_goo(goo1,g.x,g.y, r)[0]
        fx+=force_rappel_goo(goo1,g.x,g.y, r)[1]
    
    for (h,r) in goo1.platforms:
        fx+=force_rappel_goo(goo1,h.x,h.y, r)[0]
        fx+=force_rappel_goo(goo1,h.x,h.y, r)[1]
    return (fx,fy)

def forces(goos):
    F=[]
    for i in range(len(goos)):
        F.append(force(goos[i]))
    return F


def verlet_integration_bis(goos, delta_t):
    A = np.array(forces(goos))/masse_goo
    #Mise à jour
    for i in range(len(goos)): 
        goos[i].x,goos[i].y = goos[i].x +goos[i].vx * delta_t + 1/2*A[i][0]*delta_t**2, goos[i].y + goos[i].vy * delta_t + 1/2*A[i][1]*delta_t**2
    n_A = np.array(forces(goos))/masse_goo
    for i in range(len(goos)):
        goos[i].vx,goos[i].vy = goos[i].vx + (A[i][0] + n_A[i][0])/2*delta_t, goos[i].vy + (A[i][1] + n_A[i][1])/2*delta_t
    
def spring_update(goos) : 
  visite = [False]*len(g)
  for g in goos :
    if not (visite[g.id]) :
      todo = [g]
      while len(todo) != 0 :
        s = todo.pop()
        if not visite[s.id] :
          visite[s.id] = True
          for (p,r) in s.platforms :
            x,y = r.x0,r.y0
            r.distance = ((s.x-x)**2+(s.y-y)**2)**(1/2)
          for (v,r) in s.voisins :
            r.distance = ((s.x-v.x)**2+(s.y-v.y)**2)**(1/2)
            todo.append(v)









