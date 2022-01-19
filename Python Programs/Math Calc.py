##import math
###x=-b+-√b*b-4*a*c÷2*a
###a*x**2+b*x+c=0
##def sqrootfinder(x):
##    ans=1
##    for i in range(x+1,2,-1):
##        if x%i==0:
##            a=math.sqrt(i)
##            if a - int(a) == 0:
##                ans=a
##                break
##    return ans
##
##def gcd(x, y):
##    while y != 0:
##        (x, y) = (y, x % y)
##    return x
##
##while True:
##    print("Enter A")
##    A=int(input())
##    print("Enter B")
##    B=int(input())
##    print("Enter C")
##    C=int(input())
##    D=B**2 - 4*A*C
##    print("D =",D)
##    SD=sqrootfinder(D)
##    SD1=D/(SD**2)
##    if SD1!=1:
##        if SD!=1:
##            print("(",-B,"±",SD,"√",int(SD1),") ÷",2*A)
##        else:
##            print("(",-B,"± √",int(SD1),") ÷",2*A)
##    else:
##        X1=(-B + SD)/(2*A)
##        if X1 - int(X1) == 0:
##            print(int(X1))
##        else:
##            GCD=gcd(-B + SD,2*A)
##            print(int((-B + SD)/GCD),"/",int(2*A/GCD))
##            #print("(",-B + SD,") ÷",2*A)
##        X2=(-B - SD)/(2*A)
##        if X2 - int(X2) == 0:
##            print(int(X2))
##        else:
##            GCD=gcd(-B - SD,2*A)
##            print(int((-B - SD)/GCD),"/",int(2*A/GCD))
##            #print("(",-B - SD,") ÷",2*
##            

