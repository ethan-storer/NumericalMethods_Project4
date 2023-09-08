import scipy as sp
import matplotlib.pyplot as plt
import math as math
from Heun import*
from RungeKutta import*
from calcK import*
from slope import*
from scipy import integrate
from Order3 import*
from math import*
import time


#Ta is a function of time
T=90
t0=0
k=0.25 #min^-1
Tf=20 #°C
def fun(t,T): return (-k*(T-(5*cos((pi*t)+Tf))))
t_span=(0, 20)
y0=[90]
t_eval = np.arange(21)
first_step = 1
A, P, Q = Heun()


#Plot 2nd Order RungeKutta Iterations
StepSizes = [10,5,2,1,0.5]
#def RungeKutta(f, x0, y0, h, A, P, Q, n):
for i in range(0,len(StepSizes)):
    t = time.time() #stopwatch start
    [[xmatrix], [ymatrix]] = RungeKutta(fun, t0, T, StepSizes[i], A, P, Q, int(20/StepSizes[i]))
    elapsed = time.time() - t #stopwatch end
    print('2nd order time ', elapsed)

    plt.plot(xmatrix, ymatrix, marker="h", markersize=4, label=f'$Stepsize:{StepSizes[i]}$')
plt.xlabel('$time (minutes)$') # the horizontal axis represents the time
plt.ylabel('$Temperature (°C)$') # the vertical axis represents the Temperature in °C
plt.legend() # show how the colors correspond to the components of X
plt.show()



#3rd order RungeKutta
A, P, Q = Order3()
t = time.time()
[[xmatrix_O3], [ymatrix_O3]] = RungeKutta(fun, t0, T, first_step, A, P, Q, 20)
elapsed = time.time() - t
print('3rd order time ', elapsed)
#print([[xmatrix_O3], [ymatrix_O3]])


#Other Methods
t = time.time()
RK45=sp.integrate.solve_ivp(fun, t_span, y0, 'RK45', t_eval, first_step)
elapsed = time.time() - t
print('RK45 time ', elapsed)
#print(RK45)

t = time.time()
RK23=sp.integrate.solve_ivp(fun, t_span, y0, 'RK23', t_eval, first_step)
elapsed = time.time() - t
print('RK23 time ', elapsed)
#print(RK23)


t = time.time()
LSODA=sp.integrate.solve_ivp(fun, t_span, y0, 'LSODA', t_eval, first_step)
elapsed = time.time() - t
print('LSODA time ', elapsed)
#print(LSODA)


#Plot other methods and Order3

for i in range(RK45.y.shape[0]):
    plt.plot(RK45.t, RK45.y[i], marker="h", markersize=10, label=f'$RK45$')
    plt.plot(RK23.t, RK23.y[i], marker="o", markersize=6, label=f'$RK23$')
    plt.plot(LSODA.t, LSODA.y[i], marker=".", markersize=8, label=f'$LSODA$')
    plt.plot(xmatrix_O3, ymatrix_O3, marker="h", markersize=2, label=f'$Order3$')
plt.xlabel('$time (minutes)$') # the horizontal axis represents the time
plt.ylabel('$Temperature (°C)$') # the vertical axis represents the Temperature in °C
plt.legend() # show how the colors correspond to the components of X
plt.show()