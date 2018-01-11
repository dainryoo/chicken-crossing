# Why did the chicken cross the road?
# DID the chicken cross the road???

# Crosswalk image from http://jacklamberti.com/crosswalk_detection/
# Storefront image from http://www.carlsons-stores.com/Glass_Storefronts.htm

time = 0
count = 0
count2 = 0

def setup():
    size(800, 800, P3D)
    global crosswalkBG, storefrontBG
    crosswalkBG = loadImage("crosswalk.png")
    storefrontBG = loadImage("storefront.png")
    
    
def draw():
    global time, crosswalkBG, storefrontBG, count, count2
    time += 1
    ambientLight(70, 70, 70);
    lightSpecular(100, 100, 100)
    directionalLight(100, 100, 100, -0.3, 0.5, -1)
    noStroke()
    specular(180, 180, 180)
    shininess(500.0)
    

    if time < 40: # SCENE 1
        camera(0, 0, 100, 0, 0, 0, 0,  1, 0)
        background(crosswalkBG)
        
        pushMatrix()
        translate(100-time*6, -26, 0)
        rotateX(-20 * PI / 180)
        scale(0.6, 0.6, 0.6)
        fill(150, 90, 90)
        drawCar()
        popMatrix()
        
        pushMatrix()
        translate(200-time*6, -25, 0)
        rotateX(-20 * PI / 180)
        scale(0.6, 0.6, 0.6)
        fill(100, 90, 200)
        drawCar()
        popMatrix()
        
        pushMatrix()
        translate(-100+time*15, -2, 0)
        rotateX(-20 * PI / 180)
        rotateY(175 * PI / 180)
        scale(1.2, 1, 1)
        fill(100, 100, 150)
        drawCar()
        popMatrix()
        
        pushMatrix()
        translate(-250+time*14, -3, 0)
        rotateX(-20 * PI / 180)
        rotateY(175 * PI / 180)
        scale(1, 0.7, 1)
        fill(160, 160, 180)
        drawCar()
        popMatrix()
        
        pushMatrix()
        translate(-400+time*10, 0, 0)
        rotateX(-20 * PI / 180)
        rotateY(175 * PI / 180)
        scale(1, 1, 1)
        fill(160, 150, 140)
        drawCar()
        popMatrix()
        
        pushMatrix()
        rotateX(12)
        count += 1
        if count < 10:
            translate(-count*0.5, 0, 0)
            rotateY(-4.7+count*0.01)
        elif count < 20:
            translate(count*0.5, 0, 0)
            rotateY(-4.7-count*0.01)
        else:
            rotateY(-4.7)
            count = 0
        translate(-27, 10, 0)
        drawChicken()
        popMatrix()
    
    elif time < 240: # SCENE 2
        pointLight(200, 200, 200, 100, -400, -200);
        background(storefrontBG)
        
        pushMatrix() # chicken
        translate(random(3)/5, random(2)/10, random(3)/5) # *nervously vibrates*
        rotateX(10 * PI / 180)
        rotateY(4.7)
        translate(-140, 70, 0)
        scale(6, 6, 6)
        drawChicken()
        popMatrix()
        
        fill(200, 250, 255) # Thought Bubble
        if time > 100:
            ellipse(-20, 15, 5, 5)
        if time > 110:
            ellipse(-25, 10, 7, 7)
        if time > 120:
            ellipse(-21, 0, 10, 10)
        if time > 130:
            ellipse(0, -30, 65, 57)
            
        if time > 150: # Thought Bubble expands (transition to next scene)
            if time > 185:
                fill(200-(time*0.9), 250-(time*0.9), 255-(time*0.9), time*1.1)
            elif time > 180:
                fill(200-(time*0.6), 250-(time*0.6), 255-(time*0.6), time*1.1)
            elif time > 175:
                fill(200-(time*0.4), 250-(time*0.4), 255-(time*0.4), time*1.1)
            elif time > 170:
                fill(200-(time*0.2), 250-(time*0.2), 255-(time*0.2), time*1.1)
            elif time > 160:
                fill(200-(time*0.1), 250-(time*0.1), 255-(time*0.1), time*1.1)
            else:
                fill(200, 250, 255, time*1.1)
            ellipse(0, -30, 65+abs(150-time)*2, 57+abs(150-time)*2)
        
        
    elif time < 800: # SCENE 3
        if time < 290: # chicken appears and motionlessly contemplates life
            background(0, 0, 0)
            camera(0, -30, 100, 0, 0, 0, 0,  1, 0)
            pushMatrix()
            rotateY(-80 * PI / 180)
            drawChicken()
            popMatrix()
            count = 0 # to loop chicken animation
            count2 = 0 # to loop crosswalk animation
            
        elif time < 550: # chicken walks
            background(0, 0, 0)
            camera(0, -30, 100, 0, 0, 0, 0,  1, 0)
            pushMatrix()
            count += 1
            count2 += 1
            if count < 4: # chicken bounces
                translate(0, count*0.2, 0)
            elif count < 8:
                translate(0, -abs(8-count*0.2), 0)
            else:
                count = 0
            rotateY(-80 * PI / 180)
            drawChicken()
            popMatrix()
            
            pushMatrix() # antagonist (car) approaches
            fill(185, 180, 240)
            translate(abs(550-time)*10, 0, 0) 
            rotateY(25 * PI / 180)
            drawCar()
            popMatrix()
            
            for i in range(0, 10): # draw many crosswalk lines
                drawCrosswalk(100 + i*25)
                
        else: # the tragedy
            if time < 620:
                background(0, 0, 0)
                camera(0, -30, 100, 0, 0, 0, 0,  1, 0)
                for i in range(0, 10):
                    drawCrosswalk(100 + i*25)
                
                pushMatrix()
                fill(185, 180, 240)
                translate(-30, 0, 0) 
                rotateY(25 * PI / 180)
                drawCar()
                popMatrix()
                count = 0
                
            if time < 690:
                count += 1
                background(0, 0, 0)
                camera(0, -30-count/2, 100, 0, 0, 0, 0,  1, 0)
    
                pushMatrix()
                translate(count, 0, 0)
                for i in range(0, 10):
                    drawCrosswalk(100 + i*25)
                
                pushMatrix()
                translate(-70, 0, 0)
                rotateX(55 * PI / 180)
                drawChicken()
                popMatrix()
                pushMatrix()
                fill(185, 180, 240)
                translate(-30, 0, 0) 
                rotateY(25 * PI / 180)
                drawCar()
                popMatrix()
                popMatrix()
                
    elif time < 1190: # SCENE 4
        camera(0, 0, 100, 0, 0, 0, 0,  1, 0)
        pointLight(200, 200, 200, 100, -400, -200);
        background(storefrontBG)
        
        if time < 860:
            pushMatrix() # chicken
            rotateX(0 * PI / 180)
            rotateY(-90 * PI / 180)
            translate(-5, 40, 0)
            scale(3, 3, 3)
            drawChicken()
            popMatrix()
            count = 0
        elif time < 870:
            count += 1
            pushMatrix() # chicken turns away from danger
            rotateX(0 * PI / 180)
            rotateY((-90-count*14) * PI / 180)
            translate(0, 40, 0)
            scale(3, 3, 3)
            drawChicken()
            popMatrix()
            count2 = 0
        else:
            if time < 872:
                count = 0 # hacky way to reset count, sorry 
                
            pushMatrix() # chicken walks away from danger
            
            translate(-count*3, 0, -count*1.5*3)
            count += 1 # increment for walking
            count2 += 1 # increment for bouncing
            if count2 < 3: # chicken bounces
                translate(0, count2*0.05, 0)
            elif count2 < 6:
                translate(0, -abs(6-count2*0.05), 0)
            else:
                count2 = 0
            
            rotateX(0 * PI / 180)
            rotateY((-90-10*14) * PI / 180)
            translate(0, 40, 0)
            scale(3, 3, 3)
            drawChicken()
            popMatrix()
            
    else: # END!!
        background(0, 0, 0)
    
