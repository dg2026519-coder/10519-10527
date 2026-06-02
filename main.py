ground = box(pos=vector(0, -5, 0), size=vector(10, 0.2, 4), color=color.blue)

    
v = vector(0, 0, 0)
g = vector(0, -9.8, 0)
dt = 0.02

  
b= box(pos=vector(0, 4, 0), radius=0.3,)
v = vector(3.0, 0, 0)
dt = 0.02

t = 0
while t < 8:
    rate(60)
    b.pos = b.pos + v * dt
    if b.pos.x > 5.6 or b.pos.x < -5.6:
        v = vector(-v.x, v.y, v.z)
    t = t + dt
    
    
    
while b.pos.y > -4.5:
    rate(60)
    

    k = keysdown()
    if 'down' in k :
        a.axis.y -= 0.5
    if ' ' in k :
        v = v + g * dt
        b.pos = b.pos + v * dt 
    
        


v = vector(3.0, 0, 0)
dt = 0.02

t = 0
while t < 8:
    rate(60)
    a.pos = a.pos + v * dt
    if a.pos.x > 5.6 or a.pos.x < -5.6:
        v = vector(-v.x, v.y, v.z)
    t = t + dt







