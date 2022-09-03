import numpy as np
import matplotlib.pyplot as plt


def cubic_traj(start_val=[10,5,30,8], end_val=[50,0,80,0], end_time = 10, steps =10, start_time = 0):
    a0 = 0
    a1 = 0
    a2 = 0
    a3 = 0
    t = start_time
    a_ = np.array([[a0], [a1], [a2], [a3]])
    t_values = np.array([[1, t, t**2, t**3],[0, 1, 2*t, 3*t**2]])
    path = []
    path.append(start_val)
    timestep = []
    a01_values = []
    a23_values = []
    x = 0
    for i in range(int(len(start_val)/2)):
        a01_values.append([start_val[x], start_val[x+1]])
        x += 2
    print(a01_values[0][1])
    print(a01_values)
    x = 0
    for i in range( int(len(start_val)/2)):
        theta = np.array([[end_val[x] - a01_values[i][0]], [end_val[x+1] - a01_values[i][1]]])
        t_ = np.array([[end_time**2, end_time**3], [2*end_time, 3*end_time**2]])
        a23 = np.matmul(np.linalg.pinv(t_), theta)
        print(a23.shape)
        x+=2
        #a23_values.append([a23[i , 0], a23[i+1, 0]])
    #print(a23_values)
'''
    #solving for a0 & a1
    for i in range(int(len(start_val)/2)):
        temp = []
        theta = [start_val[i], start_val[i+1]]
        a_ = np.matmul(np.linalg.pinv(t_values), theta)
        temp.append([a_[0],a_[1]])
        a01_values.append(temp)
        print(a01_values)

    #solving for a2 & a3
    for i in range(int(len(start_val)/2)):
        theta = np.array([[end_val[-2]], [end_val[-1]]])
        t_ = np.array([t**2, t**3],[2*t, 3*t**2])
        a23_values = np.matmul(np.linalg.pinv(t_), theta)
'''          

#call function in this form [theta1, theta1_dot, theta2, theta2_dot .....]  

cubic_traj()