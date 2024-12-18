

import math
import matplotlib.pyplot as plt

v_initial = 6.43
launch_angle = 10
float_angle_deg = 0

rho = 1.204
A = 0.03325
m = 0.035
y = 1.8
x = 0

angle = launch_angle/360 * 2 * math.pi
float_angle_rad = float_angle_deg/360 * 2 * math.pi

dt=0.001
t=0
v=v_initial
g=-9.81
coef = 0.3674
x_plot = []
y_plot = []
angle_plot = []


v_x = v * math.cos(angle)
v_y = v * math.sin(angle)

while y > 0:
    angle = math.atan(v_y/v_x)
    if angle < float_angle_rad :
        angle = float_angle_rad 

    lift = coef * rho * A * v * v / 2
    lift_x = - lift * math.sin(angle)
    lift_y = lift * math.cos(angle)
    a_x = lift_x / m 
    a_y =  lift_y  / m + g

    v_x = v_x + a_x * dt
    v_y = v_y + a_y * dt

    x= x+ v_x * dt 
    y= y + v_y * dt
    t= t + dt
    x_plot.append (x)
    y_plot.append (y)
    angle_plot.append (angle)
    v = math.sqrt(v_x * v_x + v_y * v_y )


print (t)
plt.plot (x_plot,y_plot)
plt.plot(x_plot,angle_plot)
print (x)

    

