#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY projectCosts
#  2. INTEGER target
#

def countPairs(projectCosts, target):
    target = int(target)
    n = 0
    projectCosts = list(map(int, projectCosts))
    projectCosts.sort()
    s_costs = projectCosts
    l_costs = projectCosts[1:]
    
    for s_cost in s_costs:
        t = s_cost + target
        while len(l_costs) > 0:
            l_cost = l_costs[0]
            if t > l_cost:
                l_costs.pop(0)
            else:
                if t == l_cost:
                    n+=1
                    l_costs.pop(0)
                break
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    projectCosts_count = int(input().strip())

    projectCosts = []

    for _ in range(projectCosts_count):
        projectCosts_item = int(input().strip())
        projectCosts.append(projectCosts_item)

    target = int(input().strip())

    result = countPairs(projectCosts, target)

    fptr.write(str(result) + '\n')

    fptr.close()
