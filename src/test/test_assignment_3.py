#euler method



#initial conditions are

def eulerCalc(t0,y0,iterations,tEnd):
    stepSize = (tEnd-t0)/iterations
    tValues = []
    yValues = []
    for x in range(iterations+1):
        tValues.append(x*stepSize + t0)
        yValues.append(0)
    yValues[0] = y0

    for x in range(iterations):
        yValues[x+1] = yValues[x] + stepSize*eulerFunc(tValues[x],yValues[x])

    print(yValues[x+1])


def rungeKutta(t0,y0,iterations,tEnd):
    stepSize = (tEnd-t0)/iterations
    tValues = []
    yValues = []
    for x in range(iterations+1):
        tValues.append(x*stepSize + t0)
        yValues.append(0)
    yValues[0] = y0
    for x in range(iterations):
        k1=stepSize*rungeFunc(tValues[x],yValues[x])
        k2=stepSize*rungeFunc(tValues[x] + stepSize/2,yValues[x]+k1/2)
        k3=stepSize*rungeFunc(tValues[x]+ stepSize/2,yValues[x] + k2/2)
        k4=stepSize*rungeFunc(tValues[x]+ stepSize,yValues[x]+k3)
        yValues[x+1] = yValues[x] + (1/6)*(k1+2*k2+2*k3+k4)
    print(yValues[x+1])


#testing 

#test inputs are
#function at t-y^2
#range 0<t<2
#iterations: 10
#initial point f(0) =1
def eulerFunc(t,y):
    return t-y**2

eulerCalc(0,1,10,2)
print()
def rungeFunc(t,y):
    return t-y**2
rungeKutta(0,1,10,2)