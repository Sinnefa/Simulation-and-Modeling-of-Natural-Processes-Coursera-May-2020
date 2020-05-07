import numpy as np
import math

class Integrator:
    xMin = 0
    xMax = 0
    N = 0
    s = 0
    def __init__(self, xMin, xMax, N):
        self.xMin=xMin
        self.xMax=xMax
        self.N=N    
            
    def integrate(self):       
        dx = (self.xMax-self.xMin)/(self.N) 
        for i in range(0,self.N-1):
            xi = self.xMin + i*dx
            fx = np.power(xi,2)*np.power(math.e,-xi)*math.sin(xi)
            self.s=self.s+fx
        self.s=self.s*dx
    def show(self):
        print(round((self.s),5))
        

examp = Integrator(1,3,200000)
examp.integrate()
examp.show()
