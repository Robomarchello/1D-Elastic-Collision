#elastic collision is a collision where kinetic energy always the same
#m1 v1 = m2 v2
#v1 + v2 = v1f + v2f
import math

def get_elastic(vel1, mass1, vel2, mass2):
    #variable names are placeholders
    ratio1 = (mass1 - mass2) / (mass1 + mass2)
    ratio2 = (2 * mass1) / (mass1 + mass2)
    ratio3 = (2 * mass2) / (mass1 + mass2)

    vel1f = ratio1 * vel1 + ratio3 * vel2
    vel2f = ratio2 * vel1 + ratio1 * vel2

    print(f'before: v1={vel1} v2={vel2}')
    print(f'after: v1={vel1f} v2={vel2f}')

get_elastic(4, 3, -6, 5)