def drawCrosswalk(initialPos): # crosswalk moving "animation" to make it look like chicken is walking
    global count2
    pushMatrix()
    fill(255, 255, 255)
    translate(initialPos/5+5-count2*0.2, 20, initialPos-count2)
    rotateY(15 * PI / 180)
    box(50, 0.1, 10)
    popMatrix()

def drawCar():
    pushMatrix() # body
    scale(4, 1.2, 3)
    box(10)
    popMatrix()
    
    pushMatrix()
    translate(5, -8, 0)
    scale(2, 1, 3)
    box(10)
    translate(-5, 3, 0)
    scale(4, 4, 5)
    prism()
    popMatrix()
    
    pushMatrix() # wheel
    translate(10, 5, -14)
    drawWheel()
    popMatrix()
    
    pushMatrix() # wheel
    translate(-10, 5, -14)
    drawWheel()
    popMatrix()
    
    pushMatrix() # wheel
    translate(10, 5, 14)
    drawWheel()
    popMatrix()
    
    pushMatrix() # wheel
    translate(-10, 5, 14)
    drawWheel()
    popMatrix()
    
    pushMatrix() # back lights
    fill(255, 10, 10)
    translate(16, 0, 10)
    scale(1, 0.5, 0.7)
    box(10)
    translate(0, 0, -29)
    box(10)
    popMatrix()
    
    pushMatrix() # license plate
    fill(250, 250, 250)
    translate(16, 1, 0)
    scale(1, 0.35, 0.7)
    box(10)
    popMatrix()
    
    pushMatrix() # front detail
    fill(150, 150, 150)
    translate(-16, -1, 0)
    scale(1, 0.3, 1)
    box(10)
    popMatrix()
    
    pushMatrix() # front lights
    fill(255, 232, 150)
    translate(-16, -1, 10)
    scale(1, 0.4, 0.6)
    box(10)
    translate(0, 0, -34)
    box(10)
    popMatrix()
    
    
