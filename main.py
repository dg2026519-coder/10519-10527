5/26

ground = box(pos=vector(0, -5, 0), size=vector(10, 0.2, 4), color=color.blue)
b= box(pos=vector(0, 4, 0), radius=0.3,)
v = vector(0, 0, 0)
g = vector(0, -9.8, 0)
dt = 0.02
a = arrow(size = vec(5,5,5), pos = vec (0,10,0),color= color.cyan, axis = vec(0,-1,0))

while b.pos.y > -4.5:
    rate(60)
    

    k = keysdown()
    if 'down' in k :
        a.axis.y -= 0.5
    if ' ' in k :
        v = v + g * dt
        b.pos = b.pos + v * dt
