"""
Author(s) : 
This script allows step by step localisation of the car using icp
"""

from math import pi,sin,cos

def movement(prev_data, new_data):
    """Renvoie (dx,dy), le déplacement de la voiture en une étape de durée dt"""
    deltas = [(i,new_data[i]-prev_data[i]) for i in range(len(new_data))]
    min_dist = float("inf")
    min_delta = 0
    for d in deltas:
        moved_data = [new_data[j]-d[1] for j in range(len(new_data))]
        dist = sum(moved_data)
        if dist < min_dist:
            min_dist = dist
            min_delta = d
    theta = -1*(min_delta[0]-90)*pi/180
    r = min_delta[1]
    return (-r*cos(theta), -r*sin(theta))
        