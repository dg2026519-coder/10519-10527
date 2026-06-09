

Web VPython 3.2
ground = box(pos=vector(3, -5, 0), size=vector(5, 0.2, 2), color=color.green)

r = ring(pos=vector(3.7, -4, 0), size=vector(0.1, 1,1, 1,1), color=color.white, axis = vec(0,1,0))

v = vector(0, 0, 0)
g = vector(0, -9.8, 0)
dt = 0.02

  
s= sphere(pos=vector(0, 4, 0),radius=0.3)
v = vector(3.0, 0, 0)
dt = 0.02

t = 0
while t < 8 and s.pos.y < -4.5 :
    rate(60)
    s.pos = s.pos + v * dt
    if s.pos.x > 5.6 or s.pos.x < -5.6:
        v = vector(-v.x, v.y, v.z)
    t = t + dt
    
    
    
while s.pos.y > -4.5:
    rate(60)
    

    k = keysdown()
    if 'down' in k :
        a.axis.y -= 0.5
    if ' ' in k :
        v = v + g * dt
        s.pos = s.pos + v * dt








