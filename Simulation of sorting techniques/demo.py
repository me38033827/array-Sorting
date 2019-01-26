import sortTech
import numpy as np
import time
import pandas as pd
import generateSortness as gs
import Sortedness as sn
from matplotlib import pyplot as plt
import sys
import psutil
import os

sys.setrecursionlimit(3000000)

data=pd.read_csv('data/creditcard.csv')

print list((data['V1']))[3000]
