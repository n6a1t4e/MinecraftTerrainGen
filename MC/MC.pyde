width = 750
height = 750

def setup():
    global width, height
    size(width,height,P3D)
    
scl = 16
rows = 32
cols = 32

xoff = .03
yoff = xoff
depth = 0
high = 16
terrain = [[PVector(x,y,floor(map(noise(x*xoff,y*yoff),0,1,depth,high))) for x in range(cols)]for y in range(rows)]
Z = 0

def draw():
    global width,height,rows,cols,Z
    
    background(255)
    translate(width/2,height/2,-cols*scl*3/4)
    rotateX(PI/3)
    rotateZ(Z)
    
    fill(0,150,50)
    lights()
    for i in terrain:
        for j in i:
            pushMatrix()
            translate(j.x*scl-rows*scl/2,j.y*scl-cols*scl/2,j.z*scl)
            box(scl)
            popMatrix()
    Z += .015
