import math
from pprint import pprint
m = 1
k = 1

# y - Velocity and Position are 0 as we have a spring 
# in horizontal Direction fixed at x0
def expEuler(v, pos, dt):
    f = - pos * k
    pos_new = pos + v * dt
    v_new = v + dt * f/m
    return (v_new, pos_new)

def analytic(v, pos, t, dt):
    pos_new = math.cos(math.sqrt(k/m) * t)
    v_new = -math.sqrt(k/m) * math.sin(math.sqrt(k/m) * t)
    return (v_new, pos_new)

def loop(dt):
    timstep = 0.1 
    v = 0.0
    pos = 1.0
    t = 0
    eulersolution = []
    error = []

    for j in range(1, 4): # 1-2-3
        solution = analytic(v, pos, j/10, dt)
        eulersolution = []

        for i in range(math.ceil((j/10) / dt)):
            if i == 0:
                newsol = expEuler(v, pos, dt)
                eulersolution.append(newsol)
            else: 
                newsol = expEuler(eulersolution[-1][0], eulersolution[-1][1], dt)
                eulersolution.append(newsol)
        error.append(round(eulersolution[-1][1] - solution[1], 5))
    
    return error

def main():
    errors = []
    errors.append(loop(0.1))
    errors.append(loop(0.05))
    errors.append(loop(0.025))
    for error in errors:
        print (error)
        print ("\n")

main()
