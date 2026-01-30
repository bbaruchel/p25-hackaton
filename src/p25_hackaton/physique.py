from .goo import Goo
from .platform import Platform
from .spring import Spring

import numpy as np
#gravité 
g= - 0.49

#distance attachement goo
l=0.01
masse_goo=0.4

def force_gravitation(goo: Goo):
    return (0.,-goo.masse*g)


def force_rappel_goo(goo1: Goo, x,  y,ressort : Spring): #on considère que c'est le deuxieme qui attire
    d = ressort.distance
    if d == 0:
        return(0.,0.)
    k = ressort.k
    l0=ressort.l_0
    f = -k*(d-l0)
    return (f*(goo1.x-x)/d,f*(goo1.y-y)/d)

#force de frottement visqueux pour atténuer les oscillations
def force_frottement(goo1 : Goo):
    mu = 0.1
    return (-mu*goo1.vx,-mu*goo1.vy)

def force(goo1 : Goo): 
    "Renvoie la résultante"
    (fx,fy)=force_gravitation(goo1)
    for (g,r) in goo1.voisins :
        fx+=force_rappel_goo(goo1,g.x,g.y, r)[0]
        fy+=force_rappel_goo(goo1,g.x,g.y, r)[1]
    
    for (h,r) in goo1.platforms:
        fx+=force_rappel_goo(goo1,r.x0,r.y0, r)[0]
        fy+=force_rappel_goo(goo1,r.x0,r.y0, r)[1]
    
    (fxt,fyt)=force_frottement(goo1)
    fx+=fxt
    fy+=fyt

    return (fx,fy)

def forces(goos):
    F=[]
    for i in range(len(goos)):
        F.append(force(goos[i]))
    return F


""" def verlet_integration_bis(goos, delta_t):
   A = np.array(forces(goos))/masse_goo
    #Mise à jour
   for i in range(len(goos)): 
        goos[i].x, goos[i].y = goos[i].x +0.9*(goos[i].vx * delta_t + (1/2)*A[i][0]*(delta_t)**2), goos[i].y + 0.9*(goos[i].vy * delta_t + (1/2)*A[i][1]*(delta_t)**2)
    n_A = np.array(forces(goos))/masse_goo
    for i in range(len(goos)):
        goos[i].vx ,goos[i].vy = goos[i].vx + 0.9*(delta_t*(A[i][0] + n_A[i][0])/2), goos[i].vy + 0.9*(delta_t*(A[i][1] + n_A[i][1])/2)
     """

def euler_integration(goos, delta_t):
    A = np.array(forces(goos))/masse_goo
    for i in range(len(goos)):
        goos[i].vx ,goos[i].vy = goos[i].vx + delta_t*A[i][0], goos[i].vy + delta_t*A[i][1]
        goos[i].x, goos[i].y = goos[i].x + goos[i].vx * delta_t, goos[i].y + goos[i].vy * delta_t


seuil = 0.2
def spring_update(goos) : 
  visite = [False]*len(goos)
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
            if r.distance > seuil :
              s.platforms=list(filter(lambda pr : not (pr[0].x == p.x and  pr[0].y == p.y),s.platforms))
          for (v,r) in s.voisins :
            r.distance = ((s.x-v.x)**2+(s.y-v.y)**2)**(1/2)
            if r.distance > seuil :
              s.voisins=list(filter(lambda gr : gr[0].id != v.id,s.voisins))
              v.voisins=list(filter(lambda gr : gr[0].id != s.id,v.voisins))
            todo.append(v)

def update_collision(goo: Goo, platform: Platform):
    collided = platform.contact(goo.x, goo.y)

    if not collided:
        return

    dl = goo.x - platform.x
    dr = (platform.x + platform.width) - goo.x
    dt = goo.y - platform.y
    db = (platform.y + platform.height) - goo.y

    dmin = min(dl, dr, dt, db)

    if dmin == dl:
        goo.x = platform.x - goo.rayon*0.5
        goo.vx = - goo.vx*0
    elif dmin == dr:
        goo.x = platform.x + platform.width + goo.rayon*0.5
        goo.vx = - goo.vx*0
    elif dmin == dt:
        goo.y = platform.y - goo.rayon*0.5
        goo.vy = - goo.vy*0
    else:  # dmin == db 
        goo.y = platform.y + platform.height + goo.rayon*0.5
        goo.vy = - goo.vy*0

    