def drawWheel():
    pushMatrix()
    fill(100, 100, 100)
    scale(4, 4, 3)
    cylinder()
    popMatrix()


def drawChicken():
    pushMatrix() # START CHICKEN
    sphereDetail(30)

    # ---------------- Body ----------------
    fill(255, 175, 114)
    pushMatrix()
    scale(1, 0.95, 1)
    sphere(10)
    # ---------------- Wing ----------------
    pushMatrix()
    fill(252, 166, 100)
    rotateY(-26 * PI / 180)
    translate(-1.7, 0, -8.9)
    scale(0.6, 0.4, 0.1)
    sphere(10)
    popMatrix()
    # ---------------- Wing2 ----------------
    pushMatrix()
    rotateY(26 * PI / 180)
    translate(-1.7, 0, 8.9)
    scale(0.6, 0.4, 0.1)
    sphere(10)
    popMatrix()
    # ---------------- Neck ----------------
    pushMatrix()
    fill(255, 175, 114)
    scale(0.9, 1.05, 0.9)
    translate(2, -1, 0)
    sphere(10)
    popMatrix()
    # ---------------- Tail ----------------
    pushMatrix()
    fill(252, 150, 73)
    translate(-7, -2, 0)
    rotateZ(-45 * PI / 180)
    scale(0.4, 0.7, 0.2)
    sphere(10)
    pushMatrix()
    fill(255, 161, 89)
    rotateZ(-10 * PI / 180)
    translate(-5, 2, 0)
    scale(0.9, 1, 0.9)
    sphere(10)
    pushMatrix()
    fill(249, 160, 92)
    rotateZ(-10 * PI / 180)
    translate(-5, 2, 0)
    scale(0.9, 1, 0.9)
    sphere(10)
    popMatrix()
    popMatrix()
    popMatrix()
    # ---------------- Leg ----------------
    pushMatrix()
    fill(255, 217, 79)
    scale(0.5, 4, 0.5)
    translate(0, 2, 7)
    rotateX(90 * PI / 180)
    cylinder()
    # ---------------- Foot ----------------
    pushMatrix()
    scale(3, 1.5, 0.05)
    translate(0.65, 0, -19)
    cylinder()
    popMatrix()
    popMatrix()
    # ---------------- Leg2 ----------------
    pushMatrix()
    scale(0.5, 4, 0.5)
    translate(0, 2, -7)
    rotateX(90 * PI / 180)
    cylinder()
    # ---------------- Foot2 ----------------
    pushMatrix()
    scale(3, 1.5, 0.05)
    translate(0.65, 0, -19)
    cylinder()
    popMatrix()
    popMatrix()
    popMatrix()
    
    
    # ---------------- Head ----------------
    pushMatrix()
    fill(249, 160, 92)
    scale(0.7, 0.7, 0.7)
    translate(4, -7.5, 0)
    sphere(10)
    # ---------------- Comb ---------------- 
    pushMatrix()
    fill(255,77, 17)
    scale(0.5, 0.3, 0.2)
    translate(5, -25, 0)
    sphere(10)
    popMatrix()
    # ---------------- Beak ----------------
    pushMatrix()
    fill(255, 217, 79)
    rotateZ(90 * PI / 180)
    scale(1, 2, 1)
    translate(-4, -3.5, 0)
    prism()
    # ---------------- Wattle ----------------
    pushMatrix()
    fill(255,77, 17)
    scale(0.15, 0.03, 0.1)
    translate(7, -40, 0)
    sphere(10)
    popMatrix()
    popMatrix()
    # ---------------- Eye ----------------
    pushMatrix()
    fill(10, 10, 10)
    scale(0.1, 0.15, 0.1)
    translate(75, -30, 30)
    sphere(10)
    popMatrix()
    # ---------------- Eye2 ----------------
    pushMatrix()
    fill(10, 10, 10)
    scale(0.1, 0.15, 0.1)
    translate(75, -30, -30)
    sphere(10)
    popMatrix()
    popMatrix()
    
    popMatrix() # END CHICKEN
    
def prism(): #a triangular prism
    # top triangle
    beginShape()
    vertex(0, -2, 1)
    vertex(-1, 0, 1)
    vertex(1, 0, 1)
    endShape()
    # bottom triangle
    beginShape()
    vertex(0, -2, -1)
    vertex(-1, 0, -1)
    vertex(1, 0, -1)
    endShape(CLOSE)
    # vertical side 1
    beginShape()
    vertex(0, -2, 1)
    vertex(0, -2, -1)
    vertex(-1, 0, -1)
    vertex(-1, 0, 1)
    endShape(CLOSE)
    # vertical side 2
    beginShape()
    vertex(0, -2, 1)
    vertex(0, -2, -1)
    vertex(1, 0, -1)
    vertex(1, 0, 1)
    endShape(CLOSE)
    # bottom side
    beginShape()
    vertex(1, 0, -1)
    vertex(1, 0, 1)
    vertex(-1, 0, 1)
    vertex(-1, 0, -1)
    endShape(CLOSE)

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2