import numpy as np
import matplotlib.pyplot as plt
def mandelbrot1(n_rows, n_columns, iterations):
    x_cor = np.linspace(-2,1,n_rows)
    y_cor = np.linspace(-2,1,n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    for i in range(x_len):
        for j in range(y_len):
            c = complex(x_cor[i],y_cor[j])
            z = complex(0, 0)
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
            print((i/x_len)*100,"% completed")
    print(output)
    plt.imshow(output.T, cmap = "hot")
    plt.axis("off")
    plt.show()


def mandelbrot2(n_rows, n_columns, iterations, cx, cy):
    x_cor = np.linspace(-2, 2, n_rows)
    y_cor = np.linspace(-2, 2, n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    c = complex(cx, cy)
    for i in range(x_len):
        for j in range(y_len):
            z = complex(x_cor[i], y_cor[j])
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
        print(int((i/x_len)*100),"% completed")

    print(output)
    plt.imshow(output.T, cmap='hot')
    plt.axis("off")
    plt.show()

#mandelbrot2(1000,1000,120,-0.42,0.6)
    
from turtle import *
def tree(length,angle):
        if(length<9):
            right(angle)
            pencolor('pink')
            fillcolor('pink')
            begin_fill()
            circle(3)
            end_fill()
            left(angle)
            penup()
            return
        else:
            pendown()
            pencolor('brown')
            forward(length)
            right(angle)
            tree(0.8*length,angle)
            left(2*angle)
            if(0.8*length>9):
                tree(0.8*length,angle)
            right(angle)
            backward(length)
            penup()
            pendown()
            pencolor('brown')
def draw_fractal():
    speed(1000)
    up()
    left(90)
    backward(200.0)
    down()
    tree(100,30)
    mainloop()
#draw_fractal()

import matplotlib.cm as cm
from random import randint

def map_to_pixels(x,y,x_range=[-2.2,2.7],y_range=[0,10],x_req_range=[0,300],y_req_range=[0,300]):
    x_span = x_range[1]-x_range[0]
    x_req_span = x_req_range[1]-x_req_range[0]
    x_scaled = (x-x_range[0])/(x_span)
    px = x_req_range[0]+(x_scaled*x_req_span)

    y_span = y_range[1] - y_range[0]
    y_req_span = y_req_range[1] - y_req_range[0]
    y_scaled = (y - y_range[0]) / (y_span)
    py = y_req_range[0] + (y_scaled * y_req_span)

    return int(px),int(py)

def calc(a, m, e):
    result = np.zeros((len(a),len(m[0])))
    for i in range(len(a)):
        for j in range(len(m[0])):
            for k in range(len(m)):
                result[i][j] += a[i][k]*m[k][j]
    result = result+e
    #print(result)
    return result[0][0], result[1][0]

def fern(width=400,height=400):
    img = np.zeros((width,height))
    x = []
    y = []
    count = 0
    x.append(0)
    y.append(0)
    for i in range(1,50000):
        p = randint(1,100)
        if(p==1):
            X,Y = calc(a = [[0,0],[0,0.16]], m = [[x[count]],[y[count]]],e = [[0],[0]])
            x.append(X)
            y.append(Y)
            px,py = map_to_pixels(X,Y)
            img[px,py] = 1
        if(p>=2 and p<=86):
            X,Y = calc(a = [[0.85,0.04],[-0.04,0.85]],m = [[x[count]],[y[count]]],e = [[0],[1.60]])
            x.append(X)
            y.append(Y)
            px, py = map_to_pixels(X,Y)
            img[px,py] = 1
        if (p >= 87 and p <= 93):
            X, Y = calc(a=[[0.20, -0.26], [0.23, 0.22]], m = [[x[count]], [y[count]]], e=[[0], [1.60]])
            x.append(X)
            y.append(Y)
            px, py = map_to_pixels(X, Y)
            img[px, py] = 1
        if (p >= 94 and p <= 100):
            X, Y = calc(a=[[-0.15, 0.28], [0.26, 0.24]], m = [[x[count]], [y[count]]], e=[[0.44], [0.07]])
            x.append(X)
            y.append(Y)
            px, py = map_to_pixels(X, Y)
            img[px, py] = 1
        count += 1
        print(int((i/50000)*100),"%"," ","completed")
    #print(img)
    plt.imshow(np.flipud(img.T),cmap= cm.Greens)
    plt.axis('off')
    plt.show()
#fern(400,400)


def dragon_fractal(iterations, axiom, var1, replace1, var2, replace2, length, angle):
    old = axiom
    for i in range(iterations):
        new = ''
        for char in old:
            if(char==var1):
                new += replace1
            elif(char==var2):
                new += replace2
            else:
                new += char
        old = new
    for char in old:
        if(char=="F"):
            forward(length)
        elif(char=='+'):
            right(angle)
        elif(char=='-'):
            left(angle)

def draw_fractal(fractal_name):
    speed(0)
    bgcolor('black')
    pencolor('orange')
    if(fractal_name=="dragon"):
        while True:
            up()
            backward(200.0 / 2.0)
            left(90)
            down()
            dragon_fractal(10, 'FX', 'X', "X+YF+", "Y", "-FX-Y", 8, 90)

#draw_fractal('dragon')


#importing the required libraries 
import random, argparse 
import math 
import turtle 
from PIL import Image 
from datetime import datetime	 
from fractions import gcd 

# A class that draws a spirograph 
class Spiro: 
	# constructor 
	def __init__(self, xc, yc, col, R, r, l): 

		# create own turtle 
		self.t = turtle.Turtle() 
		# set cursor shape 
		self.t.shape('turtle') 
		# set step in degrees 
		self.step = 5
		# set drawing complete flag 
		self.drawingComplete = False

		# set parameters 
		self.setparams(xc, yc, col, R, r, l) 

		# initiatize drawing 
		self.restart() 

	# set parameters 
	def setparams(self, xc, yc, col, R, r, l): 
		# spirograph parameters 
		self.xc = xc 
		self.yc = yc 
		self.R = int(R) 
		self.r = int(r) 
		self.l = l 
		self.col = col 
		# reduce r/R to smallest form by dividing with GCD 
		gcdVal = gcd(self.r, self.R) 
		self.nRot = self.r//gcdVal 
		# get ratio of radii 
		self.k = r/float(R) 
		# set color 
		self.t.color(*col) 
		# current angle 
		self.a = 0

	# restart drawing 
	def restart(self): 
		# set flag 
		self.drawingComplete = False
		# show turtle 
		self.t.showturtle() 
		# go to first point 
		self.t.up() 
		R, k, l = self.R, self.k, self.l 
		a = 0.0
		x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k)) 
		y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k)) 
		self.t.setpos(self.xc + x, self.yc + y) 
		self.t.down() 

	# draw the whole thing 
	def draw(self): 
		# draw rest of points 
		R, k, l = self.R, self.k, self.l 
		for i in range(0, 360*self.nRot + 1, self.step): 
			a = math.radians(i) 
			x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k)) 
			y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k)) 
			self.t.setpos(self.xc + x, self.yc + y) 
		# done - hide turtle 
		self.t.hideturtle() 
	
	# update by one step 
	def update(self): 
		# skip if done 
		if self.drawingComplete: 
			return
		# increment angle 
		self.a += self.step 
		# draw step 
		R, k, l = self.R, self.k, self.l 
		# set angle 
		a = math.radians(self.a) 
		x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k)) 
		y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k)) 
		self.t.setpos(self.xc + x, self.yc + y) 
		# check if drawing is complete and set flag 
		if self.a >= 360*self.nRot: 
			self.drawingComplete = True
			# done - hide turtle 
			self.t.hideturtle() 

	# clear everything 
	def clear(self): 
		self.t.clear() 

