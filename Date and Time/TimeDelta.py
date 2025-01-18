#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime
date_format = "%a %d %b %Y %H:%M:%S %z"
# Complete the time_delta function below.
def time_delta(t1, t2):
    d1 = datetime.strptime(t1, date_format)
    d2 = datetime.strptime(t2, date_format)
    if d2 < d1:
        return str(int((d1 - d2).total_seconds()))
    else :
        return str(int((d2 - d1).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# # SAMPLE INPUT:
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

#--------Yashvi Bhadania--------
