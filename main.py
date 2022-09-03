import numpy as np
import math

def solve_ik(link = [], theta = [], pos = [], eps = 0.01, n = 10000):

    #Defining the links
    a1 = link[0]
    a2 = link[1]
    a3 = link[2]

    end_pos = np.array([[pos[0]], [pos[1]]])
    i = 0
    tht = np.array([[theta[0]], [theta[1]], [theta[2]]])
    while i < n:
        # Definition of foward kinematics
        f_x = a1 * math.cos(tht[0]) + a2 * math.cos(tht[0] + tht[1]) + a3 * math.cos(tht[0] + tht[1] + tht[2])
        f_y = a1 * math.sin(tht[0]) + a2 * math.sin(tht[0] + tht[1]) + a3 * math.sin(tht[0] + tht[1] + tht[2])

        # Putting foward kinematics formula into a numpy array
        f_XY = np.array([[f_x], [f_y]])

        # Definition of the Jacobian matrix
        j = np.array([
                     [-a1 * math.sin(tht[0]) - a2 * math.sin(tht[0] + tht[1]) - a3 * math.sin(tht[0] + tht[1] + tht[2]),\
                      -a2 * math.sin(tht[0] + tht[1]) - a3 * math.sin(tht[0] + tht[1] + tht[2]),
                      -a3 * math.sin(tht[0] + tht[1] + tht[2])],\
                     [a1 * math.cos(tht[0]) + a2 * math.cos(tht[0] + tht[1]) + a3 * math.cos(tht[0] + tht[1] + tht[2]),\
                      a2 * math.cos(tht[0] + tht[1]) + a3 * math.sin(tht[0] + tht[1] + tht[2]),
                      a3 * math.cos(tht[0] + tht[1] + tht[2])]])
        #error term for the formula
        err = f_XY - end_pos

        #update formula to be iterated
        new_val = tht - np.matmul(np.linalg.pinv(j), err)
        #print( np.matmul(np.linalg.pinv(j), err).shape)
        tht = new_val
        #print("New values: ", new_val)
        #print("error:", err)
        print("Iteration count: ", i)
        if abs(err[0]) < eps and abs(err[1]) < eps:
            print("New values: ", new_val)
            break
        i += 1


if __name__ == '__main__':
    solve_ik([10, 5, 4], [15, 60, 10], [6.81, 9.02])
    print("X: ", 10 * math.cos(20) + 5 * math.cos(20 + 50) + 4 * math.cos(20 + 50 + 10))
    print("Y: ", 10 * math.sin(20) + 5 * math.sin(20 + 50) + 4 * math.sin(20 + 50 + 10))
    print("X: ", 10 * math.cos(13.31869105) + 5 * math.cos(13.31869105 + 58.48281417) + 4 * math.cos(13.31869105 + 58.48281417 + 16.1596998))
    print("Y: ", 10 * math.sin(13.31869105) + 5 * math.sin(13.31869105 + 58.48281417) + 4 * math.sin(13.31869105 + 58.48281417 + 16.1596998))