# A class for animating spirographs 
class SpiroAnimator: 
	# constructor 
	def __init__(self, N): 
		# timer value in milliseconds 
		self.deltaT = 10
		# get window dimensions 
		self.width = turtle.window_width() 
		self.height = turtle.window_height() 
		# create spiro objects 
		self.spiros = [] 
		for i in range(N): 
			# generate random parameters 
			rparams = self.genRandomParams() 
			# set spiro params 
			spiro = Spiro(*rparams) 
			self.spiros.append(spiro) 
		# call timer 
		turtle.ontimer(self.update, self.deltaT) 
	
	# restart sprio drawing 
	def restart(self): 
		for spiro in self.spiros: 
			# clear 
			spiro.clear() 
			# generate random parameters 
			rparams = self.genRandomParams() 
			# set spiro params 
			spiro.setparams(*rparams) 
			# restart drawing 
			spiro.restart() 

	# generate random parameters 
	def genRandomParams(self): 
		width, height = self.width, self.height 
		R = random.randint(50, min(width, height)//2) 
		r = random.randint(10, 9*R//10) 
		l = random.uniform(0.1, 0.9) 
		xc = random.randint(-width//2, width//2) 
		yc = random.randint(-height//2, height//2) 
		col = (random.random(), 
			random.random(), 
			random.random()) 
		return (xc, yc, col, R, r, l) 

	def update(self): 
		# update all spiros 
		nComplete = 0
		for spiro in self.spiros: 
			# update 
			spiro.update() 
			# count completed ones 
			if spiro.drawingComplete: 
				nComplete+= 1
		# if all spiros are complete, restart 
		if nComplete == len(self.spiros): 
			self.restart() 
		# call timer 
		turtle.ontimer(self.update, self.deltaT) 

	# toggle turtle on/off 
	def toggleTurtles(self): 
		for spiro in self.spiros: 
			if spiro.t.isvisible(): 
				spiro.t.hideturtle() 
			else: 
				spiro.t.showturtle() 
			
# save spiros to image 
def saveDrawing(): 
	# hide turtle 
	turtle.hideturtle() 
	# generate unique file name 
	dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S") 
	fileName = 'spiro-' + dateStr 
	print('saving drawing to %s.eps/png' % fileName) 
	# get tkinter canvas 
	canvas = turtle.getcanvas() 
	# save postscipt image 
	canvas.postscript(file = fileName + '.eps') 
	# use PIL to convert to PNG 
	img = Image.open(fileName + '.eps') 
	img.save(fileName + '.png', 'png') 
	# show turtle 
	turtle.showturtle() 

# main() function   
def main(): 
	# use sys.argv if needed 
	print('generating spirograph...') 
	# create parser 
	descStr = """This program draws spirographs using the Turtle module. 
	When run with no arguments, this program draws random spirographs. 
	
	Terminology: 

	R: radius of outer circle. 
	r: radius of inner circle. 
	l: ratio of hole distance to r. 
	"""
	parser = argparse.ArgumentParser(description=descStr) 
	
	# add expected arguments 
	parser.add_argument('--sparams', nargs=3, dest='sparams', required=False, 
						help="The three arguments in sparams: R, r, l.") 
						

	# parse args 
	args = parser.parse_args() 

	# set to 80% screen width 
	turtle.setup(width=0.8) 

	# set cursor shape 
	turtle.shape('turtle') 

	# set title 
	turtle.title("Spirographs!") 
	# add key handler for saving images 
	turtle.onkey(saveDrawing, "s") 
	# start listening 
	turtle.listen() 

	# hide main turtle cursor 
	turtle.hideturtle() 

	# checks args and draw 
	if args.sparams: 
		params = [float(x) for x in args.sparams] 
		# draw spirograph with given parameters 
		# black by default 
		col = (0.0, 0.0, 0.0) 
		spiro = Spiro(0, 0, col, *params) 
		spiro.draw() 
	else: 
		# create animator object 
		spiroAnim = SpiroAnimator(4) 
		# add key handler to toggle turtle cursor 
		turtle.onkey(spiroAnim.toggleTurtles, "t") 
		# add key handler to restart animation 
		turtle.onkey(spiroAnim.restart, "space") 

	# start turtle main loop 
	turtle.mainloop() 

# call main 
if __name__ == '__main__': 
	main() 

