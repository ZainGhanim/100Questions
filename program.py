import numpy as numpy
import matplotlib.pyplot as plot
import pandas as pandas

# number 1
radPrev = 0
radCurr = 0
setPoint = 12
timeAxis = []
angleAxis = []

for x in range(0,100):
    radCurr = 0.86*radPrev + 0.14*setPoint
    radPrev = radCurr
    timeAxis.append(x)
    angleAxis.append(radCurr)

plot.plot(timeAxis, angleAxis)
plot.xlabel("Time")
plot.ylabel("Angle")
plot.show()

# number 3
radPrev = 0
radCurr = 0
setPoint = 12
timeAxis = []
angleAxis = []
anglePrev = 0

for x in range(0, 100):
    radCurr = 0.86*radPrev + 0.14*setPoint
    radPrev = radCurr
    angle = anglePrev + 0.1*radCurr
    anglePrev = angle
    timeAxis.append(x)
    angleAxis.append(radCurr)

plot.plot(timeAxis, angleAxis)
plot.xlabel("Time")
plot.ylabel("Angle")
plot.show()

# number 5
radPrev = 0
radCurr = 0
P = 0.2
I = 0
D = 0
setPoint = 12
timeAxis = []
angleAxis = []
anglePrev = 0
angleSetpoint = 3.14

for x in range(0, 100):
    error = angleSetpoint - angle
    setPoint = 0.2*error
    radCurr = 0.86*radPrev + 0.14*setPoint
    radPrev = radCurr
    angle = anglePrev + 0.1*radCurr
    anglePrev = angle
    timeAxis.append(x)
    angleAxis.append(radCurr)

plot.plot(timeAxis, angleAxis)
plot.xlabel("Time")
plot.ylabel("Angle")
plot.show()

# number 6
radPrev = 0
radCurr = 0
P = 0.2
I = 0
D = 0
setPoint = 12
timeAxis = []
angleAxis = []
anglePrev = 0
angleSetpoint = 3.14

for x in range(0, 100):
    error = angleSetpoint - angle
    setPoint = 10*error
    radCurr = 0.86*radPrev + 0.14*setPoint
    radPrev = radCurr
    angle = anglePrev + 0.1*radCurr
    anglePrev = angle
    timeAxis.append(x)
    angleAxis.append(radCurr)

plot.plot(timeAxis, angleAxis)
plot.xlabel("Time")
plot.ylabel("Angle")
plot.show()

# number 7
radPrev = 0
radCurr = 0
P = 0.2
I = 0
D = 0
setPoint = 12
timeAxis = []
angleAxis = []
anglePrev = 0
angleSetpoint = 3.14
errorPrev = 0

for x in range(0, 100):
    error = angleSetpoint - angle
    setPoint = 5*((error - errorPrev)/0.1) + 10*error
    errorPrev = error
    radCurr = 0.86*radPrev + 0.14*setPoint
    radPrev = radCurr
    angle = anglePrev + 0.1*radCurr
    anglePrev = angle
    timeAxis.append(x)
    angleAxis.append(radCurr)

plot.plot(timeAxis, angleAxis)
plot.xlabel("Time")
plot.ylabel("Angle")
plot.show()

#number 7 reference
wPrev = 0
wSet = 12
thetaPrev = 0
Iarr = []
wArr = []
thetaArr = []
thetaSetPoint = 3.14
errorPrev = 0
angleOfWheel = thetaPrev

for i in range(0, 100):
    error = thetaSetPoint - angleOfWheel
    wSet = 5*((error-errorPrev)/.1) + (10*error)
    errorPrev = error
    angleVelocity = (.86*wPrev) + (.14*wSet)
    wPrev = angleVelocity
    angleOfWheel = thetaPrev + (.1*angleVelocity)
    thetaPrev = angleOfWheel
    """plotting"""
    thetaArr.append(angleOfWheel)
    Iarr.append(i)

plot.plot(Iarr, thetaArr)
plot.xlabel("time")
plot.ylabel("Angle in Radians")
plot.show()